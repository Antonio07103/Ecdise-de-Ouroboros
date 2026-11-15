
import random

#Chance de acerto dos ataques normais (em %). Habilidades sempre acertam.
PRECISAO_PADRAO = 90

#Defesa em porcentagem: reduz o dano em defesa / (defesa + DEFESA_K).
#Com K = 20: defesa 5 reduz 20%, defesa 10 reduz 33%, defesa 20 reduz 50%.
#Defesa negativa (debuff) aumenta o dano; o piso evita que o dano exploda.
DEFESA_K = 20
DEFESA_MINIMA = -10

def reducao_defesa(defesa):
    d = max(DEFESA_MINIMA, defesa)
    return d / (d + DEFESA_K)

#Habilidades Especiais de cada classe

DRENO_VAMPIRICO = {
    "nome": "Dreno Vampírico",
    "custo_mp": 7,
    "dano": 8,
    "cura": 5,
    "mensagem": "{nome} drena a vitalidade do inimigo com suas sombras!",
}

CONSTELACOES_ALINHADAS = {
    "nome": "Constelações Alinhadas",
    "custo_mp": 10,
    "cura": 15,
    "cura_party": True,
    "bonus_velocidade": 2,
    "duracao_bonus": 3,
    "alvo": "party",
    "buff_party": True,
    "mensagem": "{nome} alinha os astros e abençoa seus aliados com a luz das estrelas!"
}

NINJUTSU_DA_FUMACA = {
    "nome": "Ninjutsu da Fumaça",
    "custo_mp": 7,
    "inalvejavel": True,
    "bonus_golpe": 20,
    "mensagem": "{nome} sumiu em meio à fumaça. A lâmina que não se vê é a mais mortífera!",
}

HABILIDADE_INICIAL = {
    "Cavaleiro Sombrio": DRENO_VAMPIRICO,
    "Astrólogo": CONSTELACOES_ALINHADAS,
    "Ninja": NINJUTSU_DA_FUMACA,
}

#Ficha dos personagens

STATUS_CLASSE = {
    "Cavaleiro Sombrio": {
        "nome": "Alucard",
        "simbolo": "♞",
        "max_hp": 40, "max_mp": 25, "ataque": 5, "defesa": 15, "velocidade": 5,
        "precisao": 90,
    },
    "Ninja": {
        "nome": "Hayabusa",
        "simbolo": "☻",
        "max_hp": 20, "max_mp": 20, "ataque": 8, "defesa": 3, "velocidade": 9,
        "precisao": 98,
    },
    "Astrólogo": {
        "nome": "Marie",
        "simbolo": "★",
        "max_hp": 25, "max_mp": 40, "ataque": 3, "defesa": 6, "velocidade": 6,
        "precisao": 90,
    }
}

#Classe que guarda os atributos do personagem

