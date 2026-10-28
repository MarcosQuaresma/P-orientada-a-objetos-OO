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

    def notasAvaliadas(self, nota):
        self.avaliacaoTotal += nota 
        self.avaliados += 1

    def media(self):
        print(f"Média do jogo {self.nome}: {self.avaliacaoTotal / self.avaliados}")


game1 = Game("Battlefield 4", 2013, True, 9.9)
game2 = Game("Battlefield 6", 2025, True, 9.8)
game3 = Game("Bomberman 3", 1995, False, 9.0 )

game1.fichaTecnica()
game2.fichaTecnica()
game3.fichaTecnica()

game1.notasAvaliadas(2)
game1.notasAvaliadas(9.8)
game1.media()

game2.notasAvaliadas(7.6)
game2.notasAvaliadas(9.8)
game2.media()

game3.notasAvaliadas(9.1)
game3.notasAvaliadas(10.0)
game3.media()