import os
import WConio2 as WConio2
import random
from personagens import criar_party
from menu import menu_principal

AMARELO = '\033[33m'
AZUL = '\033[34m'
VERMELHO = '\033[31m'
VERDE = '\033[32m'
CINZA = '\033[90m'
BRANCO = '\033[m'

CORES = {
    "▣": '\033[33m',
    "∎": '\033[90m',
    "❂": '\033[36m',
    "☠": '\033[31m',
    "☢": '\033[31m',
    "☣": '\033[31m'
}

if menu_principal() == "Sair":
    raise SystemExit
os.system("cls")

linhas = 20
colunas = 50

# CRIAÇÃO DA FUNÇÃO SALA:
def sala():
    Matriz = []
    for i in range(20):
        Matriz.append([])
        for j in range(50):
            Matriz[i].append(" ")
    Matriz = obstaculos(Matriz)
    Matriz = baus(Matriz)
    Matriz = portas(Matriz)
    Matriz = minions(Matriz)
    return Matriz

# GERAR OBSTÁCULOS EM LUGAR ALEATÓRIO, COM ESPAÇO DESOCUPADO E NÃO PODENDO OCUPAR O ESPAÇO DO HERÓI;
def obstaculos(Matriz):
    obstaculosL = [(1, 0), (2, 0), (2, 1), (2, 2)]
    obstaculosT = [(1, 0), (1, 1), (1, 2), (2, 1), (3, 1)]
    obstaculosU = [(1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)]
    obstaculosDeitadoL = [(1, 0), (1, 1), (1, 2), (2, 0)]
    formatos = [obstaculosL, obstaculosT, obstaculosU, obstaculosDeitadoL]
    for i in range(50):
        encaixar = 0
        while encaixar < 100:
            linha = random.randint(0, 19)
            coluna = random.randint(0,49)
            formato = random.choice(formatos) #escolhe aleatoriamente os formatos da list;
            encaixeValido = True
            for encaixarLinha, encaixarColuna in formato: #verificar se o local do novo formato não contem objetos, não sobrepor outros objetos;
                novaLinha = linha + encaixarLinha
                novaColuna = coluna + encaixarColuna
                if not (0 <= novaLinha < 20 and 0 <= novaColuna < 50):
                    encaixeValido = False
                    break
                if (Matriz[novaLinha][novaColuna] != " "):
                    encaixeValido = False
                    break
                if ((novaLinha, novaColuna) == (0, 0)):
                    encaixeValido = False
                    break
            if encaixeValido:
                for encaixarLinha, encaixarColuna in formato:
                    novaLinha = linha + encaixarLinha
                    novaColuna = coluna + encaixarColuna
                    Matriz[novaLinha][novaColuna] = "∎"
                break
            encaixar += 1
    return Matriz

# GERAR BAÚ EM LUGAR ALEATÓRIO, COM ESPAÇO DESOCUPADO E NÃO PODENDO OCUPAR O ESPAÇO DO HERÓI;
def baus(Matriz):
    for i in range(2):
        while(True):
            linha = random.randint(0, 19)
            coluna = random.randint(0, 49)
            if (Matriz[linha][coluna] == " "):
                if ((linha, coluna) != (0, 0)):
                    Matriz[linha][coluna] = "▣"
                    break
    return Matriz

# GERAR PORTA EM LUGAR ALEATÓRIO, COM ESPAÇO DESOCUPADO E NÃO PODENDO OCUPAR O ESPAÇO DO HERÓI;
def portas(Matriz):
    while(True):
        linha = random.randint(0, 19)
        coluna = random.randint(0, 49)
        if (Matriz[linha][coluna] == " "):
            if ((linha, coluna) != (0, 0)):
                Matriz[linha][coluna] = "❂"
                break
    return Matriz

# GERAR INIMIGOS EM LUGAR ALEATÓRIO, COM ESPAÇO DESOCUPADO E NÃO PODE OCUPAR O ESPAÇO DO HERÓI;
def minions(Matriz):
    for i in range(2):
        while(True):
            linha = random.randint(0, 19)
            coluna = random.randint(0, 49)
            if(Matriz[linha][coluna] == " "):
                if ((linha, coluna) != (0, 0)):
                    Matriz[linha][coluna] = "☠"
                    break
    return Matriz

