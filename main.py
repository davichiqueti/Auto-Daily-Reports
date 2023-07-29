import requests
import json
import datetime
import pywhatkit


def getNotionDB(notion_key, notion_db_id):

    url = f"https://api.notion.com/v1/databases/{notion_db_id}/query"

    headers = {
        'Authorization': f'Bearer {notion_key}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
        }
    
    response = requests.post(url, headers=headers)
    data = response.json()
    activities = []
    date = str(datetime.date.today())

    for item in data['results']:

        task_date = item['properties']['Date']['date']['start']
        task_infotxt = item['properties']['About Task']['rich_text']

        if task_date == date:

            tag_propertie = item['properties']['Tags']['select']

            item_dict = {
                'Name': item['properties']['Name']['title'][0]['text']['content'],
                'Date': item['properties']['Date']['date']['start'],
                'Tags': tag_propertie['name'] if tag_propertie != None else ' ',
                'About Task': task_infotxt[0]['plain_text'] if task_infotxt else ' '
            }

            activities.append(item_dict)

        else: pass


    return activities


def getChatGptText(openai_key, today_activities, example_text):

    date = datetime.date.today()

    model_id = 'gpt-3.5-turbo'
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        'Authorization': f'Bearer {openai_key}',
        'Content-Type': 'application/json'
        }
    
    body = {
        'model': model_id,
        'messages': [
            {
                'role': 'user',
                'content': f'''
                    Faça um breve relatorio sobre atividades do dia,
                    com o cabeçalho "Relatorio dia {date.day} do {date.month}:".
                    Após isso prossiga com as atividades, Deixe uma linha em branco para separar as atividades.
                    Use como exemplo esse texto: "{example_text}".
                    Segue as atividades em dicionario: "{today_activities}".
                    Legenda:    "Name": É o nome da atividade,
                            "Date": "2023-07-28": Data da atividade,
                            "Tags": É o setor em que a atividade se enquadra, não é necessario passar essa informação.
                            Mas você pode organizar as tarefas da mesma tag juntas
                            "About Task": Informação adicional sobre a atividade
                    Seja Breve não quero textos muito longos.
                    Caso a tarefa não tenha informação adicional em "About Task" não extenda-a muito.
                    Tarefas de rotina devem apenas conter o título da tarefa. Não é necessario descrição sobre elas
                        '''
            }
        ]
    }

    body = json.dumps(body)
    response = requests.post(url, headers=headers, data=body)
    data = response.json()

    return data["choices"][0]['message']['content']


def read_configs():

    with open("config.json", 'r') as json_file:

        config_json = json.load(json_file)

    return config_json


def main():
    # Lendo config.json
    config_json = read_configs()
    # Extraindo Variaveis do json
    notion_key = config_json["config_info"]["notion_key"]
    notion_db_id = config_json["config_info"]["notion_db_id"]
    openai_key = config_json['config_info']['openai_key']
    contact_number = config_json["config_info"]["contact_number"]
    example_text = config_json["example_text"]["content"]

    activities_dict = getNotionDB(notion_key, notion_db_id)
    final_text = getChatGptText(openai_key, activities_dict, example_text)
    pywhatkit.sendwhatmsg_instantly(contact_number, final_text)


if __name__ == '__main__':

    main()