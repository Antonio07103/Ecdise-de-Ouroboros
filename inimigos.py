import random

from personagens import Personagem, PRECISAO_PADRAO

#Habilidades dos inimigos

#Fase 1

LANCA_ESQUECIDA = {
    "nome": "Lança Esquecida",
    "custo_mp": 4,
    "dano": 4,
    "mensagem": "{nome} arremessa uma lança, sem lembrar por quem luta!",
}

MORDIDA_FAMINTA = {
    "nome": "Mordida Faminta",
    "custo_mp": 3,
    "dano": 2,
    "cura_pct": 10,                  # % do HP máximo
    "mensagem": "{nome} crava presas pequenas, mas famintas!",
}

ABRACO_AMALGAMADO = {
    "nome": "Abraço Amalgamado",
    "custo_mp": 5,
    "dano": 3,
    "debuff_defesa": 2,
    "duracao_defesa": 2,
    "mensagem": "{nome} envolve a vítima com braços que não são seus!",
}

#Fase 2

PO_DE_PESADELO = {
    "nome": "Pó de Pesadelo",
    "custo_mp": 6,
    "dano": 4,
    "debuff_defesa": 3,
    "duracao_defesa": 3,
    "mensagem": "{nome} sopra um pó que corrói a coragem!",
}

NECTAR_SOMBRIO = {
    "nome": "Néctar Sombrio",
    "custo_mp": 8,
    "cura_pct": 25,                  # % do HP máximo
    "mensagem": "{nome} sorve néctar de flores murchas!",
}

GARRAS_DA_FOME = {
    "nome": "Garras da Fome",
    "custo_mp": 5,
    "dano": 2,
    "golpes": 2,
    "mensagem": "{nome} ataca movido por uma fome que nunca passa!",
}

CROSTA_DE_GEADA = {
    "nome": "Crosta de Geada",
    "custo_mp": 6,
    "bonus_defesa": 3,
    "duracao_defesa": 3,
    "mensagem": "{nome} se cobre de gelo e de ódio!",
}

SUSSURRO_OBSESSIVO = {
    "nome": "Sussurro Obsessivo",
    "custo_mp": 6,
    "dano": 6,
    "mensagem": "{nome} sussurra uma lembrança que não larga a mente!",
}

#Fase 3

BAFORADA_ARDENTE = {
    "nome": "Baforada Ardente",
    "custo_mp": 7,
    "dano": 6,
    "mensagem": "{nome} cospe fogo com o rugido de quem sobreviveu!",
}

GOLPE_QUEBRA_ESCUDO = {
    "nome": "Golpe Quebra-Escudo",
    "custo_mp": 8,
    "dano": 4,
    "debuff_defesa": 4,
    "duracao_defesa": 3,
    "mensagem": "{nome} golpeia até a guarda rachar!",
}

JURAMENTO_PERSISTENTE = {
    "nome": "Juramento Persistente",
    "custo_mp": 8,
    "cura_pct": 25,                  # % do HP máximo
    "mensagem": "{nome} renova o juramento ao rei e a armadura se remenda!",
}

TRUQUE_SANGRENTO = {
    "nome": "Truque Sangrento",
    "custo_mp": 6,
    "dano": 7,
    "mensagem": "{nome} puxa um lenço do bolso: é uma lâmina!",
}

MASCARA_DO_RISO = {
    "nome": "Máscara do Riso",
    "custo_mp": 6,
    "bonus_defesa": 5,
    "duracao_defesa": 3,
    "mensagem": "{nome} esconde o rosto atrás de um sorriso de porcelana!",
}

#Minibosses

CAUDA_ESMAGADORA = {
    "nome": "Cauda Esmagadora",
    "custo_mp": 5,
    "dano": 12,
    "mensagem": "{nome} varre o chão com a cauda para proteger as crias!",
}

ESCAMAS_DO_NINHO = {
    "nome": "Escamas do Ninho",
    "custo_mp": 6,
    "bonus_defesa": 4,
    "duracao_defesa": 3,
    "mensagem": "{nome} eriça as escamas ao redor do ninho!",
}

SOPRO_DO_FIM = {
    "nome": "Sopro do Fim",
    "custo_mp": 6,
    "dano": 12,
    "cura_pct": 10,                  # % do HP máximo
    "mensagem": "{nome} puxa o último fôlego de sua vítima!",
}

