# Skills runtime de la edición comunitaria

La ubicación canónica es [.agents/skills](../../.agents/skills/README.md), compartida por herramientas compatibles con ese formato. Esta carpeta conserva el lugar del mapa original y explica la adaptación; no contiene perfiles ni skills privadas.

| Paquete | Función |
|---|---|
| `acs-ingest` | Promover una fuente a conocimiento con trazabilidad |
| `acs-query` | Consultar un cliente/proyecto con evidencia |
| `acs-lint` | Revisar estructura y vigencia del conocimiento |

La [guía](../../05_Operations/implementacion.wiki.md) explica la carga en Hermes y Codex. Las skills operan cuando el agente las carga con acceso al vault; un archivo Markdown no ejecuta un modelo por sí solo.
