---
title: "Privacidad y sincronización"
type: kb
status: active
scope: system
updated: 2026-10-23
---

# Privacidad y sincronización

## Plantilla pública, memoria privada

La distribución pública contiene únicamente reglas genéricas, plantillas y ejemplos inventados. Los clientes, reuniones, campañas, documentos de trabajo, IDs operativos y perfiles de personas reales van en una copia privada con accesos controlados.

El `.gitignore` reduce errores; no elimina archivos que ya estén versionados ni borra commits antiguos. Un dato eliminado de una nota puede seguir en el historial. Antes de compartir cualquier copia, revisar el contenido y toda su historia.

## Fuera del vault

Guardar credenciales, archivos de autenticación, bases de sesiones, caches, registros técnicos y configuración completa del agente fuera del repositorio. Las conexiones se autentican directamente en cada proveedor o conector.

## Herramientas y modelos

Un vault local no garantiza procesamiento local. Un proveedor de modelos remoto recibe el contexto que se le envía; cada conector tiene permisos propios. Elegí herramientas y accesos según el material que vas a procesar.

## Sincronizar

Podés usar Git privado o un sistema de sincronización de archivos. Evitá ediciones simultáneas sobre la misma nota y revisá los conflictos antes de aceptar una versión. La configuración local de Obsidian se ignora para que cada persona configure su interfaz.
