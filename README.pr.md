



# Orchestrator Framework

Permite administrar processos, tarefas, transações e Assets do NOC, além de enviar alertas, registrar logs e controlar a parada do framework.

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo

Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.


## Overview


1. Login NOC
Autentica com o NOC e abre uma sessão exigida por todos os outros comandos do módulo. Suporta API Key, e-mail e senha, ou um arquivo noc.ini.

2. Obter processos
Obter todos os processos

3. Obter Tarefas
Obter tarefas

4. Criar Tarefa
Adiciona uma nova tarefa

5. Estabelecer Prioridade
Estabelecer a prioridade de uma tarefa

6. Adicionar Transação
Adicionar uma nova transação

7. Adicionar várias Transações
Adicionar novas transações

8. Obter transações não processadas
Obter todas as transações não processadas de uma tarefa

9. Definir estado
Alterar o estado de uma transação

10. Enviar alerta
Envie uma mensagem de alerta para os e-mails definidos no processo do orquestrador

11. Enviar log personalizado
Enviar log personalizado

12. Parar Framework
Envia ao NOC uma solicitação de parada para uma instância específica do processo. Este comando define o estado de parada; não deve ser confundido com Deve parar o Framework?, que apenas consulta esse estado.

13. Deve parar o Framework?
Consulta no NOC se uma instância do processo possui uma solicitação de parada pendente. Não altera o estado: retorna True quando a instância deve parar e False quando pode continuar.

14. Obter Asset específico
Obtém um Asset pelo nome. Para Assets de processo ou instância, informe o token do processo e opcionalmente a key da instância. Retorna o valor, ou um dicionário completo com os dados adicionais habilitados.

15. Obter todos os Assets
Obtém todos os Assets disponíveis para o usuário autenticado. No modo básico retorna nome e valor e cria uma variável Rocketbot por Asset; com dados adicionais retorna uma lista de metadados completos.

16. Adicionar Asset
Cria um Asset de texto, senha ou criptografado. O escopo será global sem processo, de processo somente com o token ou de instância quando também for informada a key. Opcionalmente pode ser associado a usuários do NOC.

17. Modificar Asset
Atualiza um Asset existente pelo ID. Campos vazios mantêm os dados atuais do Asset; somente os campos informados são alterados.

18. Excluir Asset
Exclui um Asset existente pelo ID.




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