class Personagem:

    def __init__(self, nome, classe, max_hp, max_mp, ataque, defesa, velocidade, simbolo):
        self.nome = nome
        self.classe = classe
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mp = max_mp
        self.mp = max_mp
        self.ataque = ataque
        self.defesa = defesa
        self.defesa_bonus = 0
        self.defesa_bonus_turnos = 0
        self.velocidade = velocidade
        self.velocidade_base = velocidade
        self.velocidade_bonus_turnos = 0
        self.habilidades = []
        self.inalvejavel = False
        self.bonus_golpe = 0
        self.simbolo = simbolo
        self.precisao = PRECISAO_PADRAO

    #Consulta sobre a morte do personagem e sobre seus atributos

    def vivo_morto(self):
        return self.hp > 0

    def mostrar_status(self):
        print(f"{self.nome} ({self.classe}) HP: {self.hp} / {self.max_hp} MP: {self.mp} / {self.max_mp}")

    #Sistema de dano e cura

    def dano_recebido(self, dano):
        if self.inalvejavel:
            print(f"{self.nome} desviou do ataque!")
            return 0

        hp_antes = self.hp
        self.hp = max(0, self.hp - dano)
        return hp_antes - self.hp

    def curar(self, cura):
        hp_antes = self.hp
        self.hp = min(self.max_hp, self.hp + cura)
        return self.hp - hp_antes

    def restaurar_mp(self, valor):
        mp_antes = self.mp
        self.mp = min(self.max_mp, self.mp + valor)
        return self.mp - mp_antes

    def aplicar_defesa_bonus(self, valor, duracao):
        self.defesa -= self.defesa_bonus
        self.defesa_bonus = valor
        self.defesa += valor
        self.defesa_bonus_turnos = duracao

    def remover_defesa_bonus(self):
        self.defesa -= self.defesa_bonus
        self.defesa_bonus = 0
        self.defesa_bonus_turnos = 0

    def fim_turno(self):
        if self.velocidade_bonus_turnos > 0:
            self.velocidade_bonus_turnos -= 1
            if self.velocidade_bonus_turnos == 0:
                self.velocidade = self.velocidade_base
                print(f"O bônus de velocidade de {self.nome} acabou.")

        if self.defesa_bonus_turnos >0:
            self.defesa_bonus_turnos -= 1
            if self.defesa_bonus_turnos == 0:
                self.remover_defesa_bonus()
                print(f"O bônus de defesa de {self.nome} acabou.")

    def fim_combate(self):
        self.velocidade = self.velocidade_base
        self.velocidade_bonus_turnos = 0
        self.bonus_golpe = 0
        self.inalvejavel = False
        self.remover_defesa_bonus()

    def calculo_dano(self, alvo):
        bruto = self.ataque + self.bonus_golpe
        dano = int(bruto * (1 - reducao_defesa(alvo.defesa)) + 0.5)      # arredonda para o mais próximo
        return max(1, dano)

    def acertou(self):
        if self.bonus_golpe > 0:
            return True                                  # golpe aprimorado (Ninjutsu da Fumaça) nunca erra
        return random.random() * 100 < self.precisao

    def atacar(self, alvo):
        if not self.acertou():
            print(f"{self.nome} errou o ataque em {alvo.nome}!")
            self.bonus_golpe = 0
            self.inalvejavel = False
            return 0

        dano_calculado = self.calculo_dano(alvo)
        dano = alvo.dano_recebido(dano_calculado)

        if dano > 0:
            print(f"{self.nome} causou: {dano} de dano em {alvo.nome}!")

        self.bonus_golpe = 0
        self.inalvejavel = False

        return dano

    #Sistema de habilidades

    def aprender_habilidade(self, habilidade):
        if habilidade not in self.habilidades:
            self.habilidades.append(habilidade)

    def pode_usar(self, habilidade):
        return (self.mp >= habilidade.get("custo_mp", 0)
                and self.hp > habilidade.get("custo_hp", 0))

    def usar_habilidade(self, habilidade, alvo, party=None):
        if not self.pode_usar(habilidade):
            print(f"{self.nome} não tem recursos para usar {habilidade['nome']}!")
            return 0

        # quantidade de golpes: fixa, ou definida pelo MP que o personagem tinha ao usar
        golpes = habilidade.get("golpes", 1)
        faixas = habilidade.get("faixas_golpes")          # lista de (MP mínimo, golpes)
        if faixas:
            golpes = max(g for minimo, g in faixas if self.mp >= minimo)

        if habilidade.get("gasta_todo_mp"):
            self.mp = 0                                   # gasta todo o MP que tinha
        else:
            self.mp = self.mp - habilidade.get("custo_mp", 0)
        self.hp = self.hp - habilidade.get("custo_hp", 0)
        print(f"{self.nome} usou {habilidade['nome']}!")
        if habilidade.get("gasta_todo_mp"):
            print(f"{self.nome} gastou todo o MP! ({golpes} golpes)")
        if habilidade.get("custo_hp", 0) > 0:
            print(f"{self.nome} sacrificou {habilidade['custo_hp']} de HP!")

        mensagem = habilidade.get("mensagem")
        if mensagem:
            print(mensagem.format(nome=self.nome))

        grupo = party if party else [self]
        afetados = grupo if habilidade.get("buff_party", False) else [self]

        # habilidade em área: "alvo" chega como lista (todos os inimigos / todos os heróis)
        if isinstance(alvo, list):
            alvos = [a for a in alvo if a.vivo_morto()]
            alvo = alvos[0] if alvos else self
        else:
            alvos = [alvo]

        # dano
        dano_causado = 0
        dano = habilidade.get("dano", 0)
        if dano > 0:
            if habilidade.get("golpes_aleatorios"):
                # cada golpe sorteia um alvo vivo diferente
                for _ in range(golpes):
                    vivos_ = [a for a in alvos if a.vivo_morto()]
                    if not vivos_:
                        break
                    alvo_atual = random.choice(vivos_)
                    causado = alvo_atual.dano_recebido(dano)
                    dano_causado += causado
                    print(f"{alvo_atual.nome} sofreu {causado} de dano!")
            else:
                for alvo_atual in alvos:
                    for _ in range(golpes):
                        causado = alvo_atual.dano_recebido(dano)
                        if causado == 0:
                            break
                        dano_causado += causado
                        print(f"{alvo_atual.nome} sofreu {causado} de dano!")

        # enfraquecer a defesa do alvo
        debuff = habilidade.get("debuff_defesa", 0)
        if debuff > 0:
            duracao = habilidade.get("duracao_defesa", 3)
            for alvo_atual in alvos:
                if alvo_atual.vivo_morto():
                    alvo_atual.aplicar_defesa_bonus(-debuff, duracao)
                    print(f"A defesa de {alvo_atual.nome} caiu em {debuff} por {duracao} turnos!")

        # cura de HP
        cura = habilidade.get("cura", 0)
        cura_pct = habilidade.get("cura_pct", 0)          # cura em % do HP máximo de quem recebe
        if cura > 0 or cura_pct > 0:
            if habilidade.get("cura_party", False):
                curados = grupo
            elif habilidade.get("cura_alvo", False):
                curados = [alvo]
            else:
                curados = [self]
            for aliado in curados:
                if aliado.vivo_morto():
                    valor = cura + (max(1, aliado.max_hp * cura_pct // 100) if cura_pct > 0 else 0)
                    recuperado = aliado.curar(valor)
                    print(f"{aliado.nome} recuperou {recuperado} de HP!")

        # restaurar MP
        restaura_mp = habilidade.get("restaura_mp", 0)
        if restaura_mp > 0:
            for aliado in afetados:
                if aliado.vivo_morto():
                    recuperado = aliado.restaurar_mp(restaura_mp)
                    print(f"{aliado.nome} recuperou {recuperado} de MP!")

        # bônus de velocidade
        bonus_velocidade = habilidade.get("bonus_velocidade", 0)
        if bonus_velocidade > 0:
            duracao = habilidade.get("duracao_bonus", 3)
            for aliado in afetados:
                if aliado.vivo_morto():
                    aliado.velocidade = aliado.velocidade_base + bonus_velocidade
                    aliado.velocidade_bonus_turnos = duracao
            print(f"A velocidade aumentou em {bonus_velocidade} por {duracao} turnos!")

        # bônus de defesa
        bonus_defesa = habilidade.get("bonus_defesa", 0)
        if bonus_defesa > 0:
            duracao = habilidade.get("duracao_defesa", 3)
            for aliado in afetados:
                if aliado.vivo_morto():
                    aliado.aplicar_defesa_bonus(bonus_defesa, duracao)
            print(f"A defesa aumentou em {bonus_defesa} por {duracao} turnos!")

        if habilidade.get("inalvejavel", False):
            self.inalvejavel = True

        bonus = habilidade.get("bonus_golpe", 0)
        if bonus > 0:
            self.bonus_golpe = bonus

        return dano_causado

#Função para criar personagens e a party, para não ter conflito quando for testar em outros momentos

def criar_personagem(classe):
    status = STATUS_CLASSE[classe]

    personagem = Personagem(
        status["nome"],
        classe,
        status["max_hp"],
        status["max_mp"],
        status["ataque"],
        status["defesa"],
        status["velocidade"],
        status["simbolo"],
    )

    personagem.precisao = status.get("precisao", PRECISAO_PADRAO)
    personagem.aprender_habilidade(HABILIDADE_INICIAL[classe])
    return personagem

LIMITE_PARTY = 3

def criar_party():
    return [criar_personagem("Cavaleiro Sombrio")]

def adicionar_membro(party,classe):
    if len(party) >= LIMITE_PARTY:
        print("Você já encontrou todos seus amigos!")
        return False

    for membro in party:
        if membro.classe == classe:
            print(f"{classe} já foi encontrado e está na party!")
            return False

    party.append(criar_personagem(classe))
    return True

def party_derrotada(party):
    for membro in party:
        if membro.vivo_morto():
            return False
    return True