REQUIEM = {
    "nome": "Réquiem",
    "custo_mp": 7,
    "dano": 9,
    "debuff_defesa": 4,
    "duracao_defesa": 3,
    "area": True,                         # atinge todos os heróis
    "mensagem": "{nome} entoa um réquiem para todos que partiram!",
}

LAMINA_DA_COROA_PARTIDA = {
    "nome": "Lâmina da Coroa Partida",
    "custo_mp": 8,
    "dano": 9,
    "golpes": 2,
    "mensagem": "{nome} corta duas vezes com a espada da coroa partida!",
}

TRIBUTO_AO_TRONO = {
    "nome": "Tributo ao Trono",
    "custo_mp": 10,
    "dano": 16,
    "cura_pct": 10,                  # % do HP máximo
    "mensagem": "{nome} cobra o tributo devido ao trono: a vida de um herói!",
}

#Boss

GARRA_DE_LEAO = {
    "nome": "Garra de Leão",
    "custo_mp": 6,
    "dano": 8,
    "mensagem": "{nome} rasga o ar com as garras do leão!",
}

CABECA_REGENERADA = {
    "nome": "Cabeça Regenerada",
    "custo_mp": 8,
    "dano": 6,
    "cura_pct": 10,                  # % do HP máximo
    "mensagem": "{nome} devora um herói e sente a carne se refazer!",
}

VENENO_DO_CICLO = {
    "nome": "Veneno do Ciclo",
    "custo_mp": 8,
    "dano": 5,
    "debuff_defesa": 5,
    "duracao_defesa": 3,
    "mensagem": "{nome} injeta o veneno da serpente: todo fim volta ao começo!",
}

ECDISE = {
    "nome": "Ecdise",
    "custo_mp": 8,
    "bonus_defesa": 6,
    "duracao_defesa": 3,
    "mensagem": "{nome} troca de pele e renasce mais resistente!",
}

TRES_CABECAS_EM_FURIA = {
    "nome": "Três Cabeças em Fúria",
    "custo_mp": 12,
    "dano": 4,
    "golpes": 3,
    "requer_vivos": 3,                    # só pode usar se as 3 cabeças estiverem vivas
    "mensagem": "{nome} ruge e as três cabeças atacam de uma vez!",
}

#Cabeças da Hydra: depois de derrotada, a cabeça renasce se as outras ainda estiverem vivas
REGENERA_RODADAS = 5        # rodadas até a cabeça renascer (contando a rodada em que caiu)
MAX_RENASCIMENTOS = 2       # quantas vezes cada cabeça pode renascer
VIDA_AO_RENASCER = 40       # % do HP máximo com que ela volta

#Ficha dos inimigos

