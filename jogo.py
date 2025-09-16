#Personagem: Classe Mae

#Heroi controlado pelo usuario

#Inimigo: adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def getNome(self):
        return self.__nome

    def getVida(self):
        return self.__vida

    def getNivel(self):
        return self.__nivel

    def exibirDetalhes(self):
        return f"\nNome: {self.getNome()} \nVida: {self.getVida()} \nNivel: {self.getNivel()}"


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel) #recebo tudo de personagem pelo super
        self.__habilidade = habilidade

    def getHabilidade(self):
        return self.__habilidade

    def exibirDetalhes(self):
        return f"{super().exibirDetalhes()}\nHabilidade: {self.getHabilidade()}"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def exibirDetalhes(self):
        return f"{super().exibirDetalhes()}\nTipo: {self.getTipo()}"


class Jogo:
    """Classe que orquestra o Jogo"""
    def __init__(self, ):
        self.heroi = Heroi("Rodolfo", 100, 5, "Força")
        self.inimigo = Inimigo("Luzas", 50, 3, "Ave")

    def iniciarBatalha(self):
            """"Gestão da Batalha"""
            print(f"|====== Iniciando Batalha... ======|")
            while self.heroi.getVida() > 0 and self.inimigo.getVida() > 0:
                print("\nDetalhes dos Personagens:")
                print(self.heroi.exibirDetalhes())
                print(self.inimigo.exibirDetalhes())

                input("|======Pressione <Enter> para atacar... ======|")
                escolha = input("\n|====== Escolha de ataque ======|\n1 - Ataque Normal\n2 - Ataque Especial\n> ")



jogo = Jogo()
jogo.iniciarBatalha()