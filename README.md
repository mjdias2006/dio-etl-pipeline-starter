<div align="center">

# 🚀 DIO ETL Pipeline Starter

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)]()

*Um pipeline simples de ETL (Extract, Transform, Load) para automação de análise de portfólios de clientes.*

</div>

## 📝 Projeto
Este repositório contém uma implementação prática de **ETL**. O objetivo é extrair dados de clientes, aplicar uma regra de negócio e salvar o resultado de forma estruturada.

## 🛠 Funcionalidades
- **Extract:** Definição da base de dados de clientes.
- **Transform:** Lógica de negócio que sugere diversificação de investimentos com base no perfil do cliente.
- **Load:** Exportação do arquivo final em formato `JSON`.

## 📁 Estrutura
```text
├── data/
│   └── processed/          # Dados transformados (.json)
├── main.py                 # Script principal de execução
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto
