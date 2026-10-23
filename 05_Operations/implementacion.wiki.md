---
title: "Cómo implementar Achalay OS"
type: wiki
status: active
scope: system
updated: 2026-10-23
---

# Cómo implementar Achalay OS

## Qué vas a poner en marcha

Una carpeta compartida entre vos y tu agente, con fuentes, conocimiento procesado, instrucciones y resultados enlazados. Podés empezar solo con Markdown y agregar Obsidian y un agente con acceso a archivos. La plantilla no necesita un servidor.

El objetivo de la primera prueba es simple: abrir el caso ficticio, encontrar la evidencia de una afirmación y producir un brief que no invente datos faltantes.

## 1. Conseguir tu copia

En el repositorio público, elegí **Code → Download ZIP** y descomprimilo. Si usás Git:

```bash
git clone https://github.com/achalaymarketing/achalay-os-template.git
cd achalay-os-template
```

Si aparece **Use this template**, podés crear un repositorio propio desde ese botón. Para trabajar con información propia, elegí visibilidad **Private**. Un fork público conserva su vínculo de distribución; para memoria privada conviene una copia independiente.

### Separar la prueba del trabajo real

Para una copia local sin Git, descargá otro ZIP y guardalo en una carpeta distinta. El ZIP de GitHub contiene los archivos de la plantilla, sin la carpeta `.git`. Antes de añadir datos reales, asegurate de estar en esa copia.

Si querés versionar esa copia, creá un repositorio privado vacío en tu cuenta de GitHub, sin README inicial. Desde la carpeta nueva descomprimida (sin `.git`):

```bash
git init -b main
git add .
git diff --cached --stat
git commit -m "Inicializar mi vault privado"
git remote add origin https://github.com/TU_USUARIO/TU_REPO_PRIVADO.git
```

Reemplazá usuario y nombre, comprobá en GitHub que ese destino diga **Private**, revisá `git remote -v` y recién entonces ejecutá `git push -u origin main`. No apuntes tu vault de trabajo al repositorio público de la comunidad.

## 2. Abrirlo en Obsidian

Instalá Obsidian desde su sitio oficial. Elegí **Open folder as vault / Abrir carpeta como bóveda** y seleccioná la raíz de tu copia, donde está `00_Index.md`. Abrí ese índice y seguí el enlace a Taller Demo.

