# Achalay OS · Plantilla para la comunidad

Un segundo cerebro en Markdown para que vos y tus agentes trabajen con contexto, fuentes y procedimientos reutilizables.

**[Empezá por la guía de implementación](05_Operations/implementacion.wiki.md)** · [Explorá el índice](00_Index.md) · [Probá el ejemplo ficticio](02_Clients/demo-taller/00_index.wiki.md)

Esta es una edición pública de la estructura de Achalay OS / ACS-v2. Incluye reglas genéricas, plantillas vacías, tres skills de operación y un caso inventado. Fue construida como un repositorio independiente, sin el historial, los clientes, los perfiles personales ni los procesos privados de la instalación original.

## Cómo funciona

```text
Una fuente entra → se extrae conocimiento con evidencia → se aplica a una tarea
                                    ↓
                      quedan enlaces, fuentes y pendientes
```

Los archivos quedan en tu carpeta. Obsidian permite navegar las notas; un agente con acceso a archivos puede consultarlas y editarlas. La plantilla no ejecuta modelos ni conecta servicios por sí sola. La documentación explica el uso con Hermes y Codex; también podés usarla manualmente con otro asistente.

## Arranque rápido

1. Descargá el ZIP desde **Code → Download ZIP** y descomprimilo, o usá Git:

   ```bash
   git clone https://github.com/achalaymarketing/achalay-os-template.git
   cd achalay-os-template
   ```

2. Abrí la carpeta como vault existente en Obsidian y entrá a `00_Index.md`.
3. Abrí la misma carpeta en tu agente y pedile:

   > Leé AGENTS.md y 00_Index.md. Recorré únicamente el cliente ficticio demo-taller. Explicame cómo se conectan su fuente, su conocimiento y su brief. No modifiques archivos.

4. Para usar datos propios, creá una copia local separada o un repositorio **privado** siguiendo la guía. Una plantilla pública sirve para distribuir el sistema; tu memoria de trabajo necesita su propio destino.

## Qué incluye

| Carpeta | Para qué sirve |
|---|---|
| `00_Canon/` | Reglas del sistema y gramática de archivos |
| `01_Agency/` | Espacio vacío para tu organización o actividad |
| `02_Clients/` | Contexto por cliente o proyecto, con una demostración ficticia |
| `03_Library/` | Procedimientos, roles y explicación del runtime |
| `04_Inbox/` | Entrada de material todavía sin procesar |
| `05_Operations/` | Guía, registro de fuentes, mantenimiento y verificador |
| `06_Archive/` | Espacio para material retirado, sin historial precargado |
| `templates/` | Modelos para notas, briefs y alta de clientes |
| `.agents/skills/` | Skills genéricas: ingesta, consulta y revisión |

No necesitás una base de datos, un servidor, plugins comunitarios ni automatizaciones para empezar. Python 3.9+ es opcional para ejecutar el verificador local. El agente y su proveedor de modelos se instalan/configuran por separado y pueden tener costo.

## Verificar la estructura

Desde la raíz:

```bash
python3 05_Operations/scripts/check_vault.py
```

El verificador revisa enlaces locales, metadatos, estructura de clientes y señales comunes de archivos sensibles. Es una ayuda para revisar; no certifica ausencia de información privada ni inspecciona todo el historial Git.

## Reutilización

Licencia [MIT](LICENSE): podés adaptar y compartir la plantilla, incluso para uso comercial, conservando el aviso de licencia. Las herramientas externas mantienen sus propias licencias y condiciones. Para proponer mejoras, mirá [CONTRIBUTING.md](CONTRIBUTING.md).
