import random

from personagens import adicionar_membro

QTD_BAUS_FASE = 7

ATRIBUTOS_EQUIPAMENTO = ("ataque", "defesa", "max_hp", "max_mp")

def fase_da_sala(sala):
    return(sala - 1) // 3 + 1


#Habilidades coletadas em baús

#Habilidades do Cavaleiro Sombrio

GOLPE_IMPIEDOSO = {
    "nome": "Golpe Impiedoso",
    "classe": "Cavaleiro Sombrio",
    "custo_mp": 5,
    "alvo": "inimigo",
    "dano": 12,
    "mensagem": "{nome} concentra toda a sua raiva em um único golpe!",
}

CORACAO_NEGRO = {
    "nome": "Coração Negro",
    "classe": "Cavaleiro Sombrio",
    "alvo": "si",
    "custo_mp": 5,
    "bonus_defesa": 5,
    "duracao_defesa": 2,
    "mensagem": "{nome} liberta as sombras profundas de seu coração!",
}

PACTO_DA_AGONIA = {
    "nome": "Pacto da Agonia",
    "classe": "Cavaleiro Sombrio",
    "alvo": "inimigo",
    "custo_hp": 12,
    "dano": 27,
    "mensagem": "{nome} sela um pacto de agonia com as sombras!",
}

MANTO_CREPUSCULAR = {
    "nome": "Manto Crepuscular",
    "classe": "Cavaleiro Sombrio",
    "alvo": "party",
    "custo_mp": 9,
    "bonus_defesa": 3,
    "duracao_defesa": 3,
    "buff_party": True,
    "mensagem": "{nome} estende sua escuridão para encobrir seus aliados da luz!",
}

#Habilidades do Astrólogo

ESTRELA_CADENTE = {
    "nome": "Estrela Cadente",
    "classe": "Astrólogo",
    "alvo": "inimigo",
    "custo_mp": 5,
    "dano": 11,
    "mensagem": "{nome} faz uma estrela despencar do céu!",
}

BENCAO_LUNAR = {
    "nome": "Bênção Lunar",
    "classe": "Astrólogo",
    "alvo": "aliado",
    "custo_mp": 6,
    "cura": 25,
    "cura_alvo": True,
    "mensagem": "{nome} invoca a benção da lua!",
}

ECLIPSE = {
    "nome": "Eclipse",
    "classe": "Astrólogo",
    "area": True,                         # atinge todos os inimigos
    "custo_mp": 8,
    "dano": 8,
    "debuff_defesa": 4,
    "duracao_defesa": 3,
    "mensagem": "{nome} sobrepõe a lua ao sol e deixa os inimigos no escuro!",
}

MARE_DE_MANA = {
    "nome": "Maré de Mana",
    "classe": "Astrólogo",
    "alvo": "party",
    "custo_mp": 10,
    "restaura_mp": 10,
    "buff_party": True,
    "mensagem": "{nome} faz a energia dos astros fluir entre os aliados!",
}

#Habilidades do Ninja

SHURIKEN_RELAMPAGO = {
    "nome": "Shuriken Relâmpago",
    "classe": "Ninja",
    "alvo": "inimigo",
    "custo_mp": 4,
    "dano": 9,
    "mensagem": "{nome} arremessa uma shuriken veloz como um raio!",
}

PASSO_DO_VENTO = {
    "nome": "Passo do Vento",
    "classe": "Ninja",
    "alvo": "si",
    "custo_mp": 5,
    "cura": 8,
    "bonus_velocidade": 4,
    "duracao_bonus": 3,
    "mensagem": "{nome} se transforma em um com o vento!",
}

LAMINAS_GEMEAS = {
    "nome": "Lâminas Gêmeas",
    "classe": "Ninja",
    "alvo": "inimigo",
    "custo_mp": 7,
    "dano": 8,
    "golpes": 2,
    "mensagem": "{nome} corta duas vezes antes que o inimigo perceba!",
}