No hace falta un plugin comunitario. Los enlaces Markdown funcionan de base. El grafo muestra relaciones creadas por enlaces; para que una nota aparezca conectada, enlazala desde su índice o desde otra nota pertinente. Obsidian guarda su configuración en `.obsidian/`, ignorada por Git en esta plantilla. [Referencia oficial](https://obsidian.md/help/vault).

## 3. Elegir un agente

Necesitás un agente que pueda leer la carpeta y, para ingestas, editar archivos dentro de ella. Configurá primero una conversación que funcione con tu proveedor. La plantilla no incluye una suscripción ni credenciales, y los costos dependen de la herramienta y del modelo elegidos.

### Hermes

Instalá y configurá Hermes siguiendo su [inicio oficial](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart). Abrí tu copia como workspace, o iniciá `hermes` desde esa carpeta en terminal.

Pedile que lea `AGENTS.md` y `00_Index.md` y use el caso ficticio. Para verificar las skills, consultá `hermes skills list` desde la raíz. Las versiones con descubrimiento de skills de proyecto reconocen `.agents/skills/` dentro de un repo Git. Si Hermes indica que ese proyecto necesita confianza, leé antes los tres `SKILL.md` y seguí su flujo `hermes skills trust` para **tu copia**. [Referencia de skills de Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).

Si tu versión requiere directorios externos, agregá esta sección al `config.yaml` local del perfil que estés usando, conservando el resto de su configuración:

```yaml
skills:
  external_dirs:
    - ${ACS_VAULT}/.agents/skills
```

Definí `ACS_VAULT` como la ruta real de tu copia en el entorno que inicia Hermes; también podés reemplazar esa expresión por la ruta local directamente en su configuración. La variable no se define por este repositorio. No subas el config del perfil al vault. Reiniciá la sesión y confirmá que aparecen `acs-ingest`, `acs-query` y `acs-lint`.

Si descargaste un ZIP sin `.git`, no dependas del descubrimiento de proyecto basado en Git: usá el directorio externo o pedile que lea el paquete por su ruta. Editar un archivo de skill cambia las instrucciones que se cargarán; las sesiones ya abiertas pueden conservar la versión anterior.

### Codex

Abrí la raíz de tu copia como proyecto. `AGENTS.md` contiene las instrucciones persistentes del repositorio y `.agents/skills/` los tres paquetes de skills locales. Estas ubicaciones están documentadas por OpenAI en [Customization](https://learn.chatgpt.com/docs/customization/overview) y [Build skills](https://learn.chatgpt.com/docs/build-skills).

Para el primer uso, pegá el prompt de la sección siguiente. Si no aparecen las skills, verificá que estás en la raíz correcta y reiniciá Codex. También podés pedir la lectura explícita del `SKILL.md` por su ruta. Un `.agent.md` de la biblioteca es un rol que se lee cuando se pide; no lanza subagentes.

### Otro asistente

Usá la misma carpeta y pedí lectura explícita de `AGENTS.md`, `00_Index.md` y las notas relevantes. Si la herramienta no tiene acceso al disco, adjuntá solo esos archivos y las fuentes necesarias. Los cambios tendrán que volver a guardarse en tu vault. Comprobá el resultado antes de considerar que la memoria quedó actualizada.

## 4. Probar el recorrido ficticio

Pegá este pedido:

> Leé AGENTS.md y 00_Index.md. Usá únicamente demo-taller. Abrí su índice, su fuente, perfil, oferta y claims. Explicá qué afirmaciones del brief están sustentadas y qué datos siguen pendientes. Citá las rutas. No edites archivos.

Resultado esperado: reconoce turnos, revisión y presupuesto previo; identifica que faltan precios, cobertura, contacto y plazos. No crea una empresa real ni infiere condiciones comerciales. Los enlaces del brief permiten volver a la fuente.

## 5. Dar de alta tu primer cliente o proyecto

Hacé este paso en la copia privada. Duplicá `templates/cliente/` dentro de `02_Clients/` y renombrala, por ejemplo `mi-proyecto`. En macOS/Linux podés usar, desde la raíz y con un destino que todavía no exista:

```bash
cp -R templates/cliente 02_Clients/mi-proyecto
```

En Windows podés hacerlo desde el explorador. Completá el nombre y el índice; incorporá al principio una fuente, perfil, oferta y límites de claims. Dejá los demás archivos como borrador si todavía no hay evidencia. Agregá el enlace al nuevo índice en `02_Clients/README.md` y, si corresponde, en `00_Index.md`.

El caso demo puede quedar como referencia o retirarse. Si lo retirás, ajustá también sus enlaces y las filas de demostración del manifiesto y run log.

## 6. Hacer la primera ingesta

Guardá una fuente que tengas autorización para procesar en `02_Clients/mi-proyecto/sources/`. Usá un nombre con fecha y origen comprensible. Pedí:

> Usá acs-ingest para incorporar la fuente que te indico al proyecto mi-proyecto. Leé antes su índice. Extraé hechos con fuente y fecha; separá hipótesis y pendientes. Actualizá solo las notas necesarias, el índice, el manifiesto y el run log. No inventes datos ni publiques nada. Al terminar, indicá las rutas cambiadas.

Indicá la ruta concreta de la fuente. Revisá los cambios y verificá que cada hecho importante pueda volver al original. Si la fuente no sostiene un dato, dejalo pendiente.

## 7. Usar el conocimiento

Para consultar:

> Usá acs-query para responder sobre mi-proyecto: ¿qué sabemos de su oferta y qué falta validar? Citá las notas que uses. No edites archivos.

Para producir:

> Leé el índice, perfil, oferta y claims de mi-proyecto. Completá un brief usando templates/template.brief.md y guardalo dentro de sus campaigns. Incluí objetivo, restricciones, resultado, fuentes y pendientes. No lo publiques.

Revisá los claims y el formato antes de usar el resultado externamente. Conectar email, Telegram, CRM o analytics es una ampliación posterior y requiere configurar tus propias cuentas y permisos.

## 8. Mantener la memoria

Después de una ingesta importante, ejecutá desde la raíz:

```bash
python3 05_Operations/scripts/check_vault.py
```

No instala paquetes ni usa red. Chequea enlaces locales e imports, frontmatter básico, estructura mínima de clientes, trazabilidad y señales habituales de archivos sensibles. Leé además las notas afectadas para comprobar vigencia, evidencia y aislamiento. Podés pedir esa revisión con `acs-lint`.

El chequeo no interpreta la verdad de las afirmaciones ni detecta todos los datos privados. Un repositorio privado también requiere elegir quién accede. Antes de cualquier publicación, revisá los archivos y todos los commits que vas a compartir.

## Si algo no funciona

| Síntoma | Qué comprobar |
|---|---|
| El agente responde con datos genéricos | Que haya leído el índice y las fuentes; pedir rutas utilizadas |
| Mezcla dos clientes | Reiniciar con alcance explícito y leer solo el cliente elegido |
| Una skill no aparece | Carpeta raíz, formato SKILL.md, soporte/trust del agente y nueva sesión |
| Obsidian abre una carpeta vacía | Seleccionar la raíz descomprimida que contiene 00_Index.md |
| El verificador marca un enlace roto | Corregir ruta o actualizar índice después de renombrar |
| Se editó una fuente original | Revisar sus notas derivadas en el manifiesto |

## Qué podés sumar después

Una vez que el flujo básico sea útil, podés agregar skills específicas, roles, conectores o búsqueda semántica. Empezá por una necesidad real y verificá la versión y documentación de cada herramienta. Esta edición deja esas integraciones sin configurar para que cada implementación use sus propias cuentas.

Referencias de herramientas verificadas para esta guía el 2026-10-23. El recorrido estructural se prueba con el caso ficticio; la conexión a tu proveedor se verifica en tu entorno.
