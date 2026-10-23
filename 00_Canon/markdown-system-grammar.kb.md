---
title: "Gramática Markdown del sistema"
type: kb
status: active
scope: system
updated: 2026-10-23
---

# Gramática Markdown del sistema

Elegí el tipo por la función de la nota.

| Tipo | Función | Ejemplo |
|---|---|---|
| `.kb.md` | Conocimiento durable con evidencia | `profile.kb.md` |
| `.skill.md` | Procedimiento reutilizable documentado | `lint-checklist.skill.md` |
| `.agent.md` | Rol o prompt para aplicar a una tarea | `knowledge-curator.agent.md` |
| `.brief.md` | Objetivo, restricciones y resultado puntual | `presentacion.brief.md` |
| `.wiki.md` | Explicación o recorrido humano | `implementacion.wiki.md` |
| `.spec.md` | Diseño todavía no implementado | `template.spec.md` |
| `.plan.md` | Pasos y criterio de aceptación | `template.plan.md` |
| `.md` | README, índices, instrucciones y registros livianos | `AGENTS.md` |

## Metadatos

Las notas tipadas empiezan con YAML entre líneas `---`. Usar `title` (o `name` para roles), `type`, `status`, `scope` y fecha `updated` en formato ISO. En una plantilla vacía la fecha puede quedar como `YYYY-MM-DD` hasta completarla.

Estados útiles: `draft`, `active`, `deprecated`. El estado `example` identifica material ficticio. Una plantilla sigue en `draft` hasta que se completa y se revisa.

## Enlaces e imports

Preferí enlaces Markdown relativos con extensión `.md`: funcionan en GitHub y Obsidian. También podés usar wikilinks; resolvelos desde la nota o desde la raíz y evitá nombres ambiguos. Los placeholders de una plantilla no son enlaces válidos hasta reemplazarlos.

`imports` en un `.agent.md` es una lista de archivos que el agente debe leer; el prefijo `@` significa relativo a la raíz del vault. Es una convención documentada, no un importador de código.

## Runtime

Una nota `.skill.md` no se instala sola. Un paquete descubrible tiene `SKILL.md` con `name` y `description` en su propia carpeta bajo `.agents/skills/`. Un `.agent.md` tampoco crea subagentes automáticamente.