STATUS_INIMIGO = {
    #Fase 1
    "Lemuriano Desatento": {
        "max_hp": 7, "max_mp": 4, "ataque": 4, "defesa": 1, "velocidade": 4,
        "precisao": 85,                       # chance de acerto do ataque normal (%)
        "habilidades": [LANCA_ESQUECIDA],
    },
    "Serpe Neonata": {
        "max_hp": 5, "max_mp": 3, "ataque": 4, "defesa": 0, "velocidade": 8,
        "precisao": 95,                       # chance de acerto do ataque normal (%)
        "habilidades": [MORDIDA_FAMINTA],
    },
    "Gosma Distorcida": {
        "max_hp": 9, "max_mp": 3, "ataque": 4, "defesa": 2, "velocidade": 2,
        "precisao": 80,                       # chance de acerto do ataque normal (%)
        "habilidades": [ABRACO_AMALGAMADO],
    },

    #Fase 2
    "Fada Maléfica": {
        "max_hp": 9, "max_mp": 8, "ataque": 4, "defesa": 3, "velocidade": 5,
        "precisao": 95,                       # chance de acerto do ataque normal (%)
        "habilidades": [PO_DE_PESADELO, NECTAR_SOMBRIO],
    },
    "Wendigo Colérico": {
        "max_hp": 11, "max_mp": 6, "ataque": 6, "defesa": 3, "velocidade": 7,
        "precisao": 85,                       # chance de acerto do ataque normal (%)
        "habilidades": [GARRAS_DA_FOME, CROSTA_DE_GEADA],
    },
    "Espírito Obsessor": {
        "max_hp": 11, "max_mp": 6, "ataque": 5, "defesa": 4, "velocidade": 4,
        "precisao": 90,                       # chance de acerto do ataque normal (%)
        "habilidades": [SUSSURRO_OBSESSIVO],
    },

    #Fase 3
    "Serpe Crescida": {
        "max_hp": 14, "max_mp": 7, "ataque": 6, "defesa": 4, "velocidade": 6,
        "precisao": 90,                       # chance de acerto do ataque normal (%)
        "habilidades": [BAFORADA_ARDENTE],
    },
    "Guarda do Rei Arruinado": {
        "max_hp": 12, "max_mp": 12, "ataque": 6, "defesa": 4, "velocidade": 8,
        "precisao": 80,                       # chance de acerto do ataque normal (%)
        "habilidades": [GOLPE_QUEBRA_ESCUDO, JURAMENTO_PERSISTENTE],
    },
    "Bobo da Corte Endiabrado": {
        "max_hp": 18, "max_mp": 6, "ataque": 7, "defesa": 5, "velocidade": 3,
        "precisao": 95,                       # chance de acerto do ataque normal (%)
        "habilidades": [TRUQUE_SANGRENTO, MASCARA_DO_RISO],
    },

    #Minibosses
    "Serpe Matriarca": {
        "max_hp": 57, "max_mp": 28, "ataque": 14, "defesa": 3, "velocidade": 3,
        "precisao": 85,                       # chance de acerto do ataque normal (%)
        "habilidades": [CAUDA_ESMAGADORA, ESCAMAS_DO_NINHO],
    },
    "Thanatos": {
        "titulo": "O Guardião da Finitude",
        "max_hp": 80, "max_mp": 34, "ataque": 14, "defesa": 4, "velocidade": 6,
        "precisao": 85,                       # chance de acerto do ataque normal (%)
        "habilidades": [SOPRO_DO_FIM, REQUIEM],
    },
    "Rei Arruinado": {
        "max_hp": 126, "max_mp": 46, "ataque": 18, "defesa": 5, "velocidade": 7,
        "precisao": 85,                       # chance de acerto do ataque normal (%)
        "habilidades": [LAMINA_DA_COROA_PARTIDA, TRIBUTO_AO_TRONO],
    },

    #Boss (age 2 vezes por turno)
    # A Hydra Químera é formada por 3 cabeças; cada uma é um inimigo separado.
    # (números provisórios: serão balanceados na Etapa 4)
    "Cabeça de Leão": {
        "max_hp": 54, "max_mp": 24, "ataque": 10, "defesa": 5, "velocidade": 8,
        "precisao": 85,                       # chance de acerto do ataque normal (%)
        "regenera": REGENERA_RODADAS,
        "habilidades": [GARRA_DE_LEAO, TRES_CABECAS_EM_FURIA],
    },
    "Cabeça de Cabra": {
        "max_hp": 54, "max_mp": 24, "ataque": 8, "defesa": 6, "velocidade": 7,
        "precisao": 80,                       # chance de acerto do ataque normal (%)
        "regenera": REGENERA_RODADAS,
        "habilidades": [CABECA_REGENERADA, ECDISE],
    },
    "Cabeça de Serpe": {
        "max_hp": 54, "max_mp": 24, "ataque": 9, "defesa": 4, "velocidade": 10,
        "precisao": 95,                       # chance de acerto do ataque normal (%)
        "regenera": REGENERA_RODADAS,
        "habilidades": [VENENO_DO_CICLO],
    },
}

#Quais inimigos aparecem em cada fase

INIMIGOS_POR_FASE = {
    1: ["Lemuriano Desatento", "Serpe Neonata", "Gosma Distorcida"],
    2: ["Fada Maléfica", "Wendigo Colérico", "Espírito Obsessor"],
    3: ["Serpe Crescida", "Guarda do Rei Arruinado", "Bobo da Corte Endiabrado"],
}

MINIBOSS_POR_SALA = {
    3: "Serpe Matriarca",
    6: "Thanatos",
    9: "Rei Arruinado",
}

