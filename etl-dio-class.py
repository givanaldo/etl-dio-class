# EXTRACT - listagem de alunos e suas notas de um arquivo CSV
# ===========================================================

import pandas as pd

# Definindo o nome do arquivo CSV
arquivo_csv = 'turma.csv'

# Lendo o arquivo CSV usando o Pandas
dados = pd.read_csv(arquivo_csv)

# imprimir as primeiras linhas do DataFrame
print(dados.head())

# TRANSFORM - calcular as médias dos alunos e a situação na disciplina
# ====================================================================

# Calculando a média ponderada com pesos 2 e 3
dados['media'] = (dados['nota1'] * 2 + dados['nota2'] * 3) / 5

# Determinando a situação do aluno com base na média
def determinar_situacao(media):
    if media >= 60:
        return 'Aprovado'
    elif media >= 30:
        return 'Recuperação'
    else:
        return 'Reprovado'

# Aplicando a função para determinar a situação e criando a coluna 'situacao' no DataFrame
dados['situacao'] = dados['media'].apply(determinar_situacao)

# Imprimindo o DataFrame com as colunas de média e situação
print(dados)

# LOAD - Cria uma planilha excel e um arquivo JSON com o dataframe atualizado
# ===========================================================================

# Criando um arquivo Excel a partir do DataFrame
dados.to_excel('turma.xlsx', index=False)

# Criando um arquivo JSON a partir do DataFrame
dados.to_json('turma.json', orient='records')