MIL_LAMINAS_DA_MORTE = {
    "nome": "Mil Lâminas da Morte",
    "classe": "Ninja",
    "custo_mp": 13,                       # MP mínimo para usar...
    "gasta_todo_mp": True,                # ...e ela gasta TODO o MP que o Ninja tiver
    "golpes_aleatorios": True,            # cada golpe cai num inimigo vivo sorteado
    "dano": 6,
    "faixas_golpes": [(13, 4), (16, 6), (20, 8)],   # (MP que tinha, golpes): mais MP, mais golpes
    "mensagem": "{nome} desaparece e mil lâminas surgem das sombras!",
}

#Habilidades ganhas por cada fase

HABILIDADES_POR_FASE = {
    1: [GOLPE_IMPIEDOSO, CORACAO_NEGRO],
    2: [PACTO_DA_AGONIA, MANTO_CREPUSCULAR, ESTRELA_CADENTE, BENCAO_LUNAR],
    3: [ECLIPSE, MARE_DE_MANA, SHURIKEN_RELAMPAGO, PASSO_DO_VENTO, LAMINAS_GEMEAS],
}

#Itens: Consumiveis e equipamentos

ITENS = [
    #Consumiveis
    {"nome": "Extrato de Serpente", "tipo": "consumivel", "efeito": "cura", "valor": 15, "peso": 40, "fases": [1, 2]},
    {"nome": "Extrato Refinado de Serpente", "tipo": "consumivel", "efeito": "cura", "valor": 30, "peso": 30, "fases": [2, 3]},
    {"nome": "Veneno da Vida", "tipo": "consumivel", "efeito": "revive", "valor": 50, "peso": 5, "fases": [2, 3]},

    #Equipamentos iniciais
    {"nome": "Fragmento de Força", "tipo": "equipamento", "bonus": {"ataque": 2}, "peso": 15, "fases": [1]},
    {"nome": "Fragmento de Perseverança", "tipo": "equipamento", "bonus": {"defesa": 2}, "peso": 15, "fases": [1]},
    {"nome": "Fragmento de Vitalidade", "tipo": "equipamento", "bonus": {"max_hp": 5}, "peso": 12, "fases": [1, 2]},
    {"nome": "Fragmento de Sabedoria", "tipo": "equipamento", "bonus": {"max_mp": 5}, "peso": 12, "fases": [1, 2]},

    #Equipamentos finais
    {"nome": "Memória da Força", "tipo": "equipamento", "bonus": {"ataque": 3}, "peso": 15, "fases": [2, 3]},
    {"nome": "Memória da Perseverança", "tipo": "equipamento", "bonus": {"defesa": 3}, "peso": 15, "fases": [2, 3]},
    {"nome": "Memória da Vitalidade", "tipo": "equipamento", "bonus": {"max_hp": 8}, "peso": 10, "fases": [2, 3]},
    {"nome": "Memória da Sabedoria", "tipo": "equipamento", "bonus": {"max_mp": 8}, "peso": 10, "fases": [2, 3]}
]

#Armas lendárias que recebem no mini boss da sala 9
EQUIPAMENTOS_LENDARIOS = [
    {"nome": "Lâmina do Pregresso", "tipo": "equipamento", "classe": "Cavaleiro Sombrio", "bonus": {"ataque": 5, "defesa": 3}},
    {"nome": "Cetro do Mercúrio Retrógado", "tipo": "equipamento", "classe": "Astrólogo", "bonus": {"ataque": 4, "max_mp": 15 }},
    {"nome": "Izanagi e Izanami", "tipo": "equipamento", "classe": "Ninja", "bonus": {"ataque": 6, "max_hp": 5}},
]

#Recompensa de cada mini boss
RECOMPENSAS_MINIBOSS = {
    3: {"recruta": "Astrólogo"},
    6: {"recruta": "Ninja"},
    9: {"habilidades": [MIL_LAMINAS_DA_MORTE],
        "equipamentos": EQUIPAMENTOS_LENDARIOS},
}

