#!/usr/bin/env python3
"""Chequeo local de estructura y señales sensibles. Solo biblioteca estándar."""

import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


SKIP_DIRS = {
    '.git', '.obsidian', '.venv', 'node_modules', '__pycache__', '.cache',
    '.hermes', '.codex', '.claude', '.hub',
}
TYPES = ('kb', 'skill', 'agent', 'brief', 'wiki', 'spec', 'plan')
SECRET_PATTERNS = {
    'clave privada': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'token de GitHub': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b'),
    'clave de proveedor': re.compile(r'\bsk-[A-Za-z0-9_-]{24,}\b'),
    'clave AWS': re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    'ruta personal': re.compile(r'(?:/Users/|/home/)[A-Za-z0-9_.-]+/|[A-Z]:\\Users\\[A-Za-z0-9_.-]+\\'),
}


def check(root):
    root = root.resolve()
    errors = []
    files = []

    def fail(path, message):
        errors.append(f'{path.relative_to(root)}: {message}')

    for current, dirs, names in os.walk(root, followlinks=False):
        base = Path(current)
        for name in dirs[:]:
            path = base / name
            if path.is_symlink():
                fail(path, 'enlace simbólico: revisar el destino antes de compartir')
                dirs.remove(name)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        files.extend(base / name for name in names)

    texts = {}
    for path in sorted(files):
        if path.is_symlink():
            fail(path, 'enlace simbólico: revisar el destino antes de compartir')
            continue
        name = path.name.lower()
        if (name == '.env' or name.startswith('.env.') or name.endswith('.env')
                or name in {'auth.json', 'state.db'}
                or name.startswith('credentials')
                or path.suffix.lower() in {'.pem', '.key', '.p12', '.db', '.sqlite', '.sqlite3', '.log', '.zip'}):
            fail(path, 'archivo potencialmente sensible o exportación: revisar y retirar de la distribución')
        try:
            text = path.read_text(encoding='utf-8-sig')
        except (UnicodeDecodeError, OSError):
            fail(path, 'archivo no legible como texto; requiere revisión manual')
            continue
        if '\x00' in text:
            fail(path, 'contenido binario: requiere revisión manual')
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                # Nunca mostrar la coincidencia: podría ser un secreto.
                fail(path, f'señal de {label}; revisar sin copiar el valor a un reporte')
        if path.suffix == '.md':
            texts[path] = text

    for required in ('AGENTS.md', '00_Index.md', 'README.md', 'templates/cliente/00_index.wiki.md'):
        if not (root / required).is_file():
            errors.append(f'{required}: falta entrada requerida')

    def exists(source, target, wiki=False):
        target = unquote(target.strip().strip('<>'))
        if not target or target.startswith('#') or urlsplit(target).scheme:
            return True
        target = target.split('#', 1)[0].split('?', 1)[0]
        candidates = [source.parent / target]
        if wiki:
            candidates.append(root / target)
            candidates += [Path(str(p) + '.md') for p in candidates if not str(p).endswith('.md')]
        for candidate in candidates:
            resolved = candidate.resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                continue
            if resolved.exists():
                return True
        return False

    for path, text in texts.items():
        typed = next((kind for kind in TYPES if path.name.endswith(f'.{kind}.md')), None)
        front = re.match(r'\A---\s*\n(.*?)\n---(?:\n|$)', text, re.S)
        if typed:
            if not front:
                fail(path, 'nota tipada sin frontmatter')
            else:
                metadata = front.group(1)
                for field in ('type', 'status', 'scope', 'updated'):
                    if not re.search(rf'^{field}:\s*\S', metadata, re.M):
                        fail(path, f'falta metadato {field}')
                if not re.search(r'^(?:title|name):\s*\S', metadata, re.M):
                    fail(path, 'falta title o name')
                if not re.search(rf'^type:\s*{typed}\s*$', metadata, re.M):
                    fail(path, 'type no coincide con el sufijo')
        if typed == 'skill' and '## Stack de ejecución' not in text:
            fail(path, 'falta Stack de ejecución')
        if typed == 'brief' and '## Trazabilidad de agente' not in text:
            fail(path, 'falta Trazabilidad de agente')
        if path.name == 'SKILL.md':
            if not front or not all(re.search(rf'^{field}:\s*\S', front.group(1), re.M) for field in ('name', 'description')):
                fail(path, 'paquete skill sin name/description')
        if front:
            imports = re.search(r'^imports:\s*\n((?:[ \t]+.*\n?)*)', front.group(1), re.M)
            if imports:
                for target in re.findall(r'^\s*-\s*[\"\']?@([^\"\'\n]+)', imports.group(1), re.M):
                    candidate = (root / target.strip()).resolve()
                    if not candidate.is_relative_to(root) or not candidate.is_file():
                        fail(path, 'import inexistente o fuera del vault')
        # Los ejemplos de código no se interpretan como enlaces de navegación.
        content = re.sub(r'^(`{3,}|~{3,}).*?^\1\s*$', '', text, flags=re.M | re.S)
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', content):
            if not exists(path, target):
                fail(path, f'enlace local roto: {target}')
        for target in re.findall(r'\[\[([^\]\n]+)\]\]', content):
            target = target.split('|', 1)[0]
            if not exists(path, target, wiki=True):
                fail(path, f'wikilink roto: {target}')

    clients = root / '02_Clients'
    if clients.is_dir():
        for folder in sorted(clients.iterdir()):
            if folder.is_dir() and not folder.name.startswith('.'):
                for required in ('00_index.wiki.md', 'profile.kb.md'):
                    if not (folder / required).is_file():
                        fail(folder, f'falta {required}')
    return files, texts, errors


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
    if not root.is_dir():
        print('ERROR: la raíz del vault no existe.')
        return 2
    files, texts, errors = check(root)
    for error in errors:
        print(f'ERROR: {error}')
    print(f'{len(files)} archivos; {len(texts)} Markdown; {len(errors)} hallazgos.')
    print('Chequeo local orientativo. Revisar contenido y todo el historial antes de publicar.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
