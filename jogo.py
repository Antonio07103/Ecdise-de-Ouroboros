# ============================================================
#  A ECDISE DE OUROBOROS  -  RODE ESTE ARQUIVO PARA JOGAR
#
#  Este arquivo só liga o jogo. O código de verdade fica nos
#  arquivos separados, na mesma pasta:
#
#    personagens.py      classes, habilidades, party
#    inimigos.py         inimigos, minibosses e boss
#    baus.py             conteúdo dos baús e recompensas
#    menu.py             menu principal e escolha de membro
#    cenarioCombate.py   desenho da tela de combate
#    combate.py          turnos e regras do combate
#    cenarioEcombate.py  mapa, salas e o laço principal do jogo
#
#  Pode editar qualquer um deles: o jogo sempre usa a versão
#  que estiver salva na pasta.
# ============================================================

import os
import sys

# garante que o Python procure os arquivos na pasta deste jogo.py,
# mesmo que o terminal tenha sido aberto em outra pasta
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# o cenário roda assim que é importado (o laço do jogo fica nele)
import cenarioEcombate
