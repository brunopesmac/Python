Detalhes: https://pandas.pydata.org/

Pandas é um pacote para a manupulação dos dados de nossa investigação usando Inteligência Artificial em Python. Fornece uma série de recursos de leitura e manipulação de grandes bases de dados com uma grande variedade de comandos.

IMPORT: import pandas as pd

Comandos:

    Comando no Colab:

        from google.colab import files - Importa o files
        uploaded = files.upload() - Habilita a importação

variavel = pd.read_excel('NomeDoArquivo') - Le o arquivo excel

variavel.shape - Mostra o número de linhas e colunas.

variavel.head() - Mostra os 5 primeiros dados.

variavel.head(8)- Mostra os 8 primeiros dados.

alunos = {'Nome':['Marcelo','Lucas','Cynthia','Helena'],'Media':[4,7,5.5,9],'Status':['Reprovado','Aprovado','Reprovado','Aprovado']} - Cria um objetos

variavel2 = pd.DataFrame(alunos) - Transforma os dados em um datasets

varialvel2.describe() - Traz informações importantes sobre as colunas numéricas do dataframe

variavel2.loc[[1,3]] - Traz os dados dos repectivos índices.

pd.Series([1,2,4,5,8,1,2,1,5,3,7]) - Coloca os dados em uma coluna cada um com um índice.

variavel.rename(colums={"numeros":"nr"}) - Troca o nome das colunas.

variavel.drop("numeros",axis=1,inplace=True) - Apaga a coluna.

variavel.dropna() - Retira as linhas vazias.

variavel.isnull() - Retorna onde tem dados faltantes.