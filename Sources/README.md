# projeto_mba_eng_python
projeto python para engenharia - MBA

# Projeto de Limpeza e Transformação de Dados de Voos

## Descrição
Este projeto tem como objetivo a limpeza e transformação de um conjunto de dados de voos, extraído de um repositório público. O fluxo de dados segue as seguintes etapas:

1. **Leitura e limpeza dos dados**: O script `clean_data.py` realiza o carregamento e a limpeza dos dados.
2. **Transformação dos dados**: O script `transforme_data.py` processa os dados limpos, gerando novas colunas e categorizando os horários dos voos.
3. **Orquestração**: O script `main.py` gerencia a execução das etapas anteriores.

## Estrutura dos Arquivos

### `main.py`
Arquivo responsável por orquestrar a execução do fluxo de dados:
- Executa a limpeza de dados utilizando `CleanData`.
- Aplica a transformação de dados com `TransformData`.

### `clean_data.py`
Arquivo responsável pela limpeza dos dados:
- Faz a leitura do dataset de voos a partir de uma URL.
- Converte colunas de data para um formato adequado.
- Filtra dados inválidos e remove duplicatas.
- Renomeia colunas para um formato padronizado.
- Aplica funções para padronização de strings através do módulo `tools.py`.

### `transforme_data.py`
Arquivo responsável por transformar os dados limpos:
- Converte o tempo de voo de horas para minutos.
- Classifica os voos em turnos com base na hora de decolagem.
- Retorna o DataFrame transformado.

### `tools.py`
Arquivo utilitário contendo a função:
- `padroniza_str()`: Remove caracteres especiais e formata strings para maiúsculas.

## Dependências
Para rodar este projeto, é necessário instalar as seguintes bibliotecas:
```bash
pip install pandas
