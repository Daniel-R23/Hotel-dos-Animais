def printMatriz(matriz): #Função que recebe uma matriz como parâmetro e a imprime na tela com pulando uma linha a cada linha da matriz
    for i in range(2):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()


def validaVizinhoErrado(animal, matriz, linha, coluna): #Função que recebe o animal que não pode ser vizinho do animal a ser colocado, a matriz dos quartos, a linha e a coluna que esse animal se encontra. Retorna se esse animal que não pode ser vizinho, o é considerando os limites da matriz
    if linha == 1:
        if coluna == 3:
            return matriz[linha][coluna - 1] == animal or matriz[linha - 1][coluna] == animal
        elif coluna == 0:
            return matriz[linha - 1][coluna] == animal
        else:
            return matriz[linha][coluna - 1] == animal or matriz[linha][coluna + 1] == animal or matriz[linha - 1][coluna] == animal
    else:
        if coluna == 3:
            return matriz[linha][coluna - 1] == animal or matriz[linha - 1][coluna] == animal or matriz[linha + 1][coluna] == animal
        elif coluna == 0:
            return matriz[linha - 1][coluna] == animal or matriz[linha + 1][coluna] == animal
        else:
            return matriz[linha][coluna - 1] == animal or matriz[linha][coluna + 1] == animal or matriz[linha - 1][coluna] == animal or matriz[linha + 1][coluna] == animal


def regraDoJogo(animal, matriz, linha, coluna): #Função que recebe, o animal a ser posicionado, a matriz, linha e colunas onde ele vai ser posto e de acordo com cada animal, chama a função anterior pra validar se ele pode ficar naquela posição. Se puder, retorna True senão, False
    if animal == 'G':
        if validaVizinhoErrado('C', matriz, linha, coluna):
            print('O gato não pode ficar ao lado do cão')
            return False
        else:
            print('Parabéns, você acertou!')
            return True
    elif animal == 'C':
        if validaVizinhoErrado('O', matriz, linha, coluna):
            print('O cão não pode ficar ao lado do osso')
            return False
        else:
            print('Parabéns, você acertou!')
            return True
    elif animal == 'R':
        if validaVizinhoErrado('G', matriz, linha, coluna):
            print('O rato não pode ficar ao lado do gato')
            return False
        else:
            print('Parabéns, você acertou!')
            return True
    elif animal == 'O':
        if validaVizinhoErrado('C', matriz, linha, coluna):
            print('O osso não pode ficar ao lado do cão')
            return False
        else:
            print('Parabéns, você acertou!')
            return True
    elif animal == 'Q':
        if validaVizinhoErrado('R', matriz, linha, coluna):
            print('O queijo não pode ficar ao lado do rato')
            return False
        else:
            print('Parabéns, você acertou!')
            return True
    else:
        print('Nome de animal inválido')
        return False


def validaEscolha(escolha): #Função que recebe a posição que o jogador escolheu para posicionar o animal e verifica se é uma posição válida dentro dos limites da matriz. Retorna 0 caso seja um lugar válido dentro da primeira linha, retorna 1 caso seja um lugar válido na segunda linha e retorna 3 caso seja uma posição que não existe na matriz
    if escolha < 5:
        i = 0
    elif 4 < escolha <= 8:
        i = 1
    else:
        print('Digite uma posição válida')
        return 3
    return i


def fase(numeroFase, matriz, elementos): #Função que abstrai tudo que há em uma fase do jogo, recebe o número da fase, a matriz daquela fase e uma lista com os animais a ser posicionado dentro dos quartos
    while True:
        print("Bem vindos à fase " + numeroFase)
        saudacao = "Você deve alocar o "
        for elemento in elementos:
            saudacao += elemento + ", "
        saudacao = saudacao.removesuffix(", ")
        saudacao += " nos quartos:"
        print(saudacao)

        for elemento in elementos: #Para cada animal a ser posicionado, verifica se ele pode ficar naquela posição, se há vizinhos válidos e se o quarto está livre. Caso esteja tudo certo, retorna True, caso o jogador erre a jogada, retorna False
            lugarValido = False
            while(lugarValido == False):
                printMatriz(matriz)
                escolha = int(input("Em qual quarto você quer colocar o " + elemento + "?"))
                if validaEscolha(escolha) == 3:
                    continue
                elif validaEscolha(escolha) == 0:
                    i = 0
                    escolha -= 1
                    lugarValido = True
                elif validaEscolha(escolha) == 1:
                    i = 1
                    escolha -= 5
                    lugarValido = True

                if matriz[i][escolha] != '_':
                    print('Este quarto não está disponível. Por favor, escolha um livre')
                    lugarValido = False

            matriz[i][escolha] = elemento[0]
            printMatriz(matriz)
            if not regraDoJogo(elemento[0], matriz, i, escolha):
                return False
                break
        return True
        break


def imprimeTitulo(titulo): #Função que recebe o título do jogo e o imprime com uma formatação de asteriscos em cima e embaixo dele
    print("*"*len(titulo)*3)
    print(" "*len(titulo) + titulo + " "*len(titulo))
    print("*"*len(titulo)*3)


def jogo(): #Função que imprime o título e as regras do jogo
    imprimeTitulo("Hotel dos Animais")

    print("\t\tREGRAS:")
    print("\t\tEsse é um hotel onde os hóspedes têm algumas restrições quanto a localização de seu quarto, seguindo as seguintes regras:\n")
    print("\t\t• O rato não pode ficar ao lado do gato.")
    print("\t\t• O cão não pode ficar ao lado do osso.")
    print("\t\t• O gato não pode ficar ao lado do cão.")
    print("\t\t• O queijo não pode ficar ao lado do rato.\n")

    print("\nEspecificando as posições:")
    print("[1,2,3,4]")
    print("[5,6,7,8]\n")

while(True): #Loop principal do jogo onde são chamada as regras e cada fase do jogo. Caso o jogador erre o jogo encerra com a mensagem "Você perdeu!", caso o jogador vença todas as fases, é impressa na tela a mensagem "Você ganhou!"
    jogo()
    if fase("1", [['*', '*', '_', 'G'], ['R', '_', '*', '*']], ['RATO', 'GATO']):
        if fase("2", [['_', '*', '*', '*'], ['*', 'C', '_', '_']], ['CÃO', 'CÃO', 'OSSO']):
            if fase("3", [['_', '*', '*', '*'], ['_', 'G', '_', '*']], ['GATO', 'RATO', 'OSSO']):
                if fase("4", [['_', '_', '_', '*'], ['*', 'R', '*', '*']], ['QUEIJO', 'QUEIJO', 'OSSO']):
                    print("Você ganhou!")
                    break
                else:
                    print("Você perdeu!")
                    break
            else:
                print("Você perdeu!")
                break
        else:
            print("Você perdeu!")
            break
    else:
        print("Você perdeu!")
        break