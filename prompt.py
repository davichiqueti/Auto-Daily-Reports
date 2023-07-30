def prompt(report_date, notion_data):

    example_text = '''Relatório dia 28 do 7:

-Solicitação de cadastro de Marca na Shopee: Foi solicitado o cadastro da marca na plataforma de vendas online Shopee.

- Exclusão de anúncios das garrafas sem rendimento: Foram excluídos os anúncios das garrafas que não apresentaram bom desempenho nas vendas.

- Edição de imagem para as garrafas Fresh Juice: Realizei a edição das imagens das garrafas Fresh Juice para melhorar a qualidade visual dos anúncios.

- Processamento dos pedidos.

- Recriação dos anúncios na Shopee: Recriei os anúncios na plataforma Shopee, adicionando uma promoção aos novos anúncios."

'''

    final_text = f'''
Faça um breve relatorio sobre atividades do dia,
com o cabeçalho "Relatorio dia {report_date.day} do {report_date.month}:".
Após isso prossiga com as atividades, Deixe uma linha em branco para separar as atividades.
Use como exemplo esse texto: "{example_text}".
Segue as atividades em dicionario: "{notion_data}".
Legenda:    
    "Name": É o nome da atividade,
    "Date": "2023-07-28": Data da atividade,
    "Tags": É o setor em que a atividade se enquadra, não é necessario passar essa informação.
    "About Task": Informação adicional sobre a atividade
Seja Breve não quero textos muito longos.
Caso a tarefa não tenha informação adicional em "About Task" não extenda-a muito.
Tarefas de rotina devem apenas conter o título da tarefa. Não é necessario descrição sobre elas.
Não faça textos genericos como "- Outra tarefa: Sua tarefa - Outra tarefa de rotina: Outra tarefa"
'''
    
    return final_text
