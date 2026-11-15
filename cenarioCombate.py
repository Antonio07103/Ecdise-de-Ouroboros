import os
import textwrap
import menu

from menu import AMARELO, VERDE, VERMELHO, AZUL, CINZA, BRANCO

W_INIM = 34
W_PARTY = 20
W_STATUS = 22
W_TOTAL = W_INIM + W_PARTY + W_STATUS     
H_TOPO = 12
H_BAIXO = 8
H_TOTAL = H_TOPO + H_BAIXO
SIMBOLO_CAIDO = "✝"                       


# tela = matriz de caracteres
# tela = matriz de caracteres, começa cheia de espaços e vai sendo preenchida
def _novo():
    return [[" "] * W_TOTAL for _ in range(H_TOTAL)]


def _texto(c, x, y, txt, cor=""):
    for i, ch in enumerate(txt):
        xx = x + i
        if 0 <= y < H_TOTAL and 0 <= xx < W_TOTAL:
            c[y][xx] = (cor + ch + BRANCO) if cor else ch


def _caixa(c, x, y, w, h, titulo=""):
    _texto(c, x, y, "╔" + "═" * (w - 2) + "╗")
    for k in range(1, h - 1):
        _texto(c, x, y + k, "║")
        _texto(c, x + w - 1, y + k, "║")
    _texto(c, x, y + h - 1, "╚" + "═" * (w - 2) + "╝")
    if titulo:
        _texto(c, x + 2, y, f" {titulo} ")


def _sprites(c, lista, x0, largura, cor, atual, eh_party):
    n = len(lista)
    por_col = 3
    for k, p in enumerate(lista):
        col, idx = divmod(k, por_col)
        qtd = min(por_col, n - col * por_col)
        passo = (H_TOPO - 2) // (qtd + 1)
        y = passo * (idx + 1)
        if eh_party:
            x = x0 + largura // 2 + (2 if idx % 2 == 0 else -2)   # party meio escalonada
        else:
            x = x0 + 6 + 10 * col

        if not p.vivo_morto():
            if eh_party:
                _texto(c, x, y, SIMBOLO_CAIDO, CINZA)                        # herói caído
            continue                                               # inimigo derrotado some
        _texto(c, x, y, p.simbolo, AMARELO if p is atual else cor)



def desenhar_combate(party, inimigos, rodada, fila, atual=None,
                     titulo="", opcoes=None, selecionada=0, ajuda=""):
    os.system("cls")
    c = _novo()

    # pt de cima
    _caixa(c, 0, 0, W_INIM, H_TOPO, "Inimigos")
    _caixa(c, W_INIM, 0, W_PARTY, H_TOPO, "Party")
    _sprites(c, inimigos, 0, W_INIM, VERMELHO, atual, eh_party=False)
    _sprites(c, party, W_INIM, W_PARTY, VERDE, atual, eh_party=True)

    # coluna da direita
    x_status = W_INIM + W_PARTY
    for k, m in enumerate(party):
        y = 4 * k
        _caixa(c, x_status, y, W_STATUS, 4)
        cor_nome = AMARELO if m is atual else (VERDE if m.vivo_morto() else CINZA)
        _texto(c, x_status + 2, y + 1, m.nome[:W_STATUS - 4], cor_nome)
        if m.vivo_morto():
            linha = f"HP {m.hp}/{m.max_hp} MP {m.mp}/{m.max_mp}"
        else:
            linha = f"HP 0/{m.max_hp} (caído)"
        _texto(c, x_status + 2, y + 2, linha[:W_STATUS - 4])

    # caixa de baixo à esquerda: nome e HP dos inimigos (nome inteiro, HP embaixo)
    _caixa(c, 0, H_TOPO, W_INIM, H_BAIXO)
    linha = H_TOPO + 1
    for e in inimigos[:3]:
        if e.vivo_morto():
            _texto(c, 2, linha, f"{e.simbolo} {e.nome[:W_INIM - 6]}", VERMELHO)
            _texto(c, 4, linha + 1, f"HP {e.hp}/{e.max_hp}", VERMELHO)
        else:
            _texto(c, 2, linha, f"{SIMBOLO_CAIDO} {e.nome[:16]} (derrotado)", CINZA)
        linha += 2

    # caixa de baixo à direita: menu de comandos com cursor
    x_menu = W_INIM
    _caixa(c, x_menu, H_TOPO, W_TOTAL - W_INIM, H_BAIXO)
    largura_menu = W_TOTAL - W_INIM - 6
    linhas_titulo = textwrap.wrap(titulo, largura_menu + 2)[:2] if titulo else []   # títulos longos quebram em 2 linhas
    for k, linha_titulo in enumerate(linhas_titulo):
        _texto(c, x_menu + 2, H_TOPO + 1 + k, linha_titulo, AMARELO)
    if opcoes:
        visiveis = (H_BAIXO - 2) - len(linhas_titulo)
        inicio = max(0, selecionada - (visiveis - 1))
        for k, i in enumerate(range(inicio, min(len(opcoes), inicio + visiveis))):
            texto = f"{i + 1} - {opcoes[i]}"[:largura_menu]
            y = H_TOPO + 1 + len(linhas_titulo) + k
            if i == selecionada:
                _texto(c, x_menu + 2, y, "> " + texto, VERMELHO)
            else:
                _texto(c, x_menu + 2, y, "  " + texto, CINZA)

    print(AMARELO + f"=== COMBATE - Rodada {rodada} ===" + BRANCO)
    for linha in c:
        print("".join(linha))
    print(AZUL + "Ordem: " + " > ".join(x.nome for x in fila if x.vivo_morto()) + BRANCO)
    if ajuda:
        print(CINZA + ajuda + BRANCO)
    print()

#caso precise de teste deixei um teste aqui para ver só a tela, só tirar do comentado!
# Teste visual: python cenario_combate.py
'''if __name__ == "__main__":
    from personagens import criar_party, adicionar_membro, Personagem

    party = criar_party()
    adicionar_membro(party, "Astrólogo")
    adicionar_membro(party, "Ninja")
    inimigos = [Personagem("Sombra", "Inimigo", 20, 0, 10, 0, 4, "☠") for _ in range(2)]
    desenhar_combate(party, inimigos, 1, party + inimigos, atual=party[0],
                     titulo="Vez de Alucard", opcoes=["Atacar", "Habilidade"], selecionada=0,
                     ajuda="W/S: mover   E: confirmar   1-2: escolher direto")'''