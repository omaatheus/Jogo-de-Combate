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

    def receberAtaque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = self.__nivel * 2
        alvo.receberAtaque(dano)
        print(f"{self.getNome()} atacou {alvo.getNome()} e causou {dano} de dano!")



class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel) #recebo tudo de personagem pelo super
        self.__habilidade = habilidade

    def getHabilidade(self):
        return self.__habilidade

    def exibirDetalhes(self):
        return f"{super().exibirDetalhes()}\nHabilidade: {self.getHabilidade()}"

    def ataqueEspecial(self, alvo):
        dano = self.getNivel() * 5
        alvo.receberAtaque(dano)
        print(f"\n{self.getNome()} atacou com seu poder de {self.getHabilidade()}!")

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
    def __init__(self):
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

                if escolha == "1":
                    self.heroi.atacar(self.inimigo)
                elif escolha == "2":
                    self.heroi.ataqueEspecial(self.inimigo)
                else:
                    print("\n|====== Escolha Inválida, escolha novamente ======|")

                if self.inimigo.getVida() > 0:
                    self.inimigo.atacar(self.heroi)


            if self.heroi.getVida() > 0:
                print(f"\n|====== Parabéns, você ganhou a batalha! ======|")
            else:
                print(f"\n|====== Infelizmente, você perdeu a batalha! ======|")


jogo = Jogo()
jogo.iniciarBatalha()