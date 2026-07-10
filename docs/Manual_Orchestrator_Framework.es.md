



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
  
Autentica con NOC y abre una sesión requerida por todos los demás comandos del módulo. Soporta API Key, e-mail y contraseña, o un archivo noc.ini.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL Servidor|URL base del servidor NOC. Es obligatoria salvo que esté definida dentro del archivo noc.ini.|https://roc.myrb.io/|
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
  
Envía a NOC una solicitud de detención para una instancia concreta del proceso. Este comando establece el estado de detención; no debe confundirse con ¿Debe detenerse el Framework?, que solamente consulta ese estado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|Key de la instancia del proceso que debe detenerse.|a2f64d5d9988c|
|Process Token|Token del proceso cuya instancia recibirá la solicitud de detención.|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable que recibe True cuando NOC registra correctamente la solicitud y False cuando la operación falla.|Variable|

### ¿Debe detenerse el Framework?
  
Consulta en NOC si una instancia del proceso tiene una solicitud de detención pendiente. No cambia el estado: devuelve True cuando la instancia debe detenerse y False cuando puede continuar.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|Key de la instancia cuyo estado de detención se desea consultar.|a2f64d5d9988c|
|Process Token|Token del proceso al que pertenece la instancia.|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable booleana True indica que el Framework debe detenerse; False indica que puede continuar.|Variable|

### Obtener Asset Específico
  
Obtiene un Asset por nombre. Solo resuelve assets con scope global (All); los assets asociados a un proceso específico no devuelven datos — usar Obtener Todos los Assets en ese caso. Devuelve el valor, o un diccionario completo si se activan los datos adicionales.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Asset|Nombre exacto del Asset que se desea consultar.|Test|
|Token del proceso|Token del proceso propietario del Asset. Déjelo vacío para consultar un Asset global.|27FEXKIXFRFDUNVD|
|Key de Instancia|Key de la instancia propietaria del Asset. Requiere un token de proceso; si el login utiliza noc.ini y queda vacío, se usa la key configurada en ese archivo.|6241c3a1dd96f8f92f|
|Obtener datos adicionales|Si está marcado, devuelve todos los metadatos del Asset; si no, devuelve solamente su valor.|True|
|Asignar resultado a Variable|Variable donde se guarda el valor del Asset o el diccionario de metadatos, según la opción seleccionada.|Variable|

### Obtener Todos los Assets
  
Obtiene todos los Assets accesibles para el usuario autenticado. En modo básico devuelve nombre y valor y crea una variable Rocketbot por cada Asset; con datos adicionales devuelve una lista de metadatos completos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a Variable|Variable donde se guarda la lista resultante.|Variable|
|Obtener datos adicionales|Si está marcado, cada elemento incluye ID, tipo, valor, token de proceso, key de instancia y usuarios. Si no, devuelve name/value y también crea variables con el nombre de cada Asset.|True|

### Agregar Asset
  
Crea un Asset de tipo texto, contraseña o cifrado. Su alcance será global si no se indica proceso, de proceso si se indica solo el token, o de instancia si también se indica la key. Opcionalmente puede asociarse a usuarios de NOC.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Asset|Nombre del nuevo Asset. Debe respetar las reglas de unicidad configuradas en NOC.|NuevoAsset|
|Token del proceso|Token del proceso al que pertenecerá el Asset. Si queda vacío, se crea un Asset global.|27FEXKIXFRFDUNVD|
|Key de Instancia|Key de la instancia a la que pertenecerá el Asset. Solo es válida cuando también se informa el token del proceso.|6241c3a1dd96f8f92f|
|Mail de usuarios|Lista de e-mails de usuarios de NOC que tendrán acceso al Asset.|[usuario1@mail.com, usuario2@mail.com, ...]|
|Tipo del Asset|Tipo de almacenamiento del Asset text para texto general, password para contraseñas o encrypted para contenido cifrado.|General|
|Valor del Asset|Valor que se almacenará en el Asset.|Un valor|
|Asignar resultado a Variable|Variable donde se guarda la respuesta completa devuelta por la API de NOC.|Variable|

### Modificar Asset
  
Actualiza un Asset existente mediante su ID. El comando envía el estado final completo del Asset: nombre, tipo, valor, alcance y usuarios. Dejar proceso e instancia vacíos convierte su alcance en global.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del Asset|ID del Asset que se desea modificar. Puede obtenerse con Obtener Asset Específico activando datos adicionales.|Id_Asset|
|Nuevo nombre de Asset|Nombre final que tendrá el Asset después de la modificación.|NuevoAsset|
|Nuevo token del proceso|Token final del proceso propietario. Déjelo vacío, junto con la instancia, para convertir el Asset en global.|27FEXKIXFRFDUNVD|
|Nueva key de la instancia|Key final de la instancia propietaria. Requiere el token del proceso.|6241c3a1dd96f8f92f|
|Nuevos mails de usuarios|Lista final de e-mails de usuarios asociados. Reemplaza la asociación anterior.|[MailUsuario1, MailUsuario2, ...]|
|Nuevo tipo del Asset|Tipo final del Asset text, password o encrypted.|General|
|Nuevo valor del Asset|Valor final que se almacenará en el Asset.|Un valor|
|Asignar resultado a Variable|Variable donde se guarda la respuesta completa devuelta por la API de NOC.|Variable|
