# Importação de bibliotecas externas
import json
import os

# EXTRACT (Extração): Dados simulados como exemplo.
clientes = [
    {
        'id': 1,
        'nome': 'Ana',
        'investimentos': 100
    },
    {
        'id': 2,
        'nome': 'Beto',
        'investimentos': 500
    },
    {
        'id': 3,
        'nome': 'Carla',
        'investimentos': 200
    }
]

# TRANSFORM (Transformação): Aplicação da regra de negócio com estrutura condicional.
for cliente in clientes:
    if cliente['investimentos'] < 300:
        cliente['mensagem'] = "O que acha de diversificar?"
    else:
        cliente['mensagem'] = "Portfólio ótimo!"

# LOAD (Carregamento): Salvamento dos dados processados no caminho correto.
pasta_saida = 'data/processed'

# 01. Criação da pasta automaticamente para evitar erros de diretório.
os.makedirs(pasta_saida, exist_ok=True)

# 02. Definição do caminho completo do arquivo.
caminho_arquivo = os.path.join(pasta_saida, 'resultado_etl.json')

# 03. Salvamento dos dados em formato JSON, com codificação para os caracteres especiais.
with open(caminho_arquivo, 'w', encoding='utf-8') as f:
    json.dump(clientes, f, indent=4, ensure_ascii=False)

# 04. Confirmação visual no terminal para o usuário.
print(f"Sucesso! Dados processados e salvos em: {caminho_arquivo}")
