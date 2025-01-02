#Mapa e loja
from my_chars import *
import sys


class Loja:
    def __init__(self,discount,rank,types,tabela):
        self.__rank = rank
        self.__discount = discount
        #loja1 = types -> apresenta apenas arma e hp, se eu implementar mais coisa na loja eu crio tabelas com display de mais items
        self.tabela = tabela
        self.__types = types

    @property
    def types(self):
        return self.__types

    @types.setter
    def tabela(self, valor):
        self.__types = max(0, valor)
        

    @property 
    def tabela(self):
        return self.__tabela

    @tabela.setter
    def tabela(self, valor):
        if not isinstance(valor, dict):
            raise ValueError("O atributo 'tabela' deve ser um dicionário.")
        self.__tabela = valor
    
    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self,valor):
        if valor < 0:
            self.__discount = max(0,valor) #sem disconto negativo

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        if value > 0:  # so aceita valores positivos
            self.__rank = value

    def player_money_check(self,main_char,price):
        if main_char.wallet < price - price * self.discount / 100:
            return False
        return True

    def buy(self, main_char):
        choose = "nada"
        while choose != "0":
            try:
                choose = input("aperte de [1] a [2] comforme a tabela ou [0] para sair: ")
            except ValueError:
                print("invalido")
                continue

            match choose:
                case "0":
                    print("\nsaistes da lolja \n")
                case "1":
                    if self.player_money_check(main_char,self.tabela["hp_price"]):
                        main_char.hp_potions += 1
                        main_char.wallet -= int(self.tabela["hp_price"] - self.tabela["hp_price"] * self.discount / 100)
                        print(f"\npoção comprada, agora você tem {main_char.wallet} de grana sobrando e {main_char.hp_potions} poções de cura\n")
                    else: print("\ndinheiro insuficiente \n")
                case "2":
                    if self.player_money_check(main_char,self.tabela["w_price"]):
                       arma_antiga = main_char.weapon; dano_novo = self.tabela["w_dmg"]
                       main_char.weapon = self.tabela["w"]
                       main_char.wallet -= int(self.tabela["w_price"] - self.tabela["w_price"] * self.discount / 100)
                       main_char.atk += self.tabela["w_dmg"] * self.rank
                       print(f"\nTrocastes {arma_antiga} por {main_char.weapon}, agora você da {dano_novo} de  dano a mais e tem {main_char.wallet} de grana sobrando\n")
                    else: print("\ndinheiro insuficiente \n")
                case _:
                    print(f"input {choose} invalido")
            self.print_tabela()

    def print_items(self,main_char):
        print(f"\nDesconto atual da loja: {self.discount}%")
        self.print_tabela()
        print("\nOBS:\n")
        print(f"Arma da loja -> {self.tabela['w']} , dano adicional -> {self.tabela['w_dmg']} \nSua arma -> {main_char.weapon}")
        num = input("aperte alguma coisa para comprar um item ou 'q' para sair: ")
        if num == 'q':
            return 0
        else:
            self.buy(main_char)
        print("\n")

    def print_tabela(self):
        count = 0
        for item, valor in self.types.items():
            count += 1
            print(f"{item}--> {int(valor - valor * self.discount / 100)}$  --> [{count}] ")

