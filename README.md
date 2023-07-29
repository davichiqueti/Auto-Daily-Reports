# Auto Daily Reports
## Relatórios Automatizados com Notion API, OpenAI API, Requests e Pywhatkit

Projeto em Python para automatizar uma tarefa de minha rotina profissinal, o envio de um relatorio diário. Esse código acessa todas minhas atividades do dia cadastradas no Notion e envia os dados para que o ChatGPT prepare o texto para mim, logo em seguida enviando este para meu chefe.

## Tecnologias Utilizadas:

### 1. Notion API:

A API do Notion foi integrada ao projeto para acessar e recuperar dados de uma base de dados específica no Notion. Utilizando as credenciais de autenticação adequadas, o script é capaz de obter informações relevantes sobre as atividades armazenadas no Notion, tornando possível a geração de relatórios personalizados com base nesses dados em tempo real.

### 2. OpenAI API:

Através da poderosa API da OpenAI, mais especificamente o modelo GPT-3.5-Turbo, o projeto é capaz de criar relatórios detalhados e profissionais automaticamente. Para isso, uso um prompt testado para passar as instruções ao Chat Bot com um texto exemplar e com os dados filtrados extraidos do Notion.

### 3. Biblioteca requests:

A biblioteca `requests` é utilizada para realizar solicitações HTTP à API do Notion e à API da OpenAI. Ela mapeia o protocolo HTTP para uma semântica familiar da linguagem Python.

### 4. Biblioteca pywhatkit:

Por fim a biblioteca `pywhatkit` é utilizada para automatizar o envio dos relatórios gerados diretamente por mensagem. Ela permite que o script envie os relatórios como mensagens para o contato especificado em `config.json`

## Como utilizar o projeto:

1. **Configuração das Credenciais:**
   - Para utilizar a API do Notion e da OpenAI, você deve configurar as chaves de autenticação em um arquivo `config.json` com as informações necessárias.
   
2. **Execução do Script:**
   - Execute o script principal `main.py`.
   - O script irá acessar a API do Notion, recuperar os dados da base de dados e filtrar as atividades do dia atual.
   - Em seguida, a OpenAI é utilizada para gerar um relatório com base nessas atividades filtradas.
   - O relatório gerado é enviado automaticamente para um número de contato específico utilizando a biblioteca `pywhatkit`.

Com essas etapas, o processo de relatórios diários é automatizado, economizando tempo e esforço.
No caso de uso profissional converse com seu superior antes de automatizar esse processo.

## Observação:

Certifique-se de que todas as bibliotecas utilizadas estão devidamente instaladas no seu ambiente Python antes de executar o script. Para instalar as dependências, você pode utilizar o gerenciador de pacotes `pip`, como por exemplo:

`pip install requests pywhatkit`

Experimente a automação de relatórios fazendo um `clone` ou `fork` para replicar esse repositorio. cCm a combinação poderosa da Notion API e OpenAI API prepare rapidamente um resumo de seu trabalho diário.

