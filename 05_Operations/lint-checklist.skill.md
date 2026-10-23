---
title: "Revisión del vault"
type: skill
status: active
scope: system
updated: 2026-10-23
---

# Revisión del vault

## Cuándo aplicar

Después de una ingesta importante, antes de usar un resultado o cuando aparezcan fuentes contradictorias.

## Procedimiento

1. Ejecutar el verificador local para revisar estructura y enlaces.
2. Leer las notas afectadas y contrastarlas con las fuentes y fechas.
3. Revisar que no se hayan mezclado clientes ni convertido hipótesis en hechos.
4. Revisar índices, manifiesto y pendientes. Marcar lo desactualizado y proponer correcciones.
5. Registrar cambios efectivamente realizados. Una revisión de lectura puede terminar con un reporte sin modificar archivos.

## Stack de ejecución

- Herramientas: lectura de archivos; Python 3.9+ opcional para el chequeo estructural.
- Entradas: cliente/proyecto o conjunto de notas elegido.
- Salida: hallazgos con ruta, evidencia y corrección concreta.
- Registro: run log si hubo cambios relevantes; manifiesto si se procesaron fuentes.

## Límite

El script detecta algunos errores mecánicos. La revisión de contenido determina si los hechos siguen vigentes y si las fuentes los sostienen.
