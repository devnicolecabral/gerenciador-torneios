import os 
import requests
from dotenv import load_dotenv

# Carrega a nossa Refresh Key do arquivo .env 
load_dotenv()
CM_REFRESH_KEY = os.getenv("CM_REFRESH_KEY")

def pegar_cracha_cm():
    print("Aguarde um minutinho. Estou pedindo autorização para a Challenger Mode....")

    # Endereço da CM

    url_auth = "https://publicapi.challengermode.com/mk1/v1/auth/access_keys"

    # Enviando a RK no formato que eles pedem (JSON)
    dados = {
        "refreshkey": CM_REFRESH_KEY
    }

    try: 
        # POST
        resposta = requests.post(url_auth, json=dados)

        # Se a resposta for 200 (ok), pegamos o nosso crachá. 
        if resposta.status_code == 200: 
            cracha = resposta.json()["value"]
            print("Sucesso!! Crachá da CM gerado.")
            return cracha
        
        else: 
            print(f"Erro ao pedir o crachá. Código de erro: {resposta.status_code}")
            print(f"Detalhes: {resposta.text}")
            return None
    except Exception as e:
        print(f"Aconteceu um erro no código: {e}") 
        return None

if __name__ == "__main__":
    token = pegar_cracha_cm()
    if token: 
        print(f"Seu token de acesso começa com: {token[:15]}...")
        