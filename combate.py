import os
import random

from personagens import party_derrotada
from menu import ler_tecla, CINZA, BRANCO
from cenarioCombate import desenhar_combate
from itens import agrupar, alvos_do_item, usar_item


#lista vazia e ordenada com a velcidade
def vivos(lista):
    return [c for c in lista if c.vivo_morto()]


def ordenar_por_velocidade(lista):
    fila = [c for c in lista if c.vivo_morto()]
    fila.sort(key=lambda c: (c.velocidade, random.random()), reverse=True)
    return fila


def montar_fila(party, inimigos, party_primeiro=False):
    if party_primeiro:
        # 1ª rodada: a party age primeiro (do mais rápido ao mais lento),
        # depois os inimigos. Assim o combate nunca começa com um ataque inimigo.
        return ordenar_por_velocidade(party) + ordenar_por_velocidade(inimigos)
    return ordenar_por_velocidade(party + inimigos)


def pausa():
    print(CINZA + "(pressione qualquer tecla)" + BRANCO)
    ler_tecla()



# O menu aparece dentro da caixa de comandos da tela de combate

def escolher_opcao(titulo, opcoes, ctx, podeVoltar=True):
    sel = 0
    ajuda = f"W/S: mover   E: confirmar   1-{len(opcoes)}: escolher direto"
    if podeVoltar:
        ajuda += "   0: voltar"

    while True:
        desenhar_combate(**ctx, titulo=titulo, opcoes=opcoes, selecionada=sel, ajuda=ajuda)
        tecla = ler_tecla()

        if tecla == "w":
            sel = (sel - 1) % len(opcoes)
        elif tecla == "s":
            sel = (sel + 1) % len(opcoes)
        elif tecla == "e":
            return sel
        elif tecla.isdecimal():
            n = int(tecla)
            if n == 0 and podeVoltar:
                return None
            if 1 <= n <= len(opcoes):
                return n - 1


#funções de ataque aqui
def escolher_alvo(inimigos, ctx):
    alvos = vivos(inimigos)
    if len(alvos) == 1:
        return alvos[0]
    i = escolher_opcao("Escolha o alvo:", [f"{e.nome} (HP {e.hp})" for e in alvos], ctx)
    return None if i is None else alvos[i]


def acao_atacar(membro, inimigos, ctx):
    alvo = escolher_alvo(inimigos, ctx)
    if alvo is None:
        return False
    desenhar_combate(**ctx, titulo=f"{membro.nome} ataca!")
    print()
    membro.atacar(alvo)                                  # usa calculo_dano do personagens.py
    return True


def custo_texto(hab):
    partes = []
    if hab.get("custo_mp", 0) > 0:
        partes.append(f"MP {hab['custo_mp']}")
    if hab.get("custo_hp", 0) > 0:
        partes.append(f"HP {hab['custo_hp']}")
    return " + ".join(partes) or "grátis"


def tipo_alvo(hab):
    if hab.get("area"):
        return "area"                                    # atinge todos os inimigos de uma vez
    if "alvo" in hab:
        return hab["alvo"]
    return "inimigo" if hab.get("dano", 0) > 0 else "si"


def acao_habilidade(membro, party, inimigos, ctx):
    nomes = [f"{h['nome'].strip()} ({custo_texto(h)})" for h in membro.habilidades]
    i = escolher_opcao("Habilidades:", nomes, ctx)
    if i is None:
        return False
    hab = membro.habilidades[i]

    if not membro.pode_usar(hab):
        desenhar_combate(**ctx, titulo="Sem recursos!")
        print(f"\n{membro.nome} não tem recursos para usar {hab['nome'].strip()}!")
        pausa()
        return False

    tipo = tipo_alvo(hab)
    if tipo == "area":
        alvo = vivos(inimigos)
    elif tipo == "inimigo":
        alvo = escolher_alvo(inimigos, ctx)
    elif tipo == "aliado":
        aliados = vivos(party)
        j = escolher_opcao("Escolha o aliado:", [f"{m.nome} (HP {m.hp}/{m.max_hp})" for m in aliados], ctx)
        alvo = None if j is None else aliados[j]
    else:                                                # "si" ou "party"
        alvo = membro
    if alvo is None:
        return False

    desenhar_combate(**ctx, titulo=f"{membro.nome} usa {hab['nome'].strip()}!")
    print()
    membro.usar_habilidade(hab, alvo, party)
    return True