# CRIAÇÃO DA FUNÇÃO SALA MINIBOSS:
def salaMiniBoss():
    Matriz = []
    for i in range(20):
        Matriz.append([])
        for j in range(50):
            Matriz[i].append(" ")
    Matriz[10][25] = "☢"
    Matriz = obstaculos(Matriz)
    return Matriz

# CRIAÇÃO DA FUNCÃO SALA BOSS:
def salaBoss():
    Matriz = []
    for i in range(20):
        Matriz.append([])
        for j in range(50):
            Matriz[i].append(" ")
    Matriz[10][25] = "☣"
    return Matriz

salaAtual = 1
salaFinal = 10
bauAberto = 0
totalBaus = 2
inimigos = 0
totalInimigos = 2
heroiI = 0
heroiJ = 0
party = criar_party()
mensagem = ""

os.system("cls")

Matriz = sala()

# LAÇO DE REPETIÇÃO :
while(True):
    WConio2.gotoxy(0, 0)

    Tela = []                                                      # cria nova lista;
    for i in range(linhas):                                        # percorre as linhas da matriz;
        Tela.append(Matriz[i].copy())                              # copia a linha atual da matriz e adiciona para nova lista "Tela";
    Tela[heroiI][heroiJ] = party[0].simbolo                        # desenha o herói;

# CRIAÇÃO DE BORDAS :
    tela = ""
    tela += "╔"
    tela += (colunas) * "═"
    tela += "╗"
    tela += "\n"

    for i in range(len(Matriz)):
        tela += "║"
        for j in range(len(Tela[i])):
            simbolo = Tela[i][j]
            cor = CORES.get(simbolo, "")
            if cor:
                tela += cor + simbolo + BRANCO
            else:
                tela += simbolo
        tela += "║\n"

    tela += "╚"
    tela += (colunas) * "═"
    tela += "╝"
    tela += "\n"

    print(tela)
    print(salaAtual)
    print(mensagem)

# INTERAÇÃO DO USUÁRIO :
    if(WConio2.kbhit()):                                           # verifica se alguma tecla foi digitada;
        codigo, letra = WConio2.getch()                            # pega a tecla digitada;

# APAGA AS MENSAGENS DEPOIS DE ANDAR :
        if letra in ("a", "s", "d", "w"):
            mensagem = " " * 80

        novaI = heroiI                                             # cria nova variável de verificação para o heroi andar;
        novaJ = heroiJ                                             # cria nova variável de verificação para o heroi andar;
        posicionamento = [(heroiI - 1, heroiJ), (heroiI + 1, heroiJ), (heroiI, heroiJ - 1), (heroiI, heroiJ +1)] # interação com objetos, posicionamento vizinha: cima, baixo, esquerda e direita;

# MOVIMENTAÇÃO DO HERÓI (a, s, d, w):
        if(letra == 'a' and heroiJ > 0):
            novaJ -=1
        elif(letra == 'd' and heroiJ < (colunas-1)):
            novaJ +=1
        if(letra == 'w' and heroiI > 0):
            novaI -=1
        elif(letra == 's' and heroiI < (linhas-1)):
            novaI +=1

# VERIFICA SE A MOVIMENTAÇÃO É PERMITIDA:
        if letra in ("a", "s", "d", "w"):                          # verifica se as teclas digitadas estão em "letras";
            if (0 <= novaI < linhas and 0 <= novaJ < colunas):     # verifica se a posição está dentro da matriz;
                if (Matriz[novaI][novaJ] == " "):                  # verifica se a posição está vazia;
                    heroiI = novaI                                 # atualização do herói;
                    heroiJ = novaJ                                 # atualização do herói;

# INTERAÇÃO COM O BAÚ :
        if (letra == "e" and bauAberto < 2):                       # interação com a letra "e" e a sala tem dois baús que podem ser abertos;
            for i, j in posicionamento:                            # percorre "posicionamento" suas direções;
                if (0 <= i < linhas and 0 <= j < colunas):         # verifica se a posição está dentro da matriz (incapaz de seguir uma posição inválida);
                    if (Matriz[i][j] == "▣"):                      # verifica se existe "B" de baú na matriz;
                        Matriz[i][j] = " "                         # depois de aberto, o baú desaparece;
                        bauAberto += 1                             # depois de abrir um baú, o próximo da mesma sala pode ser aberto;
                        mensagem = "Encontrou Baú!"                # mensagem exibida após interagir com a letra "e";
                        break                                      # encerra o "for" de interação com o baú;

