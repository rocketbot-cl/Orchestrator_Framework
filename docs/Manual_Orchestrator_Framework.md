



# Orchestrator Framework

Manages NOC processes, tasks, transactions, and Assets, and also sends alerts, writes logs, and controls framework shutdown.

*Read this in other languages: [English](Manual_Orchestrator_Framework.md), [Português](Manual_Orchestrator_Framework.pr.md), [Español](Manual_Orchestrator_Framework.es.md)*

![banner](imgs/Banner_Orchestrator_Framework.jpg)
## How to install this module

To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.


## Description of the commands

### Login NOC

Login to NOC using one of the options, API Key, noc.ini file, or credentials.
|Parameters|Description|example|
| --- | --- | --- |
|URL Server|Server URL|https://roc.myrb.io/|
||||
|Ignore SSL|Disables SSL certificate validation during authentication and Asset requests.||
|Set to var|Variable that receives True when the connection succeeds and False when it fails.|var|

### Get Processes

Get all processes
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a Variable|Variable to store result|Variable|

### Get Tasks

Get task
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Assign result to a Variable|Variable to store result|Variable|

### Create Task

Adds a new task
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Task Key|Variable to store new Task key, without {}|key|
|Assign result to a Variable|Variable to store result|Variable|

### Set Priority

Set the priority of a task
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Priority|Priority for the task||
|Assign result to a Variable|Variable to store result|Variable|

### Add Transaction

Add one new transaction
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transaction|Transaction to send. The input must be a list of lists, being the headers the first value of the main list.|[['Header1', 'Header2', 'Header3'],[1, 2, 3]]|
|Has Headers|If checked, it will take the first list as the transaction title.|True|
|Assign result to a Variable|Variable to store result|Variable|

### Add multiple Transactions

Add new transactions
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transactions|Transactions to send. The input must be a list of lists, being the headers the first value of the main list.|[['Header1', 'Header2', 'Header3'],[1, 2, 3],[4, 5, 6],[7, 8, 9]]|
|Has Headers|If checked, it will take the first list as the transactions titles.|True|
|Assign result to a Variable|Variable to store result|Variable|

### Get unprocessed transactions

Get every unprocessed transactions from a task
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Assign result to a Variable|Variable to store result|Variable|

### Set status

Change the status of a transaction
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transaction ID|Transaction ID||
|Status|Select the status of the transaction||
|Assign result to a Variable|Variable to store result|Variable|

### Send alert

Send an alert message to the emails set into the Orchestrator Process
|Parameters|Description|example|
| --- | --- | --- |
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Assign result to a Variable|Variable to store result|Variable|
|Message|Message to be sent to the email defined in the process alert||

### Send custom log

Send custom log
|Parameters|Description|example|
| --- | --- | --- |
|Process instance|Variable where the process instance must be entered|a2f64d5d9988c|
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Message|Message to be sent to the email defined in the process alert||
|Type|Select the type of log to send.|info|

### Stop Framework

Send order to stop the framework
|Parameters|Description|example|
| --- | --- | --- |
|Process instance|ID of the process instance to stop|a2f64d5d9988c|
|Process Token|Token of the process to stop|LGPS8DYPJCAVECEF|
|Assign result to a Variable|Variable to store result|Variable|

### Should Stop Framework?

Check if the framework should stop
|Parameters|Description|example|
| --- | --- | --- |
|Process instance|Variable where the process instance must be entered|a2f64d5d9988c|
|Process Token|Variable where the token of the process to be checked if it should stop or not must be entered|LGPS8DYPJCAVECEF|
|Assign result to a Variable|Variable to store result|Variable|

### Get a Specific Asset

Obtains the specific asset that is indicated
|Parameters|Description|example|
| --- | --- | --- |
|Asset Name|Name of the asset to get|Test|
|Process token|Process token. If specified, you also need to specify the instance key.|27FEXKIXFRFDUNVD|
|Instance Key|Instance key of the process|6241c3a1dd96f8f92f|
|Obtain extra data|Check to obtain extra data from the Assets|True|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

### Get All Assets

Get all the Assets and assign them to the corresponding variable
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|
|Obtain extra data|Check to obtain extra data from the Assets|True|

### Add Asset

Add an Asset to your Orchestrator
|Parameters|Description|example|
| --- | --- | --- |
|Asset Name|Name of the Asset to add|NewAsset|
|Process token|Process Token to which the Asset will be added|27FEXKIXFRFDUNVD|
|Instance Key|Instance Key to which the Asset will be added|6241c3a1dd96f8f92f|
|User mails|List of user emails to add to the Asset. Leave blank if it is an Asset for all users.|[usuario1@mail.com, usuario2@mail.com, ...]|
|Asset type|Type of the Asset to add|General|
|Asset Value|Value of the Asset to add|A value|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

### Modify Asset

Modifies the specific asset that is indicated
|Parameters|Description|example|
| --- | --- | --- |
|Asset Id|Id of the Asset to modify|Id_Asset|
|New Asset Name|New Asset name. Leave empty to keep the current name. If there is another Asset with the same name, the asset cannot be modified|NewAsset|
|New process token|Token of the process that the Asset will have|27FEXKIXFRFDUNVD|
|New instance Key|Instance Key that the Asset will have|6241c3a1dd96f8f92f|
|New User Mails|List of user Mails who will have the Asset. Use [] if it is an Asset for all users.|[usuario1@mail.com, usuario2@mail.com, ...]|
|New Asset type|New type of the Asset to modify|General|
|New Asset Value|New value of the Asset to modify|A value|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

### Delete Asset

Deletes an existing Asset by ID.
|Parameters|Description|example|
| --- | --- | --- |
|Asset Id|ID of the Asset to delete.|Id_Asset|
|Set to var|Variable where the result will be saved. Name of variable without {}|Variable|
