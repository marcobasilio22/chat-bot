import yaml
import requests

class ApiRequest:
    def __init__(self):
        try:
            with open("/home/marco/Estudo/chat-bot-alb/backend/app/datas.yaml", 'r') as file:
                self.datas = yaml.safe_load(file)
            
            self.access_token = self.datas['access_token']
        except FileNotFoundError:
            print("O arquivo datas.yaml não foi encontrado.")
            raise
        except KeyError as e:
            print(f"Chave ausente no arquivo YAML: {e}")
            raise

    def create_payload(self, number, message):
        url = "http://localhost:9090/message/sendText/BotWhatsapp"

        headers = {
            'apikey': f'{self.access_token}',
            'Content-Type': 'application/json'
        }

        payload = {
            "number": number,
            "textMessage": {
                "text": f"{message}"
            }
        }

        return url, headers, payload

    def send_request(self, url, headers, payload):
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                print('Mensagem enviada com sucesso!')
                return response.json()
            else:
                print('Falha ao enviar a mensagem.')
                print(f'Status Code: {response.status_code}')
                print(f'Resposta: {response.text}')
                return {"error": "Falha ao enviar a mensagem.", "details": response.text}
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")
            return {"error": str(e)}

    def send_messages(self, number, message):
        try:
            url, headers, payload = self.create_payload(number, message)
            response = self.send_request(url, headers, payload)
            if response:
                return response
            return {"error": "Falha ao enviar a mensagem."}
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
            return {"error": str(e)}
