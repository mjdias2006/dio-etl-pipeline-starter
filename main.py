# Importação da biblioteca JSON, dentro do Python.
import json

# EXTRAÇÃO (EXTRACT): Definição dos dados para o processamento, em uma lista.
clientes = [
    {'id': 1, 'nome': 'Ana', 'investimentos': 100},
    {'id': 2, 'nome': 'Beto', 'investimentos': 500},
    {'id': 3, 'nome': 'Carla', 'investimentos': 200}
]

# TRANSFORMAÇÃO (TRANSFORM): Criação de uma função para ser a regra do negócio, com mensagens para o cliente.
def transformar_dados(lista_clientes):
    for cliente in lista_clientes:
        if cliente['investimentos'] < 300:
            cliente['mensagem'] = f"Olá, {cliente['nome']}! Que tal diversificar seus investimentos?"
        else:
            cliente['mensagem'] = f"Parabéns, {cliente['nome']}! Seu portfólio está ótimo."
    return lista_clientes

# Variável para a versão atualizada dos dados.
clientes_atualizados = transformar_dados(clientes)

# CARGA (LOAD): Resultado final salvo em um arquivo local na máquina, com a criação de uma função de salvamento.
def salvar_dados(dados):
    with open('resultado_etl.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Sucesso! O arquivo 'resultado_etl.json' foi criado.")

# Execução do salvamento dos dados, chamando a função de salvamento.
salvar_dados(clientes_atualizados)
