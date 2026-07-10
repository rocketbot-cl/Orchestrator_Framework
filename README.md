



# Orchestrator Framework
  
Manages NOC processes, tasks, transactions, and Assets, and also sends alerts, writes logs, and controls framework shutdown.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Login NOC  
Authenticates with NOC and opens a session required by all other commands in this module. Supports API Key, e-mail and password, or a noc.ini file.

2. Get Processes  
Get all processes

3. Get Tasks  
Get task

4. Create Task  
Adds a new task

5. Set Priority  
Set the priority of a task

6. Add Transaction  
Add one new transaction

7. Add multiple Transactions  
Add new transactions

8. Get unprocessed transactions  
Get every unprocessed transactions from a task

9. Set status  
Change the status of a transaction

10. Send alert  
Send an alert message to the emails set into the Orchestrator Process

11. Send custom log  
Send custom log

12. Stop Framework  
Sends NOC a stop request for a specific process instance. This command sets the stop state; it must not be confused with Should Stop Framework?, which only reads that state.

13. Should Stop Framework?  
Checks NOC for a pending stop request on a process instance. It does not change the state: it returns True when the instance must stop and False when it may continue.

14. Get a Specific Asset  
Gets an Asset by name. Only resolves assets with global scope (All); assets tied to a specific process return no data — use Get All Assets in that case. Returns the value, or a full dictionary with extra data enabled.

15. Get All Assets  
Gets every Asset available to the authenticated user. Basic mode returns name and value and creates one Rocketbot variable per Asset; extra-data mode returns a list of complete metadata.

16. Add Asset  
Creates a text, password, or encrypted Asset. Its scope is global without a process, process-level with only a token, or instance-level when an instance key is also supplied. It may optionally be associated with NOC users.

17. Modify Asset  
Updates an existing Asset by ID. The command sends the complete final Asset state: name, type, value, scope, and users. Leaving process and instance empty changes its scope to global.  




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