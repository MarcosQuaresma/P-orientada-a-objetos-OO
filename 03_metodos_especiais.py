class Game:
    # esse é o método construtor:
    def __init__(self, nome="", dataLancamento=0, multiplayer=0, nota=0):
        self.nome = nome
        self.dataLancamento = dataLancamento
        self.multplayer = multiplayer
        self.nota = nota 

                # ele tranforma aquela identificação "<__main__.Game object at 0x000000000192843BDSJAH>" em algo legivel    
    def __str__(self): # por meio do (self) eu consigo recuperar qualquer atribudo da minah classe
        return f"Game: {self.nome}"

game1 = Game("Battlefield 4", 2013, True, 9.9)
game2 = Game("Battlefield 6", 2025, True, 9.8)
game3 = Game("Bomberman 3", 1995, False, 9.0 )

print(game1)
print(game2)
print(game3)

print("------> Dados do Jogo <-------")
# print(f"Nome do jogo: {game5.nome}\nAno de lançamento: {game5.dataLancamento}")

