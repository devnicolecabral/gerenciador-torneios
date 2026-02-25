import pandas as pd 

# Simulação do que a API da CM vai devolver 

dados_simulados = {
    "participants": [
        {"username": "TLV", "status": "Played", "score": 20},
        {"username": "FakerBR", "status": "NoShow", "score": 0}, # W.O.
        {"username": "Megalodon", "status": "Played", "score": 15},
        {"username": "Soneca", "status": "NoShow", "score": 0} # Outro W.O.
    ]
}

def processar_torneio(dados, nome_arquivo = "jogadores_aprovados.csv"):
    print("Iniciando o processamento dos dados...")

    df = pd.DataFrame(dados["participants"])

    print("\n Tabela original (com todos os inscritos): ")
    print(df)

    df_aprovados = df[df["Status"] != "NoShow"]

    df_aprovados.to_csv(nome_arquivo, index=False)

    print("\n Taela limpa (Pronta pra riot - Sem W.O):")
    print(df_aprovados)

    return df_aprovados


# --- Área de Teste ---
if __name__ == "__main__":
    processar_torneio(dados_simulados)

