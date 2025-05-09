 # Integrar com SSL-Vision





import math
import socket
import struct
import time
from collections import deque

estados = {
    'PARADO': 0,
    'SEGUIR_ELIPSE': 1,
    'DESARME': 2,
    'MERGULHO': 3,
    'SAIDA_RAPIDA': 4,
    'PASSE': 5
}

class GoleiroFSM:
    def __init__(self,
                 id_robo=1,
                 centro_gol=(0, -4.5),
                 velocidade_max=2.0,
                 dist_tackle=0.3,
                 elipse_a=0.5,
                 elipse_b=1.0,
                 angulo_saida=math.pi/6,
                 velocidade_saida=2.5,
                 limiar_mergulho=1.2,
                 historico_tamanho=5):

        self.id_robo       = id_robo
        self.centro_gol    = centro_gol
        self.velocidade_max= velocidade_max
        self.dist_tackle   = dist_tackle
        self.elipse_a      = elipse_a
        self.elipse_b      = elipse_b
        self.angulo_saida  = angulo_saida
        self.velocidade_saida = velocidade_saida
        self.limiar_mergulho = limiar_mergulho
        self.historico_bola  = deque(maxlen=historico_tamanho)
        self.estado          = estados['PARADO']

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def enviar_movimento(self, vx, vy, omega=0):
        pacote = struct.pack('<iiii', self.id_robo,
                             int(vx*1000),
                             int(vy*1000),
                             int(omega*1000))
        self.sock.sendto(pacote, ('127.0.0.1', 20011))

    def atualizar_bola(self, pos_bola):
        self.historico_bola.append(pos_bola)

    def prever_bola(self, dt=0.1):
        if len(self.historico_bola) < 2:
            return self.historico_bola[-1] if self.historico_bola else None
        x0, y0 = self.historico_bola[-2]
        x1, y1 = self.historico_bola[-1]
        vx = (x1 - x0) / dt
        vy = (y1 - y0) / dt
        return (x1 + vx*dt, y1 + vy*dt), math.hypot(vx, vy)

    def angulo_entre(self, origem, destino):
        return math.atan2(destino[1]-origem[1], destino[0]-origem[0])

    def ponto_na_elipse(self, pos_bola):
        dx = pos_bola[0] - self.centro_gol[0]
        dy = pos_bola[1] - self.centro_gol[1]
        theta = math.atan2(dy, dx)
        x = self.centro_gol[0] + self.elipse_a * math.cos(theta)
        y = self.centro_gol[1] + self.elipse_b * math.sin(theta)
        return (x, y)

    def decidir(self, pos_bola, pos_goleiro, aliados, adversarios):
        self.atualizar_bola(pos_bola)
        previsao, velocidade = self.prever_bola()
        distancia_bola = math.hypot(pos_bola[0]-pos_goleiro[0], pos_bola[1]-pos_goleiro[1])

        if distancia_bola < self.dist_tackle:
            self.estado = estados['DESARME']
            return self._agir_desarme(pos_bola, pos_goleiro)

        if previsao:
            gx, gy = self.centro_gol
            largura_gol = 1.0
            if abs(previsao[0] - gx) > largura_gol and velocidade > self.limiar_mergulho:
                self.estado = estados['MERGULHO']
                return self._agir_mergulho(previsao, pos_goleiro)

        if previsao:
            ang = self.angulo_entre(self.centro_gol, previsao)
            if abs(ang) < self.angulo_saida and velocidade > self.velocidade_max*0.7:
                self.estado = estados['SAIDA_RAPIDA']
                return self._agir_saida(previsao, pos_goleiro)

        if pos_bola[1] > self.centro_gol[1] + 0.5:
            self.estado = estados['SEGUIR_ELIPSE']
            return self._agir_elipse(pos_bola, pos_goleiro)

        self.estado = estados['PARADO']
        return self._agir_parado()

    def _agir_desarme(self, bola, goleiro):
        ang = self.angulo_entre(goleiro, bola)
        vx, vy = math.cos(ang)*self.velocidade_max, math.sin(ang)*self.velocidade_max
        self.enviar_movimento(vx, vy)

    def _agir_mergulho(self, previsao, goleiro):
        ang = self.angulo_entre(goleiro, previsao)
        vx, vy = math.cos(ang)*self.velocidade_saida, math.sin(ang)*self.velocidade_saida
        self.enviar_movimento(vx, vy, omega=3.0)

    def _agir_saida(self, previsao, goleiro):
        ang = self.angulo_entre(goleiro, previsao)
        vx, vy = math.cos(ang)*self.velocidade_saida, math.sin(ang)*self.velocidade_saida
        self.enviar_movimento(vx, vy)

    def _agir_elipse(self, bola, goleiro):
        alvo = self.ponto_na_elipse(bola)
        ang  = self.angulo_entre(goleiro, alvo)
        vx, vy = math.cos(ang)*self.velocidade_max, math.sin(ang)*self.velocidade_max
        self.enviar_movimento(vx, vy)

    def _agir_parado(self):
        self.enviar_movimento(0, 0)

# Exemplo de uso:

def obter_posicao_bola():
    return (0.0, -2.5)  # Exemplo fictício

def obter_posicao_goleiro():
    return (0.0, -4.3)  # Exemplo fictício

def obter_aliados():
    return []  # Lista fictícia de aliados

def obter_adversarios():
    return []  # Lista fictícia de adversários

if __name__ == "__main__":
    goleiro = GoleiroFSM()

    while True:
        pos_bola = obter_posicao_bola()
        pos_goleiro = obter_posicao_goleiro()
        aliados = obter_aliados()
        adversarios = obter_adversarios()

        goleiro.decidir(pos_bola, pos_goleiro, aliados, adversarios)
        time.sleep(0.05)
        # Simulação de tempo de espera entre decisões
        