def acao_item(membro, party, inventario, ctx):
    grupos = agrupar(inventario)
    if not grupos:
        desenhar_combate(**ctx, titulo="Sem itens!")
        print("\nO inventário está vazio.")
        pausa()
        return False

    i = escolher_opcao("Itens:", [f"{nome} x{qtd}" for nome, qtd, _ in grupos], ctx)
    if i is None:
        return False
    item = grupos[i][2]

    candidatos = alvos_do_item(item, party)
    if not candidatos:
        desenhar_combate(**ctx, titulo="Sem efeito!")
        print(f"\nNinguém precisa de {item['nome']} agora.")
        pausa()
        return False

    if len(candidatos) == 1:
        alvo = candidatos[0]
    else:
        j = escolher_opcao("Usar em quem?", [f"{m.nome} (HP {m.hp}/{m.max_hp})" for m in candidatos], ctx)
        if j is None:
            return False
        alvo = candidatos[j]

    desenhar_combate(**ctx, titulo=f"{membro.nome} usa {item['nome']}!")
    print()
    print(usar_item(inventario, item, alvo))
    return True


def turno_jogador(membro, party, inimigos, rodada, fila, inventario):
    ctx = dict(party=party, inimigos=inimigos, rodada=rodada, fila=fila, atual=membro)
    while True:
        i = escolher_opcao(f"Vez de {membro.nome}", ["Atacar", "Habilidade", "Item"], ctx, podeVoltar=False)
        if i == 0:
            feito = acao_atacar(membro, inimigos, ctx)
        elif i == 1:
            feito = acao_habilidade(membro, party, inimigos, ctx)
        else:
            feito = acao_item(membro, party, inventario, ctx)
        if feito:
            return


def escolher_acao_inimigo(inimigo, inimigos):
    """Devolve a habilidade que o inimigo vai usar, ou None para um ataque normal."""
    opcoes = []
    for h in inimigo.habilidades:
        if not inimigo.pode_usar(h):
            continue
        if len(vivos(inimigos)) < h.get("requer_vivos", 0):
            continue                                     # ex.: Três Cabeças em Fúria precisa das 3 cabeças vivas
        so_cura = (h.get("cura", 0) > 0 or h.get("cura_pct", 0) > 0) and not h.get("dano")
        so_buff = h.get("bonus_defesa", 0) > 0 and not h.get("dano")
        if so_cura and inimigo.hp > inimigo.max_hp * 0.6:
            continue                                     # só se cura quando está ferido
        if so_buff and inimigo.defesa_bonus_turnos > 0:
            continue                                     # não empilha o mesmo buff
        opcoes.append(h)

    if opcoes and random.random() < 0.6:                 # 60% de chance de usar habilidade
        return random.choice(opcoes)
    return None


def turno_inimigo(inimigo, party, inimigos, rodada, fila):
    ctx = dict(party=party, inimigos=inimigos, rodada=rodada, fila=fila, atual=inimigo)
    alvo = random.choice(vivos(party))
    hab = escolher_acao_inimigo(inimigo, inimigos)
    if hab is not None and hab.get("area"):
        alvo = vivos(party)                              # habilidade em área: atinge todos os heróis

    if hab is None:
        desenhar_combate(**ctx, titulo=f"{inimigo.nome} ataca {alvo.nome}!")
        print()
        inimigo.atacar(alvo)
    else:
        desenhar_combate(**ctx, titulo=f"{inimigo.nome} usa {hab['nome'].strip()}!")
        print()
        inimigo.usar_habilidade(hab, alvo, inimigos)


def nomear_duplicados(inimigos):
    """Dois inimigos iguais viram 'Nome A' e 'Nome B' para o jogador diferenciar."""
    contagem = {}
    for e in inimigos:
        contagem[e.nome] = contagem.get(e.nome, 0) + 1
    usados = {}
    for e in inimigos:
        base = e.nome
        if contagem[base] > 1:
            usados[base] = usados.get(base, 0) + 1
            e.nome = f"{base} {'ABCDEF'[usados[base] - 1]}"



#  True = venceu, False = party derrotada

def iniciar_combate(party, inimigos, inventario=None):
    if inventario is None:
        inventario = []                                  # sem inventário: a opção Item só avisa que está vazio
    nomear_duplicados(inimigos)
    rodada = 1

#usei as listas vazias para fazer a fila de turnos tb
    while True:
        fila = montar_fila(party, inimigos, party_primeiro=(rodada == 1))   # refaz a ordem a cada rodada

        for c in fila:
            if not c.vivo_morto():
                continue
            if party_derrotada(party) or not vivos(inimigos):
                break

            if c in party:
                turno_jogador(c, party, inimigos, rodada, fila, inventario)
            else:
                turno_inimigo(c, party, inimigos, rodada, fila)

            c.fim_turno()                                # reduz duração dos buffs
            pausa()

        if party_derrotada(party):
            venceu = False
            break
        if not vivos(inimigos):
            venceu = True
            break

        # fim da rodada: cabeças derrubadas contam para renascer
        for e in inimigos:
            if e.passar_rodada():
                desenhar_combate(party, inimigos, rodada, fila, titulo=f"{e.nome} renasce!")
                print()
                print(f"{e.nome} regenera e volta à luta com {e.hp} de HP!")
                pausa()
        rodada += 1

    for m in party:
        m.fim_combate()
    os.system("cls")
    return venceu