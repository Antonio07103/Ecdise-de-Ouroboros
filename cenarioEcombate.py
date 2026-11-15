import textwrap
import os
import WConio2 as WConio2
import random
from personagens import criar_party
from menu import menu_principal, escolher_membro
from baus import preparar_fase, entregar_conteudo, fase_da_sala, recompensa_miniboss
from combate import iniciar_combate
from itens import usar_inventario, recuperar_party
from inimigos import sortear_encontro, criar_miniboss, criar_boss, nome_completo_boss

inventario = []
faseAtual = 1
baus_da_fase = preparar_fase(faseAtual)

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

# função da sala
def sala():
    if salaAtual in (1, 2):
        totalInimigos = 2
    elif salaAtual in (4, 5):
        totalInimigos = 3
    elif salaAtual in (7, 8):
        totalInimigos = 3
    Matriz = []
    for i in range(20):
        Matriz.append([])
        for j in range(50):
            Matriz[i].append(" ")
    Matriz = obstaculos(Matriz)
    Matriz = baus(Matriz)
    Matriz = portas(Matriz)
    Matriz = minions(Matriz, totalInimigos)
    return Matriz, totalInimigos

# obstaculo em lugares aleatorios
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

# baus 
def baus(Matriz):
    for i in range(totalBaus):
        while(True):
            linha = random.randint(0, 19)
            coluna = random.randint(0, 49)
            if (Matriz[linha][coluna] == " "):
                if ((linha, coluna) != (0, 0)):
                    Matriz[linha][coluna] = "▣"
                    break
    return Matriz

#portas
def portas(Matriz):
    while(True):
        linha = random.randint(0, 19)
        coluna = random.randint(0, 49)
        if (Matriz[linha][coluna] == " "):
            if ((linha, coluna) != (0, 0)):
                Matriz[linha][coluna] = "❂"
                break
    return Matriz

# inimigos sendo gerados em lugares aleatorios
def minions(Matriz, totalInimigos):
    for i in range(totalInimigos):
        while(True):
            linha = random.randint(0, 19)
            coluna = random.randint(0, 49)
            if(Matriz[linha][coluna] == " "):
                if ((linha, coluna) != (0, 0)):
                    Matriz[linha][coluna] = "☠"
                    break
    return Matriz

# minbosses
def salaMiniBoss():
    Matriz = []
    for i in range(20):
        Matriz.append([])
        for j in range(50):
            Matriz[i].append(" ")
    Matriz[10][25] = "☢"
    Matriz = obstaculos(Matriz)
    return Matriz

# sala boss
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
totalBaus = 3                  # baús por sala comum (a sala do miniboss tem 1)
inimigos = 0
totalInimigos = 2
heroiI = 0
heroiJ = 0
rastro = [(0, 0)] * 4                # últimas posições do cavaleiro (os companheiros andam por elas)
party = criar_party()
mensagem = ""

# reiniciar partida quando a party for derrotada
def reiniciar_jogo():
    global inventario, faseAtual, baus_da_fase, salaAtual, bauAberto, inimigos
    global totalInimigos, heroiI, heroiJ, rastro, party, mensagem, Matriz, posicionamento
    os.system("cls")
    print("Você perdeu, recomece!")
    print("Sua jornada recomeçou, batalhe com valentia!")
    print()
    print("Pressione qualquer tecla")
    WConio2.getch()
    os.system("cls")

    inventario = []
    faseAtual = 1
    baus_da_fase = preparar_fase(faseAtual)
    salaAtual = 1
    bauAberto = 0
    inimigos = 0
    totalInimigos = 2
    heroiI = 0
    heroiJ = 0
    rastro = [(0, 0)] * 4
    party = criar_party()
    posicionamento = []                  # evita interagir com a posição da sala antiga
    mensagem = "Você voltou ao inicio, lute com valentia e vença-os!"
    Matriz, totalInimigos = sala()

# caixa de diálogo: o texto fica na tela (quebrado em linhas) até o jogador apertar E
def dialogo(texto):
    os.system("cls")
    for linha in str(texto).split("\n"):
        for pedaco in textwrap.wrap(linha, 70) or [""]:
            print(pedaco)
    print()
    print(CINZA + "(pressione E para continuar)" + BRANCO)
    while True:
        codigo, letra = WConio2.getch()
        if letra.lower() == "e":
            break
    os.system("cls")

# mensagem de abertura do chefe: nome completo, com título
def anunciar_chefe(nome_completo):
    os.system("cls")
    print(f"{nome_completo} bloqueia o caminho!")
    print()
    print(CINZA + "(pressione qualquer tecla)" + BRANCO)
    WConio2.getch()
    os.system("cls")

