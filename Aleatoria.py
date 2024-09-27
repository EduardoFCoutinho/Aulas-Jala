import random

class Dado:
    def __init__(self, num_faces):
        self.num_faces = num_faces

    def rolar(self):
        return random.randint(1, self.num_faces)

class Jogador:
    def __init__(self, nome, dados):
        self.nome = nome
        self.dados = dados
        self.pontuacao = 0

    def jogar(self):
        soma = 0
        for dado in self.dados:
            soma += dado.rolar()
        self.pontuacao += soma
        return soma

class Batalha:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.num_rodadas = random.randint(2, 12)

    def realizar_batalha(self):
        for _ in range(self.num_rodadas):
            pontuacao_j1 = self.jogador1.jogar()
            pontuacao_j2 = self.jogador2.jogar()
            print(f"Rodada: {self.jogador1.nome}: {pontuacao_j1}, {self.jogador2.nome}: {pontuacao_j2}")

        if self.jogador1.pontuacao > self.jogador2.pontuacao:
            return self.jogador1
        else:
            return self.jogador2

class Torneio:
    def __init__(self, regras):
        self.jogadores = []
        self.regras = regras
        self.vencedores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def iniciar(self):
        while len(self.jogadores) > 1:
            jogador1 = self.jogadores.pop(0)
            jogador2 = self.jogadores.pop(0)
            vencedor = Batalha(jogador1, jogador2).realizar_batalha()
            self.vencedores.append(vencedor)
            self.jogadores.append(vencedor)

        print(f"O campeão é {self.vencedores[-1].nome}!")
  
# Criando jogadores
jogador1 = Jogador("Alice", [Dado(6), Dado(8)])
jogador2 = Jogador("Bob", [Dado(4), Dado(10)])
jogador3 = Jogador("Carol", [Dado(6), Dado(6)])

# Criando o torneio
torneio = Torneio([jogador1, jogador2, jogador3])

# Iniciando o torneio
torneio.iniciar()
