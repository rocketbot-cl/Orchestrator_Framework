



# Orchestrator Framework

Permite administrar processos, tarefas, transações e Assets do NOC, além de enviar alertas, registrar logs e controlar a parada do framework.

*Read this in other languages: [English](Manual_Orchestrator_Framework.md), [Português](Manual_Orchestrator_Framework.pr.md), [Español](Manual_Orchestrator_Framework.es.md)*

![banner](imgs/Banner_Orchestrator_Framework.jpg)
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
||||
|Ignorar SSL|Desativa a validação do certificado SSL durante a autenticação e as solicitações de Assets.||
|Definir como variável|Variável que recebe True quando a conexão é estabelecida e False quando falha.|var|

### Obter processos

Obter todos os processos
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Variável para guardar|Variable|

### Obter Tarefas

Obter tarefas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável para guardar|Variable|

### Criar Tarefa

Adiciona uma nova tarefa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Variável para guardar a key da nova tarefa, sem {}|key|
|Atribuir resultado à variável|Variável para guardar|Variable|

### Estabelecer Prioridade

Estabelecer a prioridade de uma tarefa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Prioridade|Prioridade da tarefa||
|Atribuir resultado à variável|Variável para guardar|Variable|

### Adicionar Transação

Adicionar uma nova transação
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transação|Transação a enviar. A entrada deve ser uma lista de listas, sendo os cabeçalhos o primeiro valor da lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3]]|
|Tem Cabeçalhos|Se marcada, levará a primeira lista como o título da transação..|True|
|Atribuir resultado à variável|Variável para guardar|Variable|

### Adicionar várias Transações

Adicionar novas transações
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transações|Transações a enviar. A entrada deve ser uma lista de listas, sendo os cabeçalhos o primeiro valor da lista principal.|[['Header1', 'Header2', 'Header3'],[1, 2, 3],[4, 5, 6],[7, 8, 9]]|
|Tem Cabeçalhos|Se marcada, levará a primeira lista como os títulos das transações.|True|
|Atribuir resultado à variável|Variável para guardar|Variable|

### Obter transações não processadas

Obter todas as transações não processadas de uma tarefa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Atribuir resultado à variável|Variável para guardar|Variable|

### Definir estado

Alterar o estado de uma transação
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Task Key|Task Key||
|Transaction ID|Transaction ID||
|Estado|Selecione o estado da transação||
|Atribuir resultado à variável|Variável para guardar|Variable|

### Enviar alerta

Envie uma mensagem de alerta para os e-mails definidos no processo do orquestrador
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável para guardar|Variable|
|Mensagem|Mensagem a enviar para o email definido no alerta do processo||

### Enviar log personalizado

Enviar log personalizado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|Variável onde a instância do processo deve ser inserida|a2f64d5d9988c|
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Mensagem|Mensagem a enviar para o email definido no alerta do processo||
|Tipo|Selecione o tipo de log a enviar.|info|

### Parar Framework?

Enviar ordem para parar o framework
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|ID da instância do processo a ser parada|a2f64d5d9988c|
|Process Token|Token do processo a ser parado|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável para guardar o resultado|Variable|

### Deve parar o Framework?

Verifique se o framework deve parar
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|Variável onde a instância do processo deve ser inserida|a2f64d5d9988c|
|Process Token|Variável onde o token do processo a ser verificado se deve parar ou não deve ser inserido|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável para guardar o resultado|Variable|

### Obter Asset específico

Obtém o ativo específico indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Asset|Nome do asset a ser obtido|Teste|
|Token do processo|Token do processo. Se especificado, você também precisa especificar a chave da instância.|27FEXKIXFRFDUNVD|
|Key de Instância|Key de instância do processo|6241c3a1dd96f8f92f|
|Obter dados extras|Marque para obter dados extras dos Assets|True|
|Atribuir resultado a variável|Variável onde o resultado será salvo. Nome da variável sem chaves {}|Variável|

### Obter todos os Assets

Obtém todos os Assets e os atribui a variável correspondente
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribua resultado à Variável|Variável onde o resultado será salvo. Nome da variável sem chaves {}|Variável|
|Obter dados extras|Marque para obter dados extras dos Assets|True|

### Adicionar Asset

Adiciona um Asset ao seu Orquestrador
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Asset|Nome do Asset a ser adicionado|NovoAsset|
|Token do processo|Token do processo ao qual o Asset será adicionado|27FEXKIXFRFDUNVD|
|Key de Instância|Key da instância ao qual o Asset será adicionado|6241c3a1dd96f8f92f|
|Mails dos usuários|Lista de e-mails de usuários aos quais o Asset será adicionado. Deixar em branco se for um Asset para todos os usuários.|[usuario1@mail.com, usuario2@mail.com, ...]|
|Tipo do Asset|Tipo do Asset a ser adicionado|Geral|
|Valor do Asset|Valor do Asset a ser adicionado|Um valor|
|Atribuir resultado a variável|Variável onde o resultado será salvo. Nome da variável sem chaves {}|Variável|

### Modifica o ativo específico

Modifica o ativo específico indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do Asset|Id do Asset a ser modificado|Id_Asset|
|Novo nome do Asset|Novo nome do Asset. Deixe vazio para manter o nome atual. Se existir outro Asset com o mesmo nome, o asset não poderá ser modificado.|NovoAsset|
|Novo token do processo|Token do processo que o Asset terá|27FEXKIXFRFDUNVD|
|Nova key da instância|Key da instância que o Asset terá|6241c3a1dd96f8f92f|
|Novos mails dos usuários|Lista de Mails dos usuários que terão o Asset. Usar [] se for um Asset para todos os usuários.|[usuario1@mail.com, usuario2@mail.com, ...]|
|Novo tipo do Asset|Novo tipo do Asset a ser modificado|Geral|
|Novo valor do Asset|Novo valor do Asset a ser modificado|Um valor|
|Atribuir resultado a variável|Variável onde o resultado será salvo. Nome da variável sem chaves {}|Variável|

### Excluir Asset

Exclui um Asset existente pelo ID.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do Asset|ID do Asset que será excluído.|Id_Asset|
|Definir como variável|Variável onde o resultado será salvo. Nome da variável sem chaves {}|Variável|
