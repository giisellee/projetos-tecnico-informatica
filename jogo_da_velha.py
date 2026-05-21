# PRINCIPAIS VARIÁVEIS
tabuleiro = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]

placar = {'Jogador X' : 0, 'Jogador O' : 0, 'Empate': 0}

arquivo_placar = 'placar.txt'

coordenadas = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# FUNÇÕES

# FUNÇÕES interface: menu, mostrar tabuleiro, limpar tabuleiro.
def interface():
    print("+----------------------------+")
    print("|        Jogo da Velha       |")
    print("+----------------------------+")
    print("| Escolha uma opção a seguir:|")
    print("| 1. Iniciar Partida :)      |")
    print("| 2. Como jogar ;)           |")
    print("| 3. Mostrar placar >:)      |")
    print("| 4. Sobre :D                |")    
    print("| 0. Sair do jogo :(         |")
    print("+----------------------------+")

def mostrar_tabuleiro(tabuleiro):
    print("+---+---+---+")
    for i in range(3):
        print("|", end=" ")
        for l in range(3):
            print(tabuleiro[i * 3 + l], end=" | ")
        print("\n+---+---+---+")

def limpar_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        tabuleiro[i] = "_"

# FUNÇÕES regras: mostrar regras, verficar respostas para ver regras.
def regras():
    print(197*'-')
    print("1ª Regra: O tabuleiro é 3x3 onde antes de jogar você deve digitar as coordenadas para posicionar o símbolo no espaço correto, as linhas na horizontal são 'A', 'B' e 'C', na vertical são os números '1', '2' e '3', digite primeiro a letra e depois o número;")
    print("2ª Regra: À vez, cada jogador coloca a sua marca onde pretender (um joga com “0”, outro jogador com “X”);")
    print("3ª Regra: O objetivo do jogo é fazer uma sequência de três símbolos iguais, seja em linha vertical, horizontal ou diagonal, enquanto tenta impedir que seu adversário faça o mesmo;")
    print("4ª Regra: Quando um dos participantes faz uma linha, ganha o jogo;")
    print(197*'-')

def verifica_ver_regras():
    escolha = input("Deseja ver as regras antes de começar (s - sim/ n - não)? ")
    escolha = escolha.lower()
    if escolha == 's':
        print('E vamos as regras... você é bastante exótico, nunca vi niguém querer saber de regras...')
        regras()
    else:
        pass

# FUNÇÕES placar: mostrar, salvar, iniciar ou carregar placar.
def mostrar_placar():
    print('Placar atual: ')
    print(f'Jogador "X": {placar["Jogador X"]}')
    print(f'Jogador "O": {placar["Jogador O"]}')
    print(f'Empates: {placar["Empate"]}')

def salvar_placar():
    with open(arquivo_placar, 'w') as arquivo:
        for chave, valor in placar.items():
            arquivo.write(f'{chave}: {valor}\n')

def iniciar_placar():
    try:
        with open(arquivo_placar, 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split(': ')
                placar[chave] = int(valor)
    except FileNotFoundError:
        with open(arquivo_placar, 'w') as arquivo:
            for chave, valor in placar.items():
                arquivo.write(f'{chave}: {valor}\n')

# FUNÇÕES coordenadas: definir indices e verificar coordenadas. 
def coordenadas_para_indice(coordenada):
    c = 'ABC'.index(coordenada[0])
    l = int(coordenada[1]) - 1
    return 3 * l + c

def verifica_coordenada(vez):
    if vez in coordenadas:
        try:
            i = coordenadas_para_indice(vez)
            if tabuleiro[i] == '_':
                return True
            else:
                print("Essa posição já está ocupada. Escolha outra.")
                return False
        except (ValueError, IndexError):
            print("Coordenada inválida. Digite uma coordenada válida (letra|numero, por exemplo, A1).")
            return False
    else:
        print('Coordenada inexistente... Sabia que era pra você ter lido as regras >:(')

# FUNÇÃO resultado: verificar possíbilidade de vitória em linhas, colunas e diagonais.
def resultado_game_vitoria(tabuleiro, jogador):
    # linhas
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i + 1] == tabuleiro[i + 2] == jogador:
            return True

    # colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] == jogador:
            return True

    # diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador:
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador:
        return True

# FUNÇÃO game: partida, verificar possíbilidade de vitória por parte de algum jogador ou empate, sempre atualizando e salvando o placar.
def game():
    jogador_atual = 'X'
    vezes_partida = 0
    fim_de_jogo = False

    print('Acredito que você esteja cansado de escolher... se é "X" ou "O" eu decido por você, o jogador 1 vai ser "X" e o jogador 2 vai ser "O".')
    
    while not fim_de_jogo:
        try:
            vez = input(f'Jogador {jogador_atual} dedique o seu símbolo com muito cuidado (letra|numero, por exemplo A1): ')
            vez = vez.upper()

            if verifica_coordenada(vez):
                i = coordenadas_para_indice(vez)

                if tabuleiro[i] == '_':
                    tabuleiro[i] = jogador_atual
                    mostrar_tabuleiro(tabuleiro)

                    if resultado_game_vitoria(tabuleiro, jogador_atual):
                        mostrar_tabuleiro(tabuleiro)
                        print(f'O Jogador "{jogador_atual}" é o grande vencedor! :D')
                        if jogador_atual == 'X':
                            placar["Jogador X"] += 1
                            mostrar_placar()
                            salvar_placar()
                            limpar_tabuleiro(tabuleiro)
                        elif jogador_atual == 'O':
                            placar["Jogador O"] += 1
                            mostrar_placar()
                            salvar_placar()
                            limpar_tabuleiro(tabuleiro)

                        fim_de_jogo = True
                    else:
                        vezes_partida += 1
                        jogador_atual = 'X' if jogador_atual == 'O' else 'O'
                else:
                    print("Essa posição já está ocupada. Escolha outra.")
        except (ValueError, IndexError):
            print("Coordenada inválida. Digite uma coordenada válida (letra|numero, por exemplo, A1).")

        if vezes_partida == len(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print('Temos um empate!')
            placar['Empate'] += 1
            fim_de_jogo = True
            mostrar_placar()
            salvar_placar()
            limpar_tabuleiro(tabuleiro)

# CÓDIGO PRINCIPAL: iniciar ou carregar placar, verificar dados recebidos e chamar suas respectivas funções.
iniciar_placar()
while True:
    interface()
    try:
        opcao = int(input("Eu escolho a opção... "))
        if opcao == 0:
            print('Até a próxima! ;)')
            break
        
        elif opcao == 1:
            verifica_ver_regras()
            print('iniciando jogo...')
            game()

        elif opcao == 2:
            print('Como jogar/Regras')
            regras()

        elif opcao == 3:
            mostrar_placar()

        elif opcao == 4:
            print('Aluna responsável pelo desenvolvimento do código: Giselle Estevam Paiva.')
  
        else:
            print("Opção inesistente")

    except:
        print("Ação Inválida... Presta atenção ein!")