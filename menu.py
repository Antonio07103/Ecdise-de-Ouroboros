import os
import WConio2 as WConio2

os.system("")

AMARELO = '\033[33m'
AZUL = '\033[34m'
VERMELHO = '\033[31m'
VERDE = '\033[32m'
CINZA = '\033[90m'
BRANCO = '\033[m'

TITULO = TITULO = r"""
( ▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄   ▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄
▀▄░▒▒▒▓▓▓█▐  ▄▀░▒▒▓▀▌▀▄░▒▒▓▒▒░▀▄  ▀▄░▒▒▒▓█▀▄▀░▒▒▓▓█▓▒█▄▀▄░▒▒▒▓▓▓█▐
 ▐░▒▄▀▀▀▄█ ▐░░▄▀▀▄█▐  ▌░▒▄▀▀▄░░▌   ▐░▒▄█  ▌░░▄▀▀▀▀▀█▀   ▐░▒▄▀▀▀▄█
 ▐▓ ▐▄▄▄   ▌▓ ▌  ▀▀▀  ▌▓ ▌  ▐ ▓▐   ▐▓ ▓▌  ▐   ▀▀▀▀▄     ▐▓ ▐▄▄▄
 ▌▒▓▓▒░▌  ▐▓▒▐        ▌▒▓▌   ▌▒▓▌  ▌▒▓▓▌   ▀▄▄▄█▓▓▒▀▄   ▌▒▓▓▒░▌
 ▌░ ▐▀▀    ▐▒░▌  ▄▄▄  ▌░ █  ▐░▒▐   ▌░ ▐▌  ▄▄▄▄ ▀▌▒░░▐▌  ▌░ ▐▀▀
 ▌  ▀▄▄▄▀█ ▐░░▀▄▄▀ ▐  ▌  ▀▄▄▀░░▌   ▌   █  ▐  ▀▄▄▀ ░ █▌  ▌  ▀▄▄▄▀█
▄▀        ▐  ▀▄░░  ▄▌▄▀     ░░▄▀  ▄▀  ░▓█▄ ▐▌      ▄▄▀ ▄▀        ▐
▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀   ▀▀▀▀▀▀▀▀     ▀▀▀▀▀▀   ▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀▀▀▀
▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄
▀▄░▒▒▓▒▒░▀▄  ▀▄░▒▒▒▓▓▓█▐
 ▌░▒▄▀▀▄░░▌   ▐░▒▄▀▀▀▄█
 ▌▓ ▌  ▐ ▓▐   ▐▓ ▐▄▄▄
 ▌▒▓▌   ▌▒▓▌  ▌▒▓▓▒░▌
 ▌░ █  ▐░▒▐   ▌░ ▐▀▀
 ▌  ▀▄▄▀░░▌   ▌  ▀▄▄▄▀█
▄▀     ░░▄▀  ▄▀        ▐
▀▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀▀▀▀
   ▄▄▄▄▄            ▄     ▄▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄     ▄▄▄▄▄▄▄▄        ▄▄▄▄▄      ▄▄▄▄▄▄▄▄
 ▄▀░▒▒▒░▀▄    ▄▀▄  █░▀▄  ▌░▒▒▒▓▓▓█░▄    ▄▀░▒▒▒░▀▄  ▀▄░▒▒▒▓▓▓█░▄   ▄▀░▒▒▒░▀▄  ▌░▒▒▒▓▓▓█░▄    ▄▀░▒▒▒░▀▄  ▄▀░▒▒▓▓█▓▒█▄
▐░░▄▀▀▀▄░░▌  ▐░░▓▌ ▀▄░░▌ ▐▐░▒▄▀▀▀▐▓░▌  ▐░░▄▀▀▀▄░░▌   ▐░▒▄▀▀▀▐▓░▌ ▐░░▄▀▀▀▄░░▌ ▐▐░▒▄▀▀▀▐▓░▌  ▐░░▄▀▀▀▄░░▌ ▌░░▄▀▀▀▀▀█▀
▌▓ ▌   ▐ ▓▐  ▌▓ ▒▌  ▐ ▓▓▌ ▐▓ ▐▌ ▄▀▄▀   ▌▓ ▌   ▐ ▓▐   ▐▓ ▐▌ ▄▀▄▀  ▌▓ ▌   ▐ ▓▐  ▐▓ ▐▌ ▄▀▄▀   ▌▓ ▌   ▐ ▓▐ ▐   ▀▀▀▀▄
▐▓▒▐     ▌▒▓▌▐▓▒░▐    ▌▒▓▐ ▌▒▓▓▀▀░▀▄   ▐▓▒▐     ▌▒▓▌  ▌▒▓▓▀▀░▀▄  ▐▓▒▐     ▌▒▓▌ ▌▒▓▓▀▀░▀▄   ▐▓▒▐     ▌▒▓▌ ▀▄▄▄█▓▓▒▀▄
▐▒░▌   ▐░▒▐ ▐▒▒░▌   ▐░▒██ ▌░ ▐▀▀▄▓▒█   ▐▒░▌   ▐░▒▐   ▌░ ▐▀▀▄▓▒█  ▐▒░▌   ▐░▒▐  ▌░ ▐▀▀▄▓▒█   ▐▒░▌   ▐░▒▐ ▄▄▄▄ ▀▌▒░░▐▌
▐░░▀▄▄▄▀░░▌ ▐▌░░▀▄▄▄▀░░▐▌ ▌  █   █░ █  ▐░░▀▄▄▄▀░░▌   ▌  ▀▄▄▄▀░ █ ▐░░▀▄▄▄▀░░▌  ▌  █   █░ █  ▐░░▀▄▄▄▀░░▌ ▐  ▀▄▄▀ ░ █▌
 ▀▄     ▄▀   ▀▄       ▄▀ ▄▀  ▀▄ ▄▀   █  ▀▄     ▄▀  ▄▀         ▄▀  ▀▄     ▄▀  ▄▀  ▀▄ ▄▀   █  ▀▄     ▄▀  ▐▌      ▄▄▀
   ▀▀▀▀▀       ▀▀▀▀▀▀▀   ▀▀▀▀▀▀  ▀▀▀▀     ▀▀▀▀▀     ▀▀▀▀▀▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀▀▀  ▀▀▀▀     ▀▀▀▀▀     ▀▀▀▀▀▀▀    )
"""

