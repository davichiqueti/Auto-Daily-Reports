import requests
import json
import datetime
import pywhatkit
from prompt import prompt


class AutoReport():

    def __init__(self, notion_key, notion_db_id, openai_key, contact_number):
        # Construindo um objeto da classe
        self.notion_key = notion_key
        self.notion_db_id = notion_db_id
        self.openai_key = openai_key
        self.contact_number = contact_number
        # Atributo adicional da data atual e texto de prompt
        self.report_date = datetime.date.today()
        

    def requestNotionAPI(self):
        # Consumo da Notion API
        url = f"https://api.notion.com/v1/databases/{self.notion_db_id}/query"

        headers = {
            'Authorization': f'Bearer {self.notion_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28'
            }
        
        response = requests.post(url, headers=headers)
        data = response.json()
        notion_data = []

        for item in data['results']:

            task_date = item['properties']['Date']['date']['start']
            task_checkbox = item['properties']['Done']['checkbox']

            if (task_date == str(self.report_date)) and (task_checkbox == True):
                # Tratamento dos dados que são da data atual e estão marcados como concluídos

                task_name = item['properties']['Name']['title'][0]['text']['content']
                task_tag = item['properties']['Tags']['select']
                task_info_list = item['properties']['Description']['rich_text']

                item_dict = {
                    'Name': task_name,
                    'Tags': task_tag['name'] if task_tag != None else ' ', # Vericando se a tarefa possui tag
                    'Description': task_info_list[0]['plain_text'] if len(task_info_list) != 0 else ' ' # Vericando se a tarefa possui descrição
                }

                notion_data.append(item_dict)

            else:

                pass

        self.notion_data = notion_data


    def requestOpenAiAPI(self):
        # Consumo da OpenAI API
        model_id = 'gpt-3.5-turbo'
        url = "https://api.openai.com/v1/chat/completions"

        headers = {
            'Authorization': f'Bearer {self.openai_key}',
            'Content-Type': 'application/json'
            }
        
        body = {
            'model': model_id,
            'messages': [
                {
                    'role': 'user',
                    'content': prompt(self.report_date, self.notion_data) # Passagem de um prompt personalizado para precisão na resposta
                }
            ]
        }

        body = json.dumps(body)
        response = requests.post(url, headers=headers, data=body)
        data = response.json()

        self.final_text = data["choices"][0]['message']['content']


    def sendMessage(self):
        # Método para envio da mensagem por WhatsApp
        pywhatkit.sendwhatmsg_instantly(self.contact_number, self.final_text)



def readConfigJson():
    # Função para ler configurações no arquivo json
    with open("config.json", 'r') as json_file:

        config_json = json.load(json_file)

    return config_json


def main():
    # Lendo config.json
    config_json = readConfigJson()

    # Extraindo Variaveis do json
    notion_key = config_json["notion_key"]
    notion_db_id = config_json["notion_db_id"]
    openai_key = config_json['openai_key']
    contact_number = config_json["contact_number"]

    # Gerando um objeto da classe AutoReport e chamando seus métodos
    dailyReport = AutoReport(notion_key, notion_db_id, openai_key, contact_number)
    dailyReport.requestNotionAPI()
    dailyReport.requestOpenAiAPI()
    dailyReport.sendMessage()
    

if __name__ == '__main__':

    main()