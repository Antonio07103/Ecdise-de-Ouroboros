# ============================================================
#  ITENS CONSUMÍVEIS
#  Usados no combate (opção "Item") e fora dele (tecla I no mapa).
#
#  Um consumível é um dicionário do baus.py, por exemplo:
#    {"nome": "Extrato de Serpente", "tipo": "consumivel", "efeito": "cura",   "valor": 15}
#    {"nome": "Veneno da Vida",      "tipo": "consumivel", "efeito": "revive", "valor": 50}
#
#  efeito "cura"   -> valor = pontos de HP recuperados
#  efeito "revive" -> valor = % da vida máxima com que o aliado volta
#
#  Para criar um efeito novo (ex.: restaurar MP), mexa só em
#  alvos_do_item() e aplicar_consumivel().
# ============================================================

import os

from menu import ler_tecla, AMARELO, VERMELHO, AZUL, CINZA, BRANCO


# ------------------------------------------------------------
# REGRAS (usadas pelo combate e pelo mapa)
# ------------------------------------------------------------

def agrupar(inventario):
    """Junta os iguais: [(nome, quantidade, item), ...] na ordem em que apareceram."""
    grupos = {}
    for item in inventario:
        if item["nome"] in grupos:
            grupos[item["nome"]][0] += 1
        else:
            grupos[item["nome"]] = [1, item]
    return [(nome, qtd, item) for nome, (qtd, item) in grupos.items()]


def alvos_do_item(item, party):
    """Quem pode receber o item agora (lista vazia = o item não serviria para ninguém)."""
    efeito = item["efeito"]
    if efeito == "cura":
        return [m for m in party if m.vivo_morto() and m.hp < m.max_hp]
    if efeito == "revive":
        return [m for m in party if not m.vivo_morto()]
    return []


def aplicar_consumivel(item, alvo):
    """Aplica o efeito e devolve o texto para mostrar. Não mexe no inventário."""
    efeito = item["efeito"]
    if efeito == "cura":
        recuperado = alvo.curar(item["valor"])
        return f"{alvo.nome} recuperou {recuperado} de HP!"
    if efeito == "revive":
        vida = max(1, alvo.max_hp * item["valor"] // 100)
        recuperado = alvo.curar(vida)          # o curar() já funciona com HP 0
        return f"{alvo.nome} voltou à vida com {recuperado} de HP!"
    raise ValueError(f"O item {item['nome']} tem um efeito desconhecido: {efeito}")


def usar_item(inventario, item, alvo):
    """Usa 1 unidade: aplica o efeito, tira do inventário e devolve o texto."""
    texto = aplicar_consumivel(item, alvo)
    inventario.remove(item)                    # remove só UMA unidade (a primeira igual)
    return texto


# ------------------------------------------------------------
# TELA DO INVENTÁRIO (fora do combate)
# ------------------------------------------------------------

def _escolher(titulo, opcoes, ajuda, topo=()):
    """Menu simples: devolve o índice escolhido, ou None se o jogador voltar."""
    sel = 0
    while True:
        os.system("cls")
        print(AMARELO + titulo + BRANCO)
        for linha in topo:
            print(linha)
        print()
        for i, texto in enumerate(opcoes):
            if i == sel:
                print(VERMELHO + f"> {i + 1} - {texto}" + BRANCO)
            else:
                print(CINZA + f"  {i + 1} - {texto}" + BRANCO)
        print()
        print(AZUL + ajuda + BRANCO)

        tecla = ler_tecla()
        if tecla == "w":
            sel = (sel - 1) % len(opcoes)
        elif tecla == "s":
            sel = (sel + 1) % len(opcoes)
        elif tecla == "e":
            return sel
        elif tecla in ("0", "i"):
            return None
        elif tecla.isdecimal() and 1 <= int(tecla) <= len(opcoes):
            return int(tecla) - 1


def _linha_membro(m):
    if m.vivo_morto():
        return f"{m.nome}: HP {m.hp}/{m.max_hp}  MP {m.mp}/{m.max_mp}"
    return f"{m.nome}: caído (HP 0/{m.max_hp})"


def usar_inventario(party, inventario):
    """Abre o inventário no mapa. Fica aberto até o jogador sair (0 ou I)."""
    aviso = ""
    while True:
        grupos = agrupar(inventario)
        if not grupos:
            os.system("cls")
            if aviso:
                print(aviso)
                print()
            print("Inventário vazio.")
            print(CINZA + "(pressione qualquer tecla)" + BRANCO)
            ler_tecla()
            return

        topo = [CINZA + _linha_membro(m) + BRANCO for m in party]
        if aviso:
            topo += ["", aviso]

        ajuda = "W/S: mover   E: usar   1-" + str(len(grupos)) + ": escolher direto   0 ou I: sair"
        i = _escolher("=== INVENTÁRIO ===", [f"{nome} x{qtd}" for nome, qtd, _ in grupos], ajuda, topo)
        if i is None:
            return
        item = grupos[i][2]

        candidatos = alvos_do_item(item, party)
        if not candidatos:
            aviso = f"Ninguém precisa de {item['nome']} agora."
            continue

        if len(candidatos) == 1:
            alvo = candidatos[0]
        else:
            nomes = [f"{m.nome} (HP {m.hp}/{m.max_hp})" for m in candidatos]
            j = _escolher(f"Usar {item['nome']} em quem?", nomes,
                          "W/S: mover   E: confirmar   0: voltar", topo)
            if j is None:
                aviso = ""
                continue
            alvo = candidatos[j]

        aviso = usar_item(inventario, item, alvo)



# ---------- descanso ao entrar numa sala nova ----------
RECUPERA_HP_PCT = 25        # % do HP máximo que cada herói vivo recupera
RECUPERA_MP_PCT = 25        # % do MP máximo
REVIVE_PCT = 25             # herói caído volta com esse % do HP máximo

def recuperar_party(party, hp_pct=RECUPERA_HP_PCT, mp_pct=RECUPERA_MP_PCT, revive_pct=REVIVE_PCT):
    """Chamada ao passar para uma sala nova. Devolve um texto para mostrar ao jogador."""
    voltaram = []
    for m in party:
        if not m.vivo_morto():
            if revive_pct <= 0:
                continue
            m.hp = max(1, m.max_hp * revive_pct // 100)
            voltaram.append(m.nome)
        else:
            m.curar(max(1, m.max_hp * hp_pct // 100))
        m.restaurar_mp(m.max_mp * mp_pct // 100)
    texto = f"Descanso: +{hp_pct}% HP e +{mp_pct}% MP."
    if voltaram:
        texto += " De volta: " + ", ".join(voltaram) + "."
    return texto