#Baús de cada fase

def itens_da_fase(fase):
    return[item for item in ITENS if fase in item.get("fases", (1, 2, 3))]

def preparar_fase(fase):
    habilidades = HABILIDADES_POR_FASE.get(fase)
    if habilidades is None:
        return[]

    if len(habilidades) > QTD_BAUS_FASE:
        raise ValueError(f"A fase {fase} tem {len(habilidades)} habilidades," f"mas só {QTD_BAUS_FASE} baús. ")

    conteudos = []
    for habilidade in habilidades:
        conteudos.append({"tipo": "habilidade", "dados": habilidade})

    if len(conteudos) < QTD_BAUS_FASE:
        candidatos = itens_da_fase(fase)
        if not candidatos:
            raise ValueError(f"Nenhum item disponível na fase {fase}.")
        pesos = [item["peso"] for item in candidatos]

        while len(conteudos) < QTD_BAUS_FASE:
            item = random.choices(candidatos, weights = pesos)[0]
            conteudos.append({"tipo": item["tipo"], "dados": dict(item)})

    random.shuffle(conteudos)
    return conteudos

#Entregar o conteúdo

def achar_membro(party, classe):
    for membro in party:
        if membro.classe == classe:
            return membro
    return None

def aplicar_equipamento(membro, equipamento):
    textos = []
    for atributo, valor in equipamento["bonus"].items():
        if atributo not in ATRIBUTOS_EQUIPAMENTO:
            raise ValueError(f"O equipamento {equipamento['nome']} usa um atributo inválido: {atributo}")

        setattr(membro, atributo, getattr(membro, atributo) + valor)

        if atributo == "max_hp":
            membro.hp += valor
        elif atributo == "max_mp":
            membro.mp += valor

        textos.append(f"+{valor} {atributo.replace('max_', 'máx. ')}")
    return ", ".join(textos)

def entregar_conteudo(party, bau, inventario, escolher=None):
    tipo = bau["tipo"]
    dados = bau["dados"]

    if tipo == "habilidade":
        membro = achar_membro(party, dados["classe"])
        if membro is None:
            return f"{dados['nome']} brilha, mas ninguém na party pode aprendê-la."
        if dados in membro.habilidades:
            return f"{membro.nome} já conhecia {dados['nome']}."
        membro.aprender_habilidade(dados)
        return f"{membro.nome} aprendeu {dados['nome']}!"

    elif tipo == "equipamento":
        if "classe" in dados:
            membro = achar_membro(party, dados["classe"])
        else:
            vivos = [m for m in party if m.vivo_morto()]
            if not vivos:
                membro = None
            elif len(vivos) == 1 or escolher is None:
                membro = vivos[0] if len(vivos) == 1 else random.choice(vivos)
            else:
                membro = escolher(vivos, dados)
        if membro is None:
            return f"{dados['nome']} não dono na party."
        efeito = aplicar_equipamento(membro, dados)
        return f"{membro.nome} equipou {dados['nome']}! ({efeito})"

    elif tipo == "consumivel":
        inventario.append(dados)
        return f"Encontrou {dados['nome']}!"

    return "O baú estava vazio."

#Recompensas mini boss

def recompensa_miniboss(sala, party, inventario):
    recompensa = RECOMPENSAS_MINIBOSS.get(sala)
    if recompensa is None:
        return ""

    mensagens = []

    classe = recompensa.get("recruta")
    if classe:
        if adicionar_membro(party, classe):
            mensagens.append(f"{classe} se juntou à party!")

    for habilidade in recompensa.get("habilidades", []):
        mensagens.append(entregar_conteudo(party, {"tipo": "habilidade", "dados": habilidade}, inventario))

    for equipamento in recompensa.get("equipamentos", []):
        mensagens.append(entregar_conteudo(party, {"tipo": "equipamento", "dados": equipamento}, inventario))

    return "\n".join(mensagens)
