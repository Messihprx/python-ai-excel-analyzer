import openpyxl
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Essa linha carrega as variáveis de ambiente do arquivo .env

# 1. Configuração do Cliente NVIDIA
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY") 
)

def analisar_excel(caminho_arquivo):
    print(f"📦 Lendo arquivo: {caminho_arquivo}...")
    
    # 2. Abrir a planilha e ler os dados
    wb = openpyxl.load_workbook(caminho_arquivo)
    aba = wb.active
    
    # Vamos pegar os dados das primeiras 10 linhas para não estourar o limite de texto
    dados_planilha = ""
    for linha in aba.iter_rows(min_row=1, max_row=20, values_only=True):
        dados_planilha += str(linha) + "\n"

    # 3. Criar o Prompt para a IA
    prompt = f"Analise os seguintes dados extraídos de uma planilha Excel e faça um resumo executivo com os pontos principais:\n\n{dados_planilha}"

    # 4. Chamada da IA com o código que você forneceu
    print("🤖 IA processando dados...\n")
    completion = client.chat.completions.create(
      model="meta/llama-3.1-8b-instruct",
      messages=[{"role": "user", "content": prompt}],
      temperature=0.2,
      top_p=0.7,
      max_tokens=1024,
      stream=True
    )

    for chunk in completion:
      if chunk.choices and chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# Executar a função
if __name__ == "__main__":
    # Arquivo de exemplo de dados Excel
    analisar_excel("dados/dados.xlsx")