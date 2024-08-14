



# Rocketbot Framework
  
Este módulo permite trabalhar com tarefas e transações, imprimir logs no console, enviar alertas por e-mail ou enviar um sinal para parar o framework.  

*Read this in other languages: [English](Manual_Rocketbot_Framework.md), [Português](Manual_Rocketbot_Framework.pr.md), [Español](Manual_Rocketbot_Framework.es.md)*
  
![banner](imgs/Banner_Rocketbot_Framework.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Login NOC
  
Faça login no NOC usando uma das opções, arquivo noc.ini, API Key ou credenciais.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL Servidor|URL do servidor para se conectar|https://roc.myrb.io/|
|API KEY|User APIKey|eyJ0eXAiOiJKV2QiLCJhbGciOiJIUzI1MiJ9.eyJpc3MiOiJudHRwczpcL1wvZGV2My5teXJiLmlwXC9hcGlcL3VzZXJzXC9hcGlrZXlcL2dlbmVyYXRlIiwiaWF0IjoxNjg5MDI0NDI2LCJleHAiOjE3NTIwOTY0MjYsIm5iZiI6MTY4OTAyNDQyNiwianRpIjoiSUxQQWRoY3F3NkM1RmllUCIsInN1YiI6MzIsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEiLCJub2MiOm51bGx9.HZ4oFuOXL_VBlqAHyWkgJQr29bbBLSBnmcx6ij27zaI|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Obter Tarefas
  
Obter tarefas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Definir como variável|Variável para guardar resultado sem {}|var|
|Obter key|Variável para armazenar a chave da nova tarefa|new_key|

### Criar Tarefa
  
Adiciona uma nova tarefa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Adicionar Transação
  
Adicionar uma nova transação
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transação|Transação a enviar. A entrada deve ser uma lista de listas, sendo os cabeçalhos o primeiro valor da lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3]]|
|Tem Cabeçalhos|Se marcada, levará a primeira lista como o título da transação..|True|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Adicionar várias Transações
  
Adicionar novas transações
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transações|Transações a enviar. A entrada deve ser uma lista de listas, sendo os cabeçalhos o primeiro valor da lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3],[4, 5, 6],[7, 8, 9]]|
|Tem Cabeçalhos|Se marcada, levará a primeira lista como os títulos das transações.|True|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Obter transações não processadas
  
Obter todas as transações não processadas de uma tarefa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Definir como variável|Variável para guardar resultado sem {}|var|

### Definir estado
  
Alterar o estado de uma transação
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transaction ID|Transaction ID||
|Estado|Selecione o estado da transação||
|Definir como variável|Variável para guardar resultado sem {}|var|

### Enviar alerta
  
Envie uma mensagem de alerta para os e-mails definidos no processo do orquestrador
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Definir como variável|Variável para guardar resultado sem {}|var|
|Mensagem|Mensagem a enviar para o email definido no alerta do processo||

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|Variável onde a instância do processo deve ser inserida|a2f64d5d9988c|
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Mensagem|Mensagem a enviar para o email definido no alerta do processo||

### Deve parar?
  
Verifique se o framework deve parar
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|Variável onde a instância do processo deve ser inserida|a2f64d5d9988c|
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável onde True ou False será armazenado dependendo se deve parar ou não|Variable|
