Detalhes : https://numpy.org/

NumPy é uma biblioteca de Python que fornece um objeto matriz multidimensional, vários objetos derivados e uma variedade de rotinas para operações rápidas em matrizes, incluindo matemática, lógica, manipulação de forma, classificação, seleção, E/S, álgebra linear básica, operações estatísticas básicas, simulação aleatória entre outros.

Os Arrays NumPy têm um tamanho fixo na criação, ao alterar o tamanho criará um novo array e excluirá o original.

Os elementos em uma matriz NumPy devem ser todos do mesmo tipo de dados, assim ocupando o mesmo espaço na memória.A exceção:pode-se ter array de objetos. 

Os Arrays NumPy facilitam operações matemáticas avançadas e outros tipos de operações em um grande número de dados.

IMPORT : import numpy as np

Comandos:

    np.array([1,2,3,4,5,6,7]) - Cria um array simples, uma matriz unidimensional.

    np.array([1,2,3,4,5,6,7], dtype = np.float64) - Cria um array de float 64 bits.

    np.array([1,2,3,4,5,6,7], dtype = np.int32) - Cria um array de int 32 bits.

    np.array([[7,2,23],[12,27,4],[5,34,23]]) - Cria uma matriz bidimensional.

    np.empty ([3,2], dtype = int) - Cria uma matriz 3 linhas x 2 colunas com elementos não inicializados.

    np.zeros([4,3]) - Cria uma matriz 4x3 com valores zero.

    np.ones([5,7]) - Cria uma matriz 5x7 com valores um.

    np.eye(5) - Cria uma matriz quadrada com a diagonal principal com valores 1 e  o resto 0.

    np.random.random((5)) - Cria uma matriz com valores aleatórios positívos.

    np random.randn((5)) - Cria uma matriz com valores aleatórios podendo ser negativo.

    np.floor(10*np.random.random((3,4))) - Cria uma matriz com valores aleatórios entre 0 e 10.

    np.floor([[7,2,23],[12,27,4],[5,34,23]) - Cria uma matriz com valor absoluto ou numero sem virgula.

    np.unique(NomeDaMatriz) - Pega todos os valores apenas 1 vez.

    np.sqrt(NomeDaMatriz) - Mostra o valor da raiz quadrada de todos os elementos.

    np.exp(NomeDaMatriz) - Mostra o valor do exponencial de todos os elementos.

    r = np.arange(15).reshape((3,5)) - Rearranja um conjunto de 15 elementos de 0 a 14 em 3 linhas e 5 colunas.

    r.transpose((1,0)) - Mostra a matriz transposta/invertida.

    np.where(x > 0, 1, -1) - Substitui os valores com base no x 