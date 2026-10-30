



# Orchestrator Framework

Permite administrar procesos, tareas, transacciones y Assets de NOC, además de enviar alertas, registrar logs y controlar la detención del framework.

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.


## Overview


1. Login NOC
Inicie sesión en NOC utilizando una de las opciones, API Key, archivo noc.ini o credenciales.

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
Enviar orden para detener el framework

13. ¿Debe detenerse el Framework?
Verifica si el framework debe detenerse

14. Obtener Asset Específico
Obtiene el asset especifico que se le indique

15. Obtener Todos los Assets
Obtiene todos los Assets y los asigna a la variable correspondiente

16. Agregar Asset
Agrega un Asset a tu Orquestador

17. Modificar Asset
Modifica el asset especifico que se le indique

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