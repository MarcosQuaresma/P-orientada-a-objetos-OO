class Game:
    # esse é o método construtor:
    def __init__(self, nome="", dataLancamento=0, multiplayer=0, nota=0):
        self.nome = nome
        self.dataLancamento = dataLancamento
        self.multplayer = multiplayer
        self.nota = nota 
        self.avaliacaoTotal = 0
        self.avaliados = 0
                # ele tranforma aquela identificação "<__main__.Game object at 0x000000000192843BDSJAH>" em algo legivel    
    def __str__(self): # por meio do (self) eu consigo recuperar qualquer atribudo da minah classe
        return f"Game: {self.nome}"

    def fichaTecnica(self):
        print("------> Dados do Jogo <-------")
        print(f"Nome do jogo: {self.nome}\nAno de lançamento: {self.dataLancamento}\nMultiplayer: {self.multplayer}\nNota do jogo: {self.nota}")

class GameEstudio:
    def __init__(self, nome=""):
        self.nome = nome
        self.games = [] #nessa lista podemos ultiliza-la para recoendar jogos de determinado estudio por exemplo.

    def addGame(self, game):
        self.games.append(game)

    def avaliarQualidadeDoEstudio(self):
        totalNotas = sum(game.nota for game in self.games)
        numGames = len(self.games)
        if numGames == 0:
            print(f"O estúdio {self.nome} ainda não lançou jogos!")
        else:
            mediaNotas = totalNotas / numGames
            print(f"A avaliação média dos jogos do estúdio {self.nome}: {mediaNotas:.2f}")

game1 = Game("Battlefield 4", 2013, True, 9.9)
game2 = Game("Battlefield 6", 2025, True, 9.8)
game3 = Game("Bomberman 3", 1995, False, 9.0 )

estudio = GameEstudio("Delícia De Jogo")
estudio.addGame(game1) 
estudio.addGame(game2) 
estudio.addGame(game3)

estudio.avaliarQualidadeDoEstudio()

for game in estudio.games:
    game.fichaTecnica()