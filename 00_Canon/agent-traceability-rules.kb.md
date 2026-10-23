---
title: "Trazabilidad de agentes"
type: kb
status: active
scope: system
updated: 2026-10-23
---

# Trazabilidad de agentes

Cada resultado importante debe permitir reconstruir sus insumos y límites. Registrá los archivos efectivamente leídos, las skills efectivamente usadas, el resultado y lo pendiente.

Un brief incluye `## Trazabilidad de agente`. Un procedimiento `.skill.md` incluye `## Stack de ejecución`: herramientas necesarias, entradas, salidas y registro esperado. Ver las [plantillas](../templates/README.md).

El [manifiesto](../05_Operations/source-manifest.kb.md) relaciona fuentes y notas derivadas. El [run log](../05_Operations/agent-run-log.md) registra operaciones breves. Ambos comienzan vacíos salvo por la demostración ficticia declarada.

La trazabilidad declarada no es una auditoría técnica completa del modelo. No atribuir al agente lecturas, herramientas o aprobaciones que no ocurrieron.
