---
name: acs-lint
description: Revisar estructura, enlaces, trazabilidad y vigencia de un vault ACS-v2. Usar para mantenimiento del conocimiento, no para auditorías de infraestructura ni certificación de privacidad.
---

# acs-lint

Leé AGENTS.md, 00_Index.md y `05_Operations/lint-checklist.skill.md` en la raíz del vault. Acotá la revisión al alcance pedido.

Si Python está disponible, ejecutá `python3 05_Operations/scripts/check_vault.py` desde la raíz y conservá su resultado. Si no, revisá manualmente y explicá qué no pudo automatizarse.

Contrastá las notas relevantes con sus fuentes, fechas e índices. Buscá contradicciones, claims sin evidencia, separación entre clientes y pendientes omitidos. El éxito del script no prueba que el contenido sea correcto o público.

Reportá hallazgos con ruta, evidencia, consecuencia y propuesta. Corregí dentro del alcance autorizado; registrá cambios relevantes y repetí el chequeo si cambiaste estructura o enlaces. No publiques ni actives automatizaciones por una tarea de mantenimiento.
