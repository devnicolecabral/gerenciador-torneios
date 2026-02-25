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
    

def buscar_jogadores(torneio_id):
    # Pega o crachá temporário 
    token = pegar_cracha_cm()
    
    if not token:
        print("Sem crachá, não podemos prosseguir.")
        return None
        
    print(f"Buscando inscritos do torneio: {torneio_id}...")
    
    # Endereço da API para buscar os participantes 
    url_participantes = f"https://publicapi.challengermode.com/mk1/v1/tournaments/{torneio_id}/participants"
    
    # Colocamos o nosso crachá no header do pedido
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    try:
        # Fazemos o pedido de leitura (GET)
        resposta = requests.get(url_participantes, headers=headers)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            print("Lista de jogadores lida com sucesso!")
            return dados
        else:
            print(f"Erro ao ler participantes. Código: {resposta.status_code}")
            print(f"Detalhes: {resposta.text}")
            return None
            
    except Exception as e:
        print(f"Aconteceu um erro no código: {e}")
        return None

# --- Área de Teste ---
if __name__ == "__main__":
    # Colar o ID do seu torneio de teste aqui dentro das aspas quando tiver
    ID_TESTE = "ID_DO_TORNEIO_AQUI" 
    
    dados_torneio = buscar_jogadores(ID_TESTE)
    
    if dados_torneio:
        print("-" * 30)
        print("A API devolveu isso aqui (amostra):")
        # Imprime só os primeiros 500 caracteres para não travar a tela
        print(str(dados_torneio)[:500] + " ... [tem mais coisas]")