os.system("cls")

Matriz, totalInimigos = sala()


while(True):
    WConio2.gotoxy(0, 0)

    Tela = []                                                      # cria nova lista;
    for i in range(linhas):                                        # percorre as linhas da matriz;
        Tela.append(Matriz[i].copy())                              # copia a linha atual da matriz e adiciona para nova lista "Tela";
    for k, membro in enumerate(party[1:], 1):                      # companheiros seguem o cavaleiro, um atrás do outro
        ci, cj = rastro[-k]
        Tela[ci][cj] = membro.simbolo
    Tela[heroiI][heroiJ] = party[0].simbolo                        

# bordas
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
    print(f"Sala {salaAtual}   |   I: itens ({len(inventario)})".ljust(60))
    print(mensagem)

    for membro in party:
        membro.mostrar_status()

# user interação
    if(WConio2.kbhit()):                                           # verifica se alguma tecla foi digitada;
        codigo, letra = WConio2.getch()                            # pega a tecla digitada;

# anda e apaga as mensagens
        if letra in ("a", "s", "d", "w"):
            mensagem = " " * 80

        novaI = heroiI                                             # cria nova variável de verificação para o heroi andar;
        novaJ = heroiJ                                             # cria nova variável de verificação para o heroi andar;
        posicionamento = [(heroiI - 1, heroiJ), (heroiI + 1, heroiJ), (heroiI, heroiJ - 1), (heroiI, heroiJ +1)] # interação com objetos, posicionamento vizinha: cima, baixo, esquerda e direita;

# movimentacao heroi (a, s, d, w):
        if(letra == 'a' and heroiJ > 0):
            novaJ -=1
        elif(letra == 'd' and heroiJ < (colunas-1)):
            novaJ +=1
        if(letra == 'w' and heroiI > 0):
            novaI -=1
        elif(letra == 's' and heroiI < (linhas-1)):
            novaI +=1

# verifica se a movimentacao ta permitida
        if letra in ("a", "s", "d", "w"):                          # verifica se as teclas digitadas estão em "letras";
            if (0 <= novaI < linhas and 0 <= novaJ < colunas):     # verifica se a posição está dentro da matriz;
                if (Matriz[novaI][novaJ] == " "):                  # verifica se a posição está vazia;
                    rastro.append((heroiI, heroiJ))                # guarda de onde o cavaleiro saiu
                    del rastro[:-4]
                    heroiI = novaI                                 # atualização do herói;
                    heroiJ = novaJ                                 # atualização do herói;

#baus e interacao
        if (letra == "e" and bauAberto < totalBaus):                # interação com a letra "e" enquanto ainda há baús para abrir na sala;
            for i, j in posicionamento:                            # percorre "posicionamento" suas direções;
                if (0 <= i < linhas and 0 <= j < colunas):         # verifica se a posição está dentro da matriz (incapaz de seguir uma posição inválida);
                    if (Matriz[i][j] == "▣"):                      # verifica se existe "B" de baú na matriz;
                        Matriz[i][j] = " "                         # depois de aberto, o baú desaparece;
                        bauAberto += 1                             # depois de abrir um baú, o próximo da mesma sala pode ser aberto;
                        dialogo(entregar_conteudo(party, baus_da_fase.pop(), inventario, escolher_membro))   # o que veio no baú, até apertar E
                        break                                      # encerra o "for" de interação com o baú;

# inventario (usar itens fora do combate)
        if (letra == "i"):
            usar_inventario(party, inventario)
            os.system("cls")

# obstaculos
        if (letra == "f"):                                         # interação com a letra "q";
            for i, j in posicionamento:                            # percorre "posicionamento" suas direções;
                if (0 <= i < linhas and 0 <= j < colunas):         # verifica se a posição está dentro da matriz (incapaz de seguir uma posição inválida);
                    if (Matriz[i][j] == "∎"):                      # verifica se existe "■" de obstáculo na matriz;
                        Matriz[i][j] = " "                         # depois de quebrar, o obstáculo desaparece;
                        mensagem = "Destruiu Rocha!"               # mensagem exibida após interagir com a letra "q";
                        break                                      # encerra o "for" de interação com o obstáculo;

# inimigo interacao
        if (letra == "e"):
            for i, j in posicionamento:
                if (0 <= i < linhas and 0 <= j < colunas):
                    if(Matriz[i][j] == "☠"):
                        venceu = iniciar_combate(party, sortear_encontro(salaAtual), inventario)
                        if not venceu:
                            reiniciar_jogo()
                            break
                        Matriz[i][j] = " "
                        inimigos += 1
                        dialogo(f"Inimigo derrotado! ({inimigos}/{totalInimigos})")
                        break

