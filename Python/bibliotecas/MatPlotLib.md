Detalhes : https://matplotlib.org/

MatPlot é uma biblioteca dedicada ao traçado de gráfico em 2D para a criação de visualizações estáticas, animadas e interativas em Python.

IMPORT : import matplotlib.pyplot as plt

Comandos:

    enade.hist(column='Nº de Concluintes Inscritos',bins = 30) - Exemplo de gráfico a ser usado.
    plt.show() - mostra o gráfico

    plt.scatter(x,y) - Gráfico que representa a relação x e y conhecidos como gráfico de dispersão

    x1 = sequencia de 0 a 9.
    plt.plot(x1,x1**2) -  Para plotar o gráfico gerando valores diretos no "plot"


    Montar o layout:

        plt.ylabel('Concluintes') - Colocar nome na label y
        plt.title('Participantes') - Coloca nome na label x
        plt.xlim(0,400) - Indica limite no eixo x
        plt.ylim(0,400) - Indica limite no eixo y
        plt.grid(True) - Grade de apresentação 'Grid'
        plt.scatter(valory,valorx) - Coloca os dados no gráfico
        plt.show - Motra o gráfico