---
title: "Modelo operativo ACS-v2"
type: kb
status: active
scope: system
updated: 2026-10-23
---

# Modelo operativo ACS-v2

El sistema separa cuatro cosas: la fuente original, lo que sabemos por esa fuente, el procedimiento que aplicamos y el resultado de una tarea.

```text
04_Inbox/ o sources/ → notas .kb.md → skill + contexto → resultado .brief.md
                            ↑                              ↓
                      índices y enlaces ← fuentes y registro
```

Obsidian muestra los archivos. El agente lee o escribe los archivos que la tarea requiere. Git puede versionarlos; un remoto privado permite compartir la memoria de trabajo con quienes correspondan.

## Decisiones de diseño

- Leer primero índices y después contexto específico.
- Una fuente conserva su origen; un resumen explica qué extrajo y qué no pudo confirmar.
- Una skill reutiliza el procedimiento; el cliente aporta su contexto. Evitar una skill distinta para cada cliente.
- Registrar decisiones y fuentes en forma breve. Los logs técnicos y las sesiones completas quedan fuera del vault.
- La plantilla comunitaria usa `.agents/skills/` como única ubicación de paquetes runtime. No replica perfiles, integraciones ni bundles de una instalación privada.

## Carpetas

Las ocho carpetas numeradas y de plantillas se describen en el [índice](../00_Index.md). Podés conservar `01_Agency` para tu actividad aunque no tengas una agencia, y usar `02_Clients` para proyectos personales. Renombrarlas requiere ajustar enlaces, reglas y verificador.
