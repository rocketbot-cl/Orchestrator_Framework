



# Orchestrator Framework

Permite administrar procesos, tareas, transacciones y Assets de NOC, además de enviar alertas, registrar logs y controlar la detención del framework.

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.


## Overview


1. Login NOC
Autentica con NOC y abre una sesión requerida por todos los demás comandos del módulo. Soporta API Key, e-mail y contraseña, o un archivo noc.ini.

2. Obtener procesos
Obtener todos los procesos

3. Obtener Tareas
Obtener tareas

4. Crear Tarea
Agrega una nueva tarea

5. Establecer Prioridad
Establecer la prioridad de una tarea

6. Agregar Transacción
Agrega una nueva transacción

7. Agregar multiples Transacciones
Agrega nuevas transacción

8. Obtener transacciones sin procesar
Obtenga todas las transacciones no procesadas de una tarea

9. Establecer estado
Cambiar el estado de una transacción

10. Enviar alerta
Envia un mensaje de alerta a los correos electrónicos configurados en el proceso de orquestador

11. Enviar log personalizado
Enviar log personalizado

12. Detener Framework
Envía a NOC una solicitud de detención para una instancia concreta del proceso. Este comando establece el estado de detención; no debe confundirse con ¿Debe detenerse el Framework?, que solamente consulta ese estado.

13. ¿Debe detenerse el Framework?
Consulta en NOC si una instancia del proceso tiene una solicitud de detención pendiente. No cambia el estado: devuelve True cuando la instancia debe detenerse y False cuando puede continuar.

14. Obtener Asset Específico
Obtiene un Asset por nombre. Para Assets de proceso o instancia, indique el token del proceso y opcionalmente la key de instancia. Devuelve el valor, o un diccionario completo si se activan los datos adicionales.

15. Obtener Todos los Assets
Obtiene todos los Assets accesibles para el usuario autenticado. En modo básico devuelve nombre y valor y crea una variable Rocketbot por cada Asset; con datos adicionales devuelve una lista de metadatos completos.

16. Agregar Asset
Crea un Asset de tipo texto, contraseña o cifrado. Su alcance será global si no se indica proceso, de proceso si se indica solo el token, o de instancia si también se indica la key. Opcionalmente puede asociarse a usuarios de NOC.

17. Modificar Asset
Actualiza un Asset existente mediante su ID. Los campos vacíos conservan los datos actuales del Asset; solo se modifican los campos informados.

18. Eliminar Asset
Elimina un Asset existente mediante su ID.




----
### OS

- windows
- mac
- linux
- docker

### Dependencies

### License

![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)
[MIT](http://opensource.org/licenses/mit-license.ph)