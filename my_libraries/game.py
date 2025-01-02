#Jogo
import pickle
import random
import sys
from my_chars import *
from my_maps import Mapa
from workspace import SaveGame

class Jogo(SaveGame):
    def __init__(self):
        super().__init__()
        self.levels = ["floresta","montanha","dungeon","caverna"]

    def __str__(self):
        return f"Vida: {self.main_char.hp} de {self.main_char.hp_cap} com {self.main_char.hp_potions} poções // Level: {self.main_char.lv} com {self.main_char.xp} de xp // Arma usada: {self.main_char.weapon} // dano  minimo: {int(self.main_char.atk)} // dinheiro : {self.main_char.wallet}" 

    def iniciar_jogo(self):
        if self.main_char.fase == 0:
            print("Você se encontra em uma caverna escura, o que será que aconteceu? De qualquer forma, você segue para o único caminho disponível.\n")
            input("Aperte qualquer coisa para continuar...\n")
            print("Um Goblin apareceu!\n")

            goblin = Inimigo(10, 2, 1, 2)
            self.main_char.combate(goblin,self.main_char)
            print("\napôs destruir o goblin, você se depara com 2 caminhos distintos, um levando para o fundo da caverna e outro para a saída\n")
            choose = (input("pressione [1] para adentrar ainda mais na caverna ou [qualque coisa] pra sair: "))

            if choose == '1':
                print("ao explorar ainda mais, escontras um dragão gigante. O DUELO COMEÇA")
                dragon = Inimigo(200,10,20,1000)
                self.main_char.combate(dragon,self.main_char)
                input("parabens, esse era o objetivo final do jogo... (aperte algo para fechar e reiniciar)")
                sys.exit()
            else:
                print("\nsabia escolha...\n")

            print("Ao sair da caverna, tu se deparas com uma grande floresta\n OBS: para completar o mapa basta chegar em @")
            self.main_char.fase += 1

        if self.main_char.fase == 1:
            self.levels[0] = Mapa([
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", "#", " ", " ", " ", "%", " ", " ", " ", "%", "#"],
            ["#", " ", " ", " ", "#", "#", " ", " ", "?", " ", " ", "#"],
            ["#", " ", " ", " ", "!", " ", " ", "!!", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#"],
            ["#", " ", " ", " ", " ", " ", " ", "#", " ", "?", " ", "#"],
            ["#", "#", "#", "#", "?", "#", "#", "#", "#", "#", " ", "#"],
            ["#", "@", " ", " ", " ", " ", " ", " ", "?", " ", " ", "#"],
            ["#", "#", "$", "!", "#", "#", " ", "#", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ], 1, jogo, 1, 1)
            self.levels[0].mover_pelo_mapa(self.levels[0])
            print("\n Você acaba de sair da floresta e entrar em um territorio rochoso, há vários inimigos fortes aqui\nnota: nesse mapa há um evento especial representado por '&&', nele restaurará sua vida")


        if self.main_char.fase == 2:
            self.levels[1] = Mapa( [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", "%", " ", "#"],
            ["#", " ", "?", "#", "#", "#", " ", " ", "?", " ", " ", "#"],
            ["#", " ", " ", "!", " ", " ", "&&", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "!", "#"],
            ["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", "#", "#", "#", " ", "?", " ", "#"],
            ["#", " ", " ", "!", " ", " ", " ", " ", "?", "&&", " ", "#"],
            ["#", "#", "#", "#", "#", " ", "#", "#", "!", "#", "#", "#"],
            ["#", "$", "?", "%", " ", " ", " ", "!!!", " ", " ", "@", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ], 2, jogo, 6, 1)
            self.levels[1].mover_pelo_mapa(self.levels[1])

            print(f"\n{self.__str__()}\n\nVocê entra em uma ruina antiga, pra ser mais exato, uma pequena dungeon")
        
        if self.main_char.fase == 3:
            self.levels[2] = Mapa([
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "@", "!!!", " ", " ", " ", " ", " ", "%", "#"],
            ["#", "!!", "#", "#", "#", "#", " ", "?", " ", "#"],
            ["#", " ", "#", "!", "!", "#", " ", "#", " ", "#"],
            ["#", " ", "#", "!", "!", "#", " ", "#", " ", "#"],
            ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
            ["#", " ", " ", " ", " ", "?", " ", "#", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ], 3, jogo, 8,7)
            self.levels[2].mover_pelo_mapa(self.levels[2])

            print(f"\n{self.__str__()}\n\nFinalmente voltastes para o inicio da jornada apôs entrar em um porta mágica\nAgora ,na caverna em que tinhas acordado, você se vê com a missão de adentrar na caverna e acabar com mal que nela emana. Boa sorte")
    
        if self.main_char.fase == 4:
            self.levels[3] = Mapa([
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#", "#", "#", " ", " ", "!!!", " ", " ", " ", " ", "#"],
            ["#", " ", "#", " ", " ", " ", "#", " ", "#", "#", " ", "#", " ", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#", " ", "#", "?", " ", "#", "#", " ", "#"],
            ["#", " ", "#", "%", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "$", "#"],
            ["#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#"],
            ["#", " ", "!!", " ", " ", " ", "#", " ", " ", " ", "&&", " ", "#", " ", "#"],
            ["#", "#", "#", "#", " ", "#", "#", " ", "#", "#", " ", "#", "#", " ", "#"],
            ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "?", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
            ["#", " ", " ", "!!!", " ", " ", " ", " ", " ", "!!", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", " ", "#"],
            ["#", " ", " ", " ", " ", "&&", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
            ["#", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
            ["#", " ", " ", "&&", " ", " ", " ", " ", " ", " ", " ", " ", " ", "@", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ], 5, jogo, 1,1)
            self.levels[3].mover_pelo_mapa(self.levels[3])

            input("Ao explorar,  em suas mais profundas camadas,escontras um dragão gigante. O DUELO COMEÇA...(aperte algo para continuar)")
            dragon = Inimigo(200,10,20,1000)
            self.main_char.combate(dragon,self.main_char)
            input("parabens, esse era o objetivo final do jogo... (aperte algo para fechar e reiniciar)")
            sys.exit()

if __name__ == '__main__':
    jogo = Jogo() #cria o obj jogo
    jogo.menu()
    jogo.iniciar_jogo()
