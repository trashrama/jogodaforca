from random import randint

def sortearPalavra(palavras):
    return randint(1, (len(palavras)-1))


def printarErro(erro):
    if erro == 1:
        print('O'.center(50))
    elif erro == 2:
        print('O'.center(50))
        print('|'.center(50))
        print('|'.center(50))
    elif erro == 3:
        print('O'.center(50))
        print('|/'.center(50))
        print(' | '.center(50))
    elif erro == 4:
        print('O'.center(50))
        print('\|/'.center(50))
        print(' | '.center(50))
    elif erro == 5:
        print('O'.center(50))
        print('\|/'.center(50))
        print('/   '.center(50))
    elif erro == 6:
        print('O'.center(50))
        print('\|/'.center(50))
        print('/ \ '.center(50))



def rodarJogo():
    erro = 0
    categorias = {1: 'comida', 2: 'musica nacional/internacional', 3: 'personagens', 4: 'time de futebol'}
    dados = [('milho', categorias[1]), ('bolo', categorias[1]), ('cosmo', categorias[3]), ('batata', categorias[1]), ('instituto', 'estudamos em um'), ('fortaleza', categorias[4]), ('sangue', 'liquido do corpo'), ('cinto', 'vestuario'), ('pride','album de kendrick lamar')]
    
    lista_palavras = []
    lista_dicas = []
    for palavra, dica in dados:
        lista_palavras.append(palavra)
        lista_dicas.append(dica)

    palavra = list(lista_palavras[sortearPalavra(lista_palavras)])
    mascara = ['_'] * len(palavra)

    while True:

        i_dica = lista_palavras.index("".join(palavra))
        print('\n\n')
        print(" ".join(mascara))
        print("\nDica: {}".format(lista_dicas[i_dica]))
        tentativa = input('Digite uma letra: ')

        if len(tentativa) == 1:
            for i, letra in enumerate(palavra):
                if tentativa == letra:
                    mascara[i] = letra

            if mascara == palavra:
                print(''.join(mascara))
                print('Você acertou!\n')
                print('Próxima rodada! ')
                rodarJogo()

            elif tentativa not in palavra:
                erro += 1
                printarErro(erro)
                if erro == 6:
                    print('Game Over'.center(50))
                    print('A palavra era: ' + "".join(palavra))
                    print('Tentar novamente? Y ou N - ', end='')
                    esc = input()

                    if esc.replace("  ", " ").strip().upper() == 'Y':
                        rodarJogo()
                    if esc.replace("  ", " ").strip().upper() == 'N':
                        break
        else:
            print('Insira apenas um cáracter\n')


rodarJogo()