#interacao com os boss e miniboss
        if (letra == "e"):
            for i, j in posicionamento:
                if (0 <= i < linhas and 0 <= j < colunas):
                    if (Matriz[i][j] == "☢"):
                        chefe = criar_miniboss(salaAtual)
                        chefe.simbolo = "☢"
                        anunciar_chefe(chefe.nome_completo())
                        venceu = iniciar_combate(party, [chefe], inventario)
                        if not venceu:
                            reiniciar_jogo()
                            break
                        Matriz[10][25] = " "
                        Matriz[10][27] = "▣"
                        Matriz[10][29] = "❂"
                        dialogo(recompensa_miniboss(salaAtual, party, inventario) or "Pode seguir para próxima sala!")
                        break

        if (letra == "e"):
            for i, j in posicionamento:
                if (0 <= i < linhas and 0 <= j < colunas):
                    if (Matriz[i][j] == "☣"):
                        cabecas = criar_boss()                     # a Hydra são 3 cabeças
                        for cabeca in cabecas:
                            cabeca.simbolo = "☣"
                        anunciar_chefe(nome_completo_boss())
                        venceu = iniciar_combate(party, cabecas, inventario)
                        if not venceu:
                            reiniciar_jogo()
                            break
                        os.system("cls")
                        print("VITÓRIA!")
                        print(f"Você derrotou {nome_completo_boss()} e concluiu a jornada!")
                        print()
                        print(CINZA + "(pressione qualquer tecla para sair)" + BRANCO)
                        WConio2.getch()
                        raise SystemExit

# portas
        if (letra == "e"):                                         # interação com a letra "e";
            for i, j in posicionamento:                            # percorre "posicionamento" suas direções;
                if (0 <= i < linhas and 0 <= j < colunas):         # verifica se a posição está dentro da matriz (incapaz de seguir uma posição inválida);
                    if (Matriz[i][j] == "❂"):                      # verifica se existe "P" de porta na matriz;
                        # verificacao da sala do miniboss
                        if salaAtual in (3, 6, 9):
                            if bauAberto == 1:
                                mensagem = "Portal liberado!"
                                salaAtual += 1
                                descanso = recuperar_party(party)
                                if (salaAtual == salaFinal):
                                    Matriz = salaBoss()
                                    mensagem = "Mostre sua valentia e lute contra o Boss!"
                                elif salaAtual in (3, 6, 9):
                                    Matriz = salaMiniBoss()
                                    mensagem = "Lute contra o MiniBoss, mostre sua força para encarar o Boss!"
                                else:
                                    Matriz, totalInimigos = sala()
                                    mensagem = "Portal liberado!"
                                mensagem += " " + descanso
                                heroiI = 0
                                heroiJ = 0
                                rastro = [(0, 0)] * 4
                                bauAberto = 0
                                inimigos = 0
                            else:
                                mensagem = "Derrote o Miniboss!"
                            break                                  # encerra o "for" de interação com a porta;
                        # verificacao da sala
                        else:
                            if (bauAberto == totalBaus and inimigos == totalInimigos):
                                mensagem = "Porta liberada!"
                                if (salaAtual < salaFinal):                # verifica que a sala atual não ultrapasse o limite de salas;
                                    totalInimigos += 2

                                    salaAtual += 1
                                    descanso = recuperar_party(party)
                                    if salaAtual in (3, 6, 9):
                                        Matriz = salaMiniBoss()
                                        mensagem = "Lute contra o MiniBoss!"
                                    else:
                                        Matriz, totalInimigos = sala()                    # chama a função "sala()";
                                        mensagem = "Encontrou porta!"      # mensagem exibida após passar de sala;
                                        if (salaAtual == salaFinal):            # verifica se a sala atual chegou no seu limite;
                                            Matriz = salaBoss()                # chama a função "salaBoss()"
                                            mensagem = "{-Sala Final-}\n Mostre toda sua valentia e derrote o Boss!" # mensagem exibida ao entrar na sala;
                                    mensagem += " " + descanso
                                    heroiI = 0                             # coloca o herói na posição definida;
                                    heroiJ = 0                             # coloca o herói na posição definida;
                                    rastro = [(0, 0)] * 4
                                    bauAberto = 0
                                    inimigos = 0
                            else:
                                mensagem = "Encontre todos os baús e derrote todos os inimigos!"
                            break                                  # encerra o "for" de interação com a porta;

    if fase_da_sala(salaAtual) != faseAtual:
                faseAtual = fase_da_sala(salaAtual)
                baus_da_fase = preparar_fase(faseAtual)