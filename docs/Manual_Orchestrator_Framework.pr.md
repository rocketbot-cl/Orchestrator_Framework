



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

Autentica com o NOC e abre uma sessão exigida por todos os outros comandos do módulo. Suporta API Key, e-mail e senha, ou um arquivo noc.ini.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL Servidor|URL base do servidor NOC. Obrigatória, exceto quando definida no arquivo noc.ini.|https://roc.myrb.io/|
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

### Parar Framework

Envia ao NOC uma solicitação de parada para uma instância específica do processo. Este comando define o estado de parada; não deve ser confundido com Deve parar o Framework?, que apenas consulta esse estado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|Key da instância do processo que deve parar.|a2f64d5d9988c|
|Process Token|Token do processo cuja instância receberá a solicitação de parada.|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável que recebe True quando o NOC registra a solicitação e False quando a operação falha.|Variable|

### Deve parar o Framework?

Consulta no NOC se uma instância do processo possui uma solicitação de parada pendente. Não altera o estado: retorna True quando a instância deve parar e False quando pode continuar.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Instância do processo|Key da instância cujo estado de parada será consultado.|a2f64d5d9988c|
|Process Token|Token do processo proprietário da instância.|LGPS8DYPJCAVECEF|
|Atribuir resultado à variável|Variável booleana True indica que o Framework deve parar; False indica que pode continuar.|Variable|

### Obter Asset específico

Obtém um Asset pelo nome. Para Assets de processo ou instância, informe o token do processo e opcionalmente a key da instância. Retorna o valor, ou um dicionário completo com os dados adicionais habilitados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Asset|Nome exato do Asset que será consultado.|Teste|
|Token do processo|Token do processo proprietário do Asset. Deixe vazio para um Asset global.|27FEXKIXFRFDUNVD|
|Key de Instância|Key da instância proprietária do Asset. Requer um token de processo; quando o login usa noc.ini e o campo fica vazio, é usada a key desse arquivo.|6241c3a1dd96f8f92f|
|Obter dados extras|Quando marcado, retorna todos os metadados do Asset; caso contrário, retorna somente o valor.|True|
|Atribuir resultado a variável|Variável que armazena o valor do Asset ou o dicionário de metadados, conforme a opção selecionada.|Variável|

### Obter todos os Assets

Obtém todos os Assets disponíveis para o usuário autenticado. No modo básico retorna nome e valor e cria uma variável Rocketbot por Asset; com dados adicionais retorna uma lista de metadados completos.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribua resultado à Variável|Variável que armazena a lista resultante.|Variável|
|Obter dados extras|Quando marcado, cada item inclui ID, tipo, valor, token do processo, key da instância e usuários. Caso contrário, retorna name/value e também cria variáveis com o nome de cada Asset.|True|

### Adicionar Asset

Cria um Asset de texto, senha ou criptografado. O escopo será global sem processo, de processo somente com o token ou de instância quando também for informada a key. Opcionalmente pode ser associado a usuários do NOC.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Asset|Nome do novo Asset. Deve respeitar as regras de unicidade configuradas no NOC.|NovoAsset|
|Token do processo|Token do processo proprietário do Asset. Quando vazio, é criado um Asset global.|27FEXKIXFRFDUNVD|
|Key de Instância|Key da instância proprietária do Asset. Válida somente quando também é informado o token do processo.|6241c3a1dd96f8f92f|
|Mails dos usuários|Lista de e-mails de usuários do NOC que terão acesso ao Asset. Escreva sem aspas, entre colchetes e separados por vírgula.|[usuario1@empresa.com, usuario2@empresa.com]|
|Tipo do Asset|Tipo de armazenamento do Asset text para texto geral, password para senhas ou encrypted para conteúdo criptografado.|Geral|
|Valor do Asset|Valor que será armazenado no Asset.|Um valor|
|Atribuir resultado a variável|Variavel que recebe True se o Asset foi criado com sucesso.|Variável|

### Modificar Asset

Atualiza um Asset existente pelo ID. Campos vazios mantêm os dados atuais do Asset; somente os campos informados são alterados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do Asset|ID do Asset que será modificado. Pode ser obtido com Obter Asset específico ativando os dados adicionais.|Id_Asset|
|Novo nome do Asset|Novo nome do Asset. Deixe vazio para manter o nome atual.|NovoAsset|
|Novo token do processo|Novo token do processo proprietário. Deixe vazio para manter o processo atual.|27FEXKIXFRFDUNVD|
|Nova key da instância|Nova key da instância proprietária. Deixe vazia para manter a instância atual.|6241c3a1dd96f8f92f|
|Novos mails dos usuários|Nova lista de e-mails de usuários associados. Escreva sem aspas, entre colchetes e separados por vírgula. Deixe vazia para manter os usuários atuais.|[usuario1@empresa.com, usuario2@empresa.com]|
|Novo tipo do Asset|Novo tipo do Asset text, password ou encrypted. Deixe vazio para manter o tipo atual.|Geral|
|Novo valor do Asset|Novo valor que será armazenado no Asset. Deixe vazio para manter o valor atual.|Um valor|
|Atribuir resultado a variável|Variavel que recebe True se o Asset foi modificado com sucesso.|Variável|

### Excluir Asset

Exclui um Asset existente pelo ID.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do Asset|ID do Asset que será excluído. Pode ser obtido com Obter Asset específico ativando os dados adicionais.|Id_Asset|
|Definir como variável|Variavel que recebe True se o Asset foi excluido com sucesso.|var|