# INTERAÇÃO COM OBSTÁCULOS :
        if (letra == "q"):                                         # interação com a letra "q";
            for i, j in posicionamento:                            # percorre "posicionamento" suas direções;
                if (0 <= i < linhas and 0 <= j < colunas):         # verifica se a posição está dentro da matriz (incapaz de seguir uma posição inválida);
                    if (Matriz[i][j] == "∎"):                      # verifica se existe "■" de obstáculo na matriz;
                        Matriz[i][j] = " "                         # depois de quebrar, o obstáculo desaparece;
                        mensagem = "Destruiu Rocha!"               # mensagem exibida após interagir com a letra "q";
                        break                                      # encerra o "for" de interação com o obstáculo;

# INTERAÇÃO COM O INIMIGO :
        if (letra == "e"):
            for i, j in posicionamento:
                if (0 <= i < linhas and 0 <= j < colunas):
                    if(Matriz[i][j] == "☠"):
                        Matriz[i][j] = " " # por enquanto é vazio, esperar para por função de batalha
                        inimigos += 1
                        mensagem = "Encontrou Inimigo!"
                        break

# INTERAÇÃO COM O MINIBOSS:
        if (letra == "e"):
            for i, j in posicionamento:
                if (0 <= i < linhas and 0 <= j < colunas):
                    if (Matriz[i][j] == "☢"):
                        Matriz[10][25] = " "
                        Matriz[10][27] = "▣"
                        Matriz[10][29] = "❂"
                        mensagem = "Pode seguir para próxima sala!"
                        break

# INTERAÇÃO COM A PORTA :
        if (letra == "e"):                                         # interação com a letra "e";
            for i, j in posicionamento:                            # percorre "posicionamento" suas direções;
                if (0 <= i < linhas and 0 <= j < colunas):         # verifica se a posição está dentro da matriz (incapaz de seguir uma posição inválida);
                    if (Matriz[i][j] == "❂"):                      # verifica se existe "P" de porta na matriz;
                        # VERIFICAÇÃO SE A SALA É A DO MINIBOSS:
                        if salaAtual in (3, 6, 9):
                            if bauAberto == 1:
                                mensagem = "Portal liberado!"
                                salaAtual += 1
                                if (salaAtual == salaFinal):
                                    Matriz = salaBoss()
                                    mensagem = "Lute contra o Boss!"
                                elif salaAtual in (3, 6, 9):
                                    Matriz = salaMiniBoss()
                                    mensagem = "Lute contra o MiniBoss!"
                                else:
                                    Matriz = sala()
                                    mensagem = "Portal liberado!"
                                heroiI = 0
                                heroiJ = 0
                                bauAberto = 0
                                inimigos = 0
                            else:
                                mensagem = "Derrote o Miniboss!"
                        # VERIFICAÇÃO SE A SALA É NORMAL:
                        else:
                            if (bauAberto == totalBaus and inimigos == totalInimigos):
                                mensagem = "Porta liberada!"
                                if (salaAtual < salaFinal):                # verifica que a sala atual não ultrapasse o limite de salas;
                                    salaAtual += 1
                                    if salaAtual in (3, 6, 9):
                                        Matriz = salaMiniBoss()
                                        mensagem = "Lute contra o MiniBoss!"
                                    else:
                                        Matriz = sala()                    # chama a função "sala()";
                                        mensagem = "Encontrou porta!"      # mensagem exibida após passar de sala;
                                        if (salaAtual == salaFinal):            # verifica se a sala atual chegou no seu limite;
                                            Matriz = salaBoss()                # chama a função "salaBoss()"
                                            mensagem = "Sala Final. Lute contra o BOSS ..." # mensagem exibida ao entrar na sala;
                                    heroiI = 0                             # coloca o herói na posição definida;
                                    heroiJ = 0                             # coloca o herói na posição definida;
                                    bauAberto = 0
                                    inimigos = 0
                            else:
                                mensagem = "Encontre todos os baús e derrote todos os inimigos!"
                            break                                  # encerra o "for" de interação com a porta;
