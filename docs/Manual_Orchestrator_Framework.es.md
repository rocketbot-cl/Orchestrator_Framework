



# Orchestrator Framework
  
Este módulo permite trabajar con tareas y transacciones, imprimir logs a la consola, enviar alertas por correo electrónico o enviar una señal para detener el framework.  

*Read this in other languages: [English](Manual_Orchestrator_Framework.md), [Português](Manual_Orchestrator_Framework.pr.md), [Español](Manual_Orchestrator_Framework.es.md)*
  
![banner](imgs/Banner_Orchestrator_Framework.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Login NOC
  
Inicie sesión en NOC utilizando unda de las opciones, API Key, archivo noc.ini o credenciales.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL Servidor|URL del servidor a donde se conecta|https://roc.myrb.io/|
|API KEY|User APIKey|eyJ0eXAiOiJKV2QiLCJhbGciOiJIUzI1MiJ9.eyJpc3MiOiJudHRwczpcL1wvZGV2My5teXJiLmlwXC9hcGlcL3VzZXJzXC9hcGlrZXlcL2dlbmVyYXRlIiwiaWF0IjoxNjg5MDI0NDI2LCJleHAiOjE3NTIwOTY0MjYsIm5iZiI6MTY4OTAyNDQyNiwianRpIjoiSUxQQWRoY3F3NkM1RmllUCIsInN1YiI6MzIsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEiLCJub2MiOm51bGx9.HZ4oFuOXL_VBlqAHyWkgJQr29bbBLSBnmcx6ij27zaI|
|Asignar a variable|Variable donde guardar resultado sin {}|var|

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
|Tiene Encabezados|If checked, it will take the first list as the transaction title.|True|
|Asignar resultado a Variable|Variable donde guardar|Variable|

### Agregar multiples Transacciones
  
Agrega nuevas transacción
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transacciones|Transacciones a enviar. La entrada debe ser una lista de listas, siendo los encabezados el primer valor de la lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3],[4, 5, 6],[7, 8, 9]]|
|Tiene Encabezados|If checked, it will take the first list as the transactions titles.|True|
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

### Detener Framework
  
Enviar orden para detener el framework
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|ID de la instancia del proceso a detener|a2f64d5d9988c|
|Process Token|Token del proceso a detener|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable donde guardar|Variable|

### ¿Debe detenerse el Framework?
  
Verifica si el framework debe detenerse
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Instancia del proceso|Variable donde debe ingresarse la instancia del proceso|a2f64d5d9988c|
|Process Token|Variable donde debe ingresarse el token del proceso a revisar si debe detenerse o no|LGPS8DYPJCAVECEF|
|Asignar resultado a Variable|Variable donde guardar|Variable|
