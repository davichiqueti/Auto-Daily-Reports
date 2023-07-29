# Auto Daily Reports
## Relatórios Automatizados com Notion API, OpenAI API, Requests e Pywhatkit

Este repositório contém um conjunto de scripts Python que automatizam a geração de relatórios de forma inteligente e eficiente. Veja abaixo como cada uma das tecnologias foi utilizada no projeto:

## Tecnologias Utilizadas:

### 1. Notion API:

A API do Notion foi integrada ao projeto para acessar e recuperar dados de uma base de dados específica no Notion. Utilizando as credenciais de autenticação adequadas, o script é capaz de obter informações relevantes sobre as atividades armazenadas no Notion, tornando possível a geração de relatórios personalizados com base nesses dados em tempo real.

### 2. OpenAI API:

Através da poderosa API da OpenAI, mais especificamente o modelo GPT-3.5-Turbo, o projeto é capaz de criar relatórios detalhados e profissionais automaticamente. O modelo de linguagem da OpenAI é capaz de compreender o contexto e gerar texto coeso e relevante, permitindo que o script crie relatórios de alta qualidade de forma rápida e precisa.

### 3. Biblioteca requests:

A biblioteca `requests` é utilizada para realizar solicitações HTTP à API do Notion e à API da OpenAI. Com ela, o script pode fazer chamadas para recuperar dados da base de dados do Notion e enviar o conteúdo gerado pela OpenAI para ser utilizado no relatório.

### 4. Biblioteca pywhatkit:

A biblioteca `pywhatkit` é utilizada para automatizar o envio dos relatórios gerados diretamente por mensagem. Ela permite que o script envie os relatórios como mensagens em aplicativos de mensagens instantâneas, facilitando o compartilhamento dos relatórios com as partes interessadas.

## Como utilizar o projeto:

1. **Configuração das Credenciais:**
   - Para utilizar a API do Notion e da OpenAI, você deve configurar as chaves de autenticação em um arquivo `config.json` com as informações necessárias.
   
2. **Execução do Script:**
   - Execute o script principal `main.py`.
   - O script irá acessar a API do Notion, recuperar os dados da base de dados e filtrar as atividades do dia atual.
   - Em seguida, a OpenAI é utilizada para gerar um relatório com base nessas atividades filtradas.
   - O relatório gerado é enviado automaticamente para um número de contato específico utilizando a biblioteca `pywhatkit`.

Com essas etapas, o processo de relatórios diários é automatizado, economizando tempo e esforço.

## Observação:
Certifique-se de que todas as bibliotecas utilizadas estão devidamente instaladas no seu ambiente Python antes de executar o script. Para instalar as dependências, você pode utilizar o gerenciador de pacotes `pip`, como por exemplo:

# Relatórios Automatizados com Notion API, OpenAI API, Requests e Pywhatkit

Este repositório contém um conjunto de scripts Python que automatizam a geração de relatórios de forma inteligente e eficiente. Veja abaixo como cada uma das tecnologias foi utilizada no projeto:

## Tecnologias Utilizadas:

### 1. Notion API:

A API do Notion foi integrada ao projeto para acessar e recuperar dados de uma base de dados específica no Notion. Utilizando as credenciais de autenticação adequadas, o script é capaz de obter informações relevantes sobre as atividades armazenadas no Notion, tornando possível a geração de relatórios personalizados com base nesses dados em tempo real.

### 2. OpenAI API:

Através da poderosa API da OpenAI, mais especificamente o modelo GPT-3.5-Turbo, o projeto é capaz de criar relatórios detalhados e profissionais automaticamente. O modelo de linguagem da OpenAI é capaz de compreender o contexto e gerar texto coeso e relevante, permitindo que o script crie relatórios de alta qualidade de forma rápida e precisa.

### 3. Biblioteca requests:

A biblioteca `requests` é utilizada para realizar solicitações HTTP à API do Notion e à API da OpenAI. Com ela, o script pode fazer chamadas para recuperar dados da base de dados do Notion e enviar o conteúdo gerado pela OpenAI para ser utilizado no relatório.

### 4. Biblioteca pywhatkit:

A biblioteca `pywhatkit` é utilizada para automatizar o envio dos relatórios gerados diretamente por mensagem. Ela permite que o script envie os relatórios como mensagens em aplicativos de mensagens instantâneas, facilitando o compartilhamento dos relatórios com as partes interessadas.

## Como utilizar o projeto:

1. **Configuração das Credenciais:**
   - Para utilizar a API do Notion e da OpenAI, você deve configurar as chaves de autenticação em um arquivo `config.json` com as informações necessárias.
   
2. **Execução do Script:**
   - Execute o script principal `main.py`.
   - O script irá acessar a API do Notion, recuperar os dados da base de dados e filtrar as atividades do dia atual.
   - Em seguida, a OpenAI é utilizada para gerar um relatório com base nessas atividades filtradas.
   - O relatório gerado é enviado automaticamente para um número de contato específico utilizando a biblioteca `pywhatkit`.

Com essas etapas, o processo de relatórios diários é automatizado, economizando tempo e esforço.

## Observação:

Certifique-se de que todas as bibliotecas utilizadas estão devidamente instaladas no seu ambiente Python antes de executar o script. Para instalar as dependências, você pode utilizar o gerenciador de pacotes `pip`, como por exemplo:


Experimente agora mesmo a automação de relatórios com a combinação poderosa de Notion API, OpenAI API, Requests e Pywhatkit! Simplifique seu fluxo de trabalho diário e aprimore a geração de relatórios com essa solução inteligente.