OPCOES = ["Jogar", "Como jogar", "Sair"]

def desenhar_menu(selecionada):
    os.system("cls")

    for linha in TITULO.splitlines():
        print(VERDE + linha + BRANCO)
    print()

    for i, texto in enumerate(OPCOES):
        if i == selecionada:
            print(VERMELHO + f"> {i+1} - {texto}" + BRANCO)
        else:
            print(CINZA + f" {i+1} - {texto}" + BRANCO)

    print(AZUL + f"W/S: mover   E: confirmar   1-{len(OPCOES)}: escolher direto" + BRANCO)


def ler_tecla():
    codigo, letra = WConio2.getch()
    return letra.lower()

COMO_JOGAR = [
    ("NO MAPA", [
        "W A S D: Mover o personagem.",
        "E: Interagir e confirmar.",
        "F: Quebrar as rochas.",
        "I: Abrir o inventário.",
    ]),
    ("OBJETIVO DE CADA SALA", [
        "Abra todos os baús (▣) e derrote os inimigos (☠) para abrir a porta (❂).",
        "Salas 3, 6 e 9: vença o mini chefe (☢) para abrir o baú e a porta.",
        "Em cada sala nova o grupo descansa: +25% de HP/MP e os caídos voltam.",
        "Na sala 10 espera o chefe final (☣).",
    ]),
    ("NO COMBATE", [
        "W / S: Mover a seleção.",
        "E: Confirmar.",
        "0: Voltar.",
        "1, 2, 3...: Escolher a opção direto pelo número.",
        "Atacar: Pode errar o golpe.",
        "Habilidade: Sempre acerta, mas gasta MP ou HP.",
        "Item: Usa um item do inventário.",
        "Defesa: Reduz o dano recebido em porcentagem.",
        "Hydra: Derrube as 3 cabeças; uma cabeça caída renasce se demorar.",
    ]),
]

def mostrar_como_jogar():
    os.system("cls")
    print(VERDE + "COMO JOGAR" + BRANCO)
    for titulo, linhas in COMO_JOGAR:
        print()
        print(AMARELO + titulo + BRANCO)
        for linha in linhas:
            print("  " + linha)
    print()
    print(CINZA + "(pressione qualquer tecla para voltar)" + BRANCO)
    WConio2.getch()

def menu_principal():
    selecionada = 0          # índice da opção destacada

    while True:
        desenhar_menu(selecionada)
        tecla = ler_tecla()

        escolha = None       # continua None se a tecla não confirmou nada

        if tecla == "w":
            selecionada = (selecionada - 1) % len(OPCOES)
        elif tecla == "s":
            selecionada = (selecionada + 1) % len(OPCOES)
        elif tecla == "e":
            escolha = OPCOES[selecionada]
        elif tecla.isdecimal() and 1 <= int(tecla) <= len(OPCOES):
            escolha = OPCOES[int(tecla) - 1]

        if escolha == "Como jogar":
            mostrar_como_jogar()                  # mostra a tela e volta para o menu
            continue

        if escolha is not None:
            return escolha

ROTULOS_ATRIBUTO = {
    "ataque": "ATQ",
    "defesa": "DEF",
    "max_hp": "HP máx",
    "max_mp": "MP máx",
}

def escolher_membro(candidatos, item):
    selecionado = 0

    while True:
        os.system("cls")
        print(AMARELO + f"Quem vai equipar {item['nome']}?" + BRANCO)
        print()

        for i, membro in enumerate(candidatos):
            mudancas = []
            for atributo, valor in item["bonus"].items():
                atual = getattr(membro, atributo)
                mudancas.append(f"{ROTULOS_ATRIBUTO[atributo]} {atual} -> {atual + valor}")
            texto = f"{i + 1} - {membro.nome} ({membro.classe}): " + ", ".join(mudancas)

            if i == selecionado:
                print(VERDE + "> " + texto + BRANCO)
            else:
                print(AZUL + "  " + texto + BRANCO)

        print()
        print(CINZA + "W/S: mover   E: confirmar   1-" + str(len(candidatos)) + ": escolher direto" + BRANCO)

        tecla = ler_tecla()

        if tecla == "w":
            selecionado = (selecionado - 1) % len(candidatos)
        elif tecla == "s":
            selecionado = (selecionado + 1) % len(candidatos)
        elif tecla == "e":
            os.system("cls")
            return candidatos[selecionado]
        elif tecla.isdecimal() and 1 <= int(tecla) <= len(candidatos):
            os.system("cls")
            return candidatos[int(tecla) - 1]



if __name__ == "__main__":
    escolha = menu_principal()
    os.system("cls")
    print("Você escolheu:", escolha)    # esperado: "Jogar" ou "Sair"