class Mapa(Jogador):
    def __init__(self,matriz,diff,jogo,cord_x,cord_y):
        self.jogo = jogo   
        self.__matriz = matriz
        self.traps = Inimigo(1,3,1,0)
        self.diff = diff
        self.finish = False
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.loja1 = Loja(random.randint(0,20),1,{"poção de vida" : 10,"arma levemente melhorada": 30}, {"w_price":30, "hp_price":10, "w": f"{self.jogo.main_char.weapon} + 5 níveis da sua atual", "w_dmg": 10})
        self.loja2 = Loja(random.randint(0,50),3,{"poção de vida" : 10,"arma rara" : 50}, {"w_price":50, "hp_price":10, "w":"espadão", "w_dmg": 10})
     
    @property
    def matriz(self):
        return self.__matriz

    @matriz.setter
    def matriz(self, nova_matriz):
        #vai verificar se é uma lista de listas
        if not (isinstance(nova_matriz, list) and all(isinstance(linha, list) for linha in nova_matriz)):
            raise ValueError("A matriz deve ser uma lista de listas.")
        self.__matriz = nova_matriz

    @property
    def diff(self):
        return self.__diff
    def diff(self,value):
        self.__diff = max(0,value)
    
    
    def imprimir_mapa(self):
        for i in range(len(self.matriz)):
            print()  # Separar linha
            for j in range(len(self.matriz[0])):
                print(self.matriz[i][j], end=" ")


    def move_up(self):
        if self.cord_y != 0 and self.matriz[self.cord_y-1][self.cord_x] != "#":
            if self.matriz[self.cord_y][self.cord_x] != "$":
              self.matriz[self.cord_y][self.cord_x] = " "
            self.cord_y -= 1
            self.event()
            self.matriz[self.cord_y][self.cord_x] = "W"
            if self.finish == False: self.imprimir_mapa()
        else: print("LIMITE")

    def move_left(self):
        if self.cord_x != 0 and self.matriz[self.cord_y][self.cord_x-1] != "#":
            if self.matriz[self.cord_y][self.cord_x] != "$":
              self.matriz[self.cord_y][self.cord_x] = " "
            self.cord_x -= 1
            self.event()
            self.matriz[self.cord_y][self.cord_x] = "W"
            if self.finish == False: self.imprimir_mapa()
        else: print("LIMITE")


    def move_right(self):
        if self.cord_x  != len(self.matriz[0]) - 1 and self.matriz[self.cord_y][self.cord_x+1] != "#":
            if self.matriz[self.cord_y][self.cord_x] != "$":
              self.matriz[self.cord_y][self.cord_x] = " "
            self.cord_x += 1
            self.event()
            self.matriz[self.cord_y][self.cord_x] = "W"
            if self.finish == False: self.imprimir_mapa()
        else: print("LIMITE")


    def move_down(self):
        if self.cord_y != len(self.matriz) - 1 and self.matriz[self.cord_y+1][self.cord_x] != "#":
            if self.matriz[self.cord_y][self.cord_x] != "$":
              self.matriz[self.cord_y][self.cord_x] = " "
            self.cord_y += 1
            self.event()
            self.matriz[self.cord_y][self.cord_x] = "W"
            if self.finish == False: self.imprimir_mapa()
        else: print("LIMITE do mapa")


    def gerar_inimigos(self, dif):
        if dif == 1:
            print("inimigo!!!")
            goblin1 = Inimigo(10,2,self.diff,5 + 5 * self.diff)
            self.jogo.main_char.combate(goblin1,self.jogo.main_char)
            print("\ncalma, outro goblin?!")
            goblin2 = Inimigo(12,1,self.diff,3 + 5 * self.diff)
            self.jogo.main_char.combate(goblin2,self.jogo.main_char)
            print("\nmais um???!!")
            goblin3 = Inimigo(13,1,self.diff,6 + 5 * self.diff)
            self.jogo.main_char.combate(goblin3,self.jogo.main_char)
        elif dif == 2:
            print("um golem gigante se aproxima")
            golem = Inimigo(30,9,self.diff, 10 + 10 * self.diff )
            self.jogo.main_char.combate(golem,self.jogo.main_char)
        elif dif == 3:
            print("você sente calafrios, uma névoa densa sobe, e , de repente, aparace um lobo de 3 metros com uma espada na boca")
            lobo = Inimigo(50,15,self.diff, 30 + self.diff)
            self.jogo.main_char.combate(lobo,self.jogo.main_char)
            print("parece que morreu, porem ele ainda esta vivo, e com certeza voltara para te atacar")

    def event(self):
        # Verifica o que acontece com base na posição do personagem
        if self.matriz[self.cord_y][self.cord_x] == "!":
            self.gerar_inimigos(1)
        elif self.matriz[self.cord_y][self.cord_x] == "!!":
            self.gerar_inimigos(2)
        elif self.matriz[self.cord_y][self.cord_x] == "!!!":
            self.gerar_inimigos(3)
        elif self.matriz[self.cord_y][self.cord_x] == "$":
            print("entrastes na loljinha \n")
            self.loja1.print_items(self.jogo.main_char)  # Chama a loja (precisa estar definido)
        elif self.matriz[self.cord_y][self.cord_x] == "%":
            self.gerar_chest(self.jogo.main_char)
        elif self.matriz[self.cord_y][self.cord_x] == "?":
            self.trap(self.jogo.main_char)
        elif self.matriz[self.cord_y][self.cord_x] == "&&":
            for i in range(10):
              if self.jogo.main_char.hp == self.jogo.main_char.hp_cap: break
              self.jogo.main_char.drink_hp(True)
            print("CURASTES TODA A SUA VIDA NA FONTE MÁGICA")

        elif self.matriz[self.cord_y][self.cord_x] == "@":
            self.jogo.main_char.fase += 1
            self.jogo.salvar_jogo()
            print("next...")
            self.cord_x = 0
            self.cord_y = 0
            self.finish = True
            return 0

    def gerar_chest(self, main_char):
        print("\n")
        bau = random.randint(1,20)
        print(f"encontrastes um bau! Agora você tem {main_char.wallet} dinheiros")
        main_char.money(bau)

    def trap(self,main_char):
        self.traps._attack(main_char)
        print("antes de você conseguir atacar, ele deu no pé")
    
    def mover_pelo_mapa(self,levels):
        while levels.finish == False:
            print("\n")
            movimento = input("use [w],[a],[s],[d] para se mover , [e] para mostrar dados do jogador , [h] para se curar ou [q] para sair\n->seu input: ")
            print(" \n")
            match movimento:
                case "w":
                    levels.move_up()
                case "a":
                    levels.move_left()
                case "s":
                    levels.move_down()
                case "d":
                    levels.move_right()
                case "e":
                    print(f"\n{self.jogo.__str__()}")
                case "h":
                    self.jogo.main_char.drink_hp(False)
                case "q":
                    print("fechando jogo...")
                    sys.exit()
                case _:
                    print("invalido\n")
            levels.event()
            print("\n")