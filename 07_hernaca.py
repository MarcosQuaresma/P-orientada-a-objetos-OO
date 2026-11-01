# Classe Pai (Super Classe) - Generalista
class Game:
     # uma VARIÁVEL DE CLASSE vem antes de qualquer METODO
    totalGames = 0 # <- Variável de classe para contar o número total de jogos

    # esse é o método construtor:
    def __init__(self, nome="", dataLancamento=0, multiplayer=0, nota=0):
        self.nome = nome
        self.dataLancamento = dataLancamento
        self.multplayer = multiplayer
        self.nota = nota 
        Game.totalGames += 1
        self.avaliacaoTotal = 0
        self.avaliados = 0
                # ele tranforma aquela identificação "<__main__.Game object at 0x000000000192843BDSJAH>" em algo legivel    
    def __str__(self): # por meio do (self) eu consigo recuperar qualquer atribudo da minah classe
        return f"Game: {self.nome}"

    def fichaTecnica(self):
        print("------> Dados do Jogo <-------")
        print(f"Nome do jogo: {self.nome}\nAno de lançamento: {self.dataLancamento}\nMultiplayer: {self.multplayer}\nNota do jogo: {self.nota}")

    def notasAvaliadas(self, nota):
        self.avaliacaoTotal += nota 
        self.avaliados += 1

    def media(self):
        print(f"Média do jogo {self.nome}: {self.avaliacaoTotal / self.avaliados}")

# Classe derivada (Subclasse) - Especializada <- consegue herdar atributos e informações da Classe Pai, e ter informações pessoais personalizadas 
class SinglePlayerGame(Game):
    def __init__(self, nome="", dataLancamento=0, nota=0, enredo=""):
        super().__init__(nome, dataLancamento, multiplayer=False, nota=nota)
        self.enredo = enredo

    def fichaTecnica(self):
        super().fichaTecnica()
        print(f"Enredo: {self.enredo}")

onlineGame = Game("Battlefield 4", 2014, True, 9.0)
onlineGame.fichaTecnica()

singleGame = SinglePlayerGame("Bomberman", 1995, 9.5, "Um robô escrávizado em uma mineradora que almejava " \
"ser humano caso conseguisse sair da mineradora")
singleGame.fichaTecnica()