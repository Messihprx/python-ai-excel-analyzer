# 📊 AI Excel Analyzer (NVIDIA NIM + Python)

Este projeto é uma ferramenta de **Automação de Inteligência Artificial** que lê dados de planilhas Excel (`.xlsx`) e utiliza modelos de linguagem de última geração para gerar insights e resumos executivos automáticos.

## 🚀 Funcionalidades
* **Extração de Dados:** Leitura automatizada de planilhas usando `openpyxl`.
* **Processamento de IA:** Integração com o modelo **Llama-3.1-8b** da Meta através da infraestrutura de baixo atraso da NVIDIA.
* **Streaming de Resposta:** Visualização da análise da IA em tempo real.
* **Segurança:** Gestão de credenciais via variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **NVIDIA NIM API** (Interface compatível com OpenAI)
* **Openpyxl** (Manipulação de Excel)
* **Python-dotenv** (Segurança de chaves)

## Detalhe
* A pasta dados.xlsx está apenas para fins demonstrativos, em casos reais essa pasta não subirá

## 📦 Como Instalar e Rodar

1. **Abra seu terminal e clone o repositório:**
   ```bash
   git clone [https://github.com/Messihprx/python-ai-excel-analyzer.git](https://github.com/Messihprx/python-ai-excel-analyzer.git)
* Para rodar o programa, precisará de uma chave de API no site da NVIDIA.
* Modelo: https://build.nvidia.com/meta/llama-3_1-8b-instruct
* O usuário só precisa ir no canto superior direito do site onde está escrito "view code" em uma aba com bordas verdes
* Após clicar em view code, O tester precisará criar (ou logar) uma conta no site.
* Depois de logar, o tester já pode criar uma chave de API
* Copie a chave de API e crie um arquivo chamado ".env" com o seguinte formato: NVIDIA_API_KEY=Sua_key_aqui
* Obs: Não utilize aspas nem nada, somente a chave
* Assim que o .env estiver sido criado e com a chave dentro, você pode rodar o arquivo main.py