#Quantos inimigos aparecem juntos em cada fase: {quantidade: peso}
#(pesos, não porcentagens exatas: 20/45/35 sorteia 1, 2 ou 3 inimigos nessa proporção)
PESOS_ENCONTRO = {
    1: {1: 100},
    2: {1: 65, 2: 35},
    3: {1: 20, 2: 45, 3: 35},
}

#Classe do inimigo (usa a mesma base do Personagem)

class Inimigo(Personagem):

    def __init__(self, nome, status):
        Personagem.__init__(self, nome, "Inimigo", status["max_hp"], status["max_mp"],
                            status["ataque"], status["defesa"], status["velocidade"], "☠")
        self.precisao = status.get("precisao", PRECISAO_PADRAO)
        self.titulo = status.get("titulo", "")        # só os chefes têm título
        self.regenera = status.get("regenera", 0)     # rodadas para renascer (0 = não renasce)
        self.renasce_em = None                        # contagem regressiva depois de cair
        self.renascimentos = 0

        for habilidade in status["habilidades"]:
            self.aprender_habilidade(habilidade)

    #Nome com título, para mensagens de abertura: "Thanatos, O Guardião da Finitude"
    def nome_completo(self):
        if self.titulo:
            return f"{self.nome}, {self.titulo}"
        return self.nome

    #Ao cair, uma cabeça que regenera começa a contagem para renascer
    def dano_recebido(self, dano):
        causado = Personagem.dano_recebido(self, dano)
        if (not self.vivo_morto() and self.regenera > 0 and self.renasce_em is None
                and self.renascimentos < MAX_RENASCIMENTOS):
            self.renasce_em = self.regenera
        return causado

    #Chamado no fim de cada rodada. Devolve True no momento em que renasce.
    def passar_rodada(self):
        if self.vivo_morto() or self.renasce_em is None:
            return False
        self.renasce_em -= 1
        if self.renasce_em > 0:
            return False
        self.renasce_em = None
        self.renascimentos += 1
        self.hp = max(1, self.max_hp * VIDA_AO_RENASCER // 100)
        self.mp = self.max_mp // 2
        self.remover_defesa_bonus()
        return True

#Função para criar inimigos, igual a criar_personagem

def criar_inimigo(nome):
    return Inimigo(nome, STATUS_INIMIGO[nome])

def fase_da_sala(sala):
    return (sala - 1) // 3 + 1

def sortear_encontro(sala):
    fase = fase_da_sala(sala)
    pesos = PESOS_ENCONTRO[fase]
    quantidade = random.choices(list(pesos), weights=list(pesos.values()))[0]
    return [criar_inimigo(random.choice(INIMIGOS_POR_FASE[fase])) for _ in range(quantidade)]

def criar_miniboss(sala):
    return criar_inimigo(MINIBOSS_POR_SALA[sala])

#A Hydra Químera são 3 cabeças: devolve a lista com as 3 (cada uma é um inimigo)
NOME_BOSS = "Hydra Químera"
TITULO_BOSS = "A Monarca do Ciclo"
CABECAS_BOSS = ["Cabeça de Leão", "Cabeça de Cabra", "Cabeça de Serpe"]

def criar_boss():
    return [criar_inimigo(nome) for nome in CABECAS_BOSS]

def nome_completo_boss():
    return f"{NOME_BOSS}, {TITULO_BOSS}"

#Teste rápido: rode este arquivo direto no VSCode para ver os inimigos

if __name__ == "__main__":
    for sala in (1, 4, 7):
        print(f"--- Sala {sala} ---")
        for inimigo in sortear_encontro(sala):
            inimigo.mostrar_status()

    print()
    for sala in (3, 6, 9):
        criar_miniboss(sala).mostrar_status()
    for cabeca in criar_boss():
        cabeca.mostrar_status()
    print(criar_miniboss(6).nome_completo())
    print(nome_completo_boss())

    print()
    # simula um ataque e uma habilidade para ver se funciona
    heroi = Personagem("Teste", "Teste", 40, 20, 5, 3, 5, "T")
    esqueleto = criar_inimigo("Lemuriano Desatento")
    esqueleto.atacar(heroi)
    esqueleto.usar_habilidade(LANCA_ESQUECIDA, heroi)
    heroi.mostrar_status()
