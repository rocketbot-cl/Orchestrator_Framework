



# Orchestrator Framework

Permite administrar procesos, tareas, transacciones y Assets de NOC, además de enviar alertas, registrar logs y controlar la detención del framework.

*Read this in other languages: [English](Manual_Orchestrator_Framework.md), [Português](Manual_Orchestrator_Framework.pr.md), [Español](Manual_Orchestrator_Framework.es.md)*

![banner](imgs/Banner_Orchestrator_Framework.jpg)
## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.


## Descripción de los comandos

### Login NOC

Inicie sesión en NOC utilizando una de las opciones, API Key, archivo noc.ini o credenciales.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL Servidor|URL del servidor a donde se conecta|https://roc.myrb.io/|
||||
|Ignorar SSL|Desactiva la validación del certificado SSL durante la autenticación y las solicitudes de Assets.||
|Asignar a variable|Variable que recibe True cuando la conexión se establece correctamente y False cuando falla.|var|

### Obtener procesos

Obtener todos los procesos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Obtener Tareas

Obtener tareas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Crear Tarea

Agrega una nueva tarea
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Variable donde guardar la key de la nueva tarea, sin {}|key|
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Establecer Prioridad

Establecer la prioridad de una tarea
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Prioridad|Prioridad de la tarea||
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Agregar Transacción

Agrega una nueva transacción
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transacción|Transacción a enviar. La entrada debe ser una lista de listas, siendo los encabezados el primer valor de la lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3]]|
|Tiene Encabezados|Si está marcado, tomará la primera lista como los títulos de la transacción.|True|
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Agregar multiples Transacciones

Agrega nuevas transacción
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transacciones|Transacciones a enviar. La entrada debe ser una lista de listas, siendo los encabezados el primer valor de la lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3],[4, 5, 6],[7, 8, 9]]|
|Tiene Encabezados|Si está marcado, tomará la primera lista como los títulos de las transacciones.|True|
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Obtener transacciones sin procesar

Obtenga todas las transacciones no procesadas de una tarea
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Establecer estado

Cambiar el estado de una transacción
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transaction ID|Transaction ID||
|Estado|Seleccione el estado de la transaccion||
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Enviar alerta

Envia un mensaje de alerta a los correos electrónicos configurados en el proceso de orquestador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable donde guardar|Variable|
|Mensaje|Mensaje que se enviara al correo definido en el alerta del proceso||

### Enviar log personalizado

Enviar log personalizado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|Variable donde debe ingresarse la instancia del proceso|a2f64d5d9988c|
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Mensaje|Mensaje que se enviara al correo definido en el alerta del proceso||
|Tipo|Seleccionar el tipo de log a enviar.|info|

### Detener Framework

Enviar orden para detener el framework
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|ID de la instancia del proceso a detener|a2f64d5d9988c|
|Process Token|Token del proceso a detener|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable donde guardar el resultado|Variable|

### ¿Debe detenerse el Framework?

Verifica si el framework debe detenerse
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|Variable donde debe ingresarse la instancia del proceso|a2f64d5d9988c|
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable donde guardar el resultado|Variable|

### Obtener Asset Específico

Obtiene el asset especifico que se le indique
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Asset|Nombre del asset a obtener|Test|
|Token del proceso|Token del proceso. Si se especifica, hay que tambien especificar la key de instancia.|27FEXKIXFRFDUNVD|
|Key de Instancia|Key de instancia del proceso|6241c3a1dd96f8f92f|
|Obtener datos adicionales|Marca para obtener datos extra de los Assets|True|
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|

### Obtener Todos los Assets

Obtiene todos los Assets y los asigna a la variable correspondiente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|
|Obtener datos adicionales|Marca para obtener datos extra de los Assets|True|

### Agregar Asset

Agrega un Asset a tu Orquestador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Asset|Nombre del Asset a agregar|NuevoAsset|
|Token del proceso|Token del proceso al que se le agregara el Asset|27FEXKIXFRFDUNVD|
|Key de Instancia|Key de la instancia al que se le agregara el Asset|6241c3a1dd96f8f92f|
|Mail de usuarios|Lista de mails de usuarios a los que se agregará el Asset. Dejar en blanco si es un Asset para todos los usuarios|[usuario1@mail.com, usuario2@mail.com, ...]|
|Tipo del Asset|Tipo del Asset a agregar|General|
|Valor del Asset|Valor del Asset a agregar|Un valor|
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|

### Modificar Asset

Modifica el asset especifico que se le indique
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del Asset|Id del Asset a modificar|Id_Asset|
|Nuevo nombre de Asset|Nuevo nombre del Asset. Déjelo vacío para conservar el nombre actual.Si existe otro Asset con el mismo nombre, no se podra modificar el asset|NuevoAsset|
|Nuevo token del proceso|Token del proceso que tendrá el Asset|27FEXKIXFRFDUNVD|
|Nueva key de la instancia|Key de la instancia que tendrá el Asset|6241c3a1dd96f8f92f|
|Nuevos mails de usuarios|Lista de Mails de usuarios que tendrán el Asset. Usar [] si es un Asset de todos los usuarios.|[usuario1@mail.com, usuario2@mail.com, ...]|
|Nuevo tipo del Asset|Nuevo tipo del Asset a modificar|General|
|Nuevo valor del Asset|Nuevo valor del Asset a modificar|Un valor|
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|

### Eliminar Asset

Elimina un Asset existente mediante su ID.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del Asset|ID del Asset que se desea eliminar.|Id_Asset|
|Asignar a variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|
