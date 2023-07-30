# Auto Report - Automatização de Relatórios Diários

   Automatização de Relatórios Diários consumindo API do Notion e da OpenAI com envio por WhatsApp utilizando PyWhatKit. O objetivo desse projeto é automatizar uma tarefa    
   repetitiva com uma solução útil e criativa. Automatização de Relatórios Diários

## Funcioanmento:

   A partir de uma requisição para a API do Notion são extraídas informações do meu planejamento profissional. As tarefas são transformadas em dicionários com seus títulos, descrições e categorias.

   As atividades do dia atual são enviadas no body de uma requisição para a API da OpenAI pedindo que o ChatGPT faça um relatório sobre essas atividades. Para maior precisão um exemplo e  outras instruções são definidos em ```prompt.py```.

   Por fim, a biblioteca PyWhatKit é utilizada para fazer o envio desse relátorio para meu superior. Seu número está configurado no arquivo ```config.json``` assim como as chaves das API´s e o ID da tabela do Notion.

## Tecnologias Utilizadas:

   * `Linguagem Python`
   * Estrutura e execução de ```Requisições HTTP``` utilizando ```Requests```
   * Consumo da ```Notion API``` 
   * Consumo da ```OpenAI API```
   * Envio de mensagens com ```PyWhatKit```

## Referências:

   [Documentação Biblioteca Requests](https://requests.readthedocs.io/en/latest/)
   [Documentação Notion API](https://developers.notion.com/reference/intro)
   [Documentação OpenAI API](https://platform.openai.com/docs/introduction)
