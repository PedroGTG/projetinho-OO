#Personagem
import random
import sys

class Personagem:

    def __init__(self,hp,atk, lv, wallet):
        self.lv = lv
        self.hp = hp
        self.atk = atk
        self.__wallet = wallet

    #encapsulamento de umas parada
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, valor):
        self._hp = max(valor,0) #vida nao fica menor que 0
    
    @property
    def lv(self):
        return self._lv

    @lv.setter    
    def lv(self,valor):
        self._lv = max(valor, 1) 

    @property
    def wallet(self):
        return self.__wallet
    
    @wallet.setter
    def wallet(self,valor):
        self.__wallet = max(valor, 0)
    
    @property
    def atk(self):
        return self._atk
    
    @atk.setter
    def atk(self, value):
        self._atk = max(value,1)

    def _attack(self, target):
        dano = self.atk + random.randint(0,self.lv) #dano = numero random + level
        target.hp -= dano
        target.hp = max(0,target.hp) #se a vida ficar negativa, zero fica maior, ou seja, a vida fica no zero
        if(target.hp == 0): print(f"BOOMM!!!, {target.__class__.__name__} derrotado")
        else: print(f"{self.__class__.__name__} causou {dano} de dano!, {target.__class__.__name__} esta com {target.hp} de vida")
        return target.hp

    def defend(self):
        print("25/100 de chance de bloquear e causar o triplo de dano no proximo turno!")
        if(random.randint(0,100)<= 25): return True
        return False
    
    def combate(self, inimigo, main_char):
        defesa_mult_dmg = False
        while main_char.hp > 0 and inimigo.hp > 0:
            defesa = False
            print("\nSeu turno")
            print("\n")
            while True:
                try:
                    act = int(input("Aperte 1 para atacar ou 2 para defender: "))
                    break
                except ValueError:
                    print("invalido")
            print(" ")
            match act:
                case 1:
                    if defesa_mult_dmg == True:
                        main_char.atk *= 3
                        main_char._attack(inimigo)
                        main_char.atk /= 3
                        main_char.atk = int(main_char.atk)
                        defesa_mult_dmg = False
                    else:
                        if random.randint(0,4) != 2:
                           main_char._attack(inimigo)
                        else:
                           inimigo._defend(inimigo,main_char)  #polimorfismo
                           self.game_over(main_char)
                           continue
                case 2:
                    defesa = main_char.defend()
                case _:
                    print("comando invalido")
            if inimigo.hp == 0:
                inimigo._drop(main_char)
                return 0
            print("\nTurno do oponente:")
            input("...")
            if defesa:
                print("Você se defendeu com sucesso! Nenhum dano foi causado.")
                defesa_mult_dmg = True
                continue
            else:
                input("Você não se defendeu. O inimigo atacará!...")
                inimigo._attack(main_char)
                self.game_over(main_char)
        
    def game_over(self,main_char):
        if main_char.hp == 0: 
            input("Game over...\nAperte algo pro jogo fechar e reiniciar") 
            return sys.exit()


class Inimigo(Personagem):
    def __init__(self,hp,atk, lv, wallet):
        super().__init__(hp,atk,lv, wallet)
        self.hp += 5 * self.lv
        self.atk += 2 * self.lv

    def _drop(self, main_char):
        if self.hp == 0:
            main_char.money(self.wallet)
            main_char.level_up(self.lv)
            print(f"Você ganhou {self.lv} de xp e {self.wallet} moedas")
            print(f"No total, tens {main_char.wallet} moedas, e com a experiência permanece no nível {main_char.lv}")

    def _defend(self,inimigo,main_char):
        print("O inimigo defendeu!!!!\nCom uma grande abertura, ele garante um crítico em seu contra-ataque e te acerta em cheio")
        self.atk *= 1.5
        self.atk = int(self.atk)
        inimigo._attack(main_char)
        self.atk /= 1.5
        self.atk= int(self.atk)

class Jogador(Personagem):
    def __init__(self,hp,atk,lv,xp,wallet,weapon,name):
        super().__init__(hp,atk,lv,wallet)
        self.xp = xp
        self.hp_potions = 2
        self.hp_cap = self.hp
        self.weapon = weapon
        self.cord_x = 0
        self.cord_y = 0
        self.fase = 0
        self.name = name
    
    @property
    def xp(self):
        return self.__xp
    @xp.setter
    def xp(self,value):
        self.__xp = max(value,0)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,valor):
        while valor.isdigit() or valor == "": print("\no nome do jogador não pode ser um número ou um espaço em branco\n"); valor = input("digite o nome novamente: ")
        self._name = valor

    @property
    def weapon(self):
        return self._weapon
    @weapon.setter
    def weapon(self,valor):
        while valor.isdigit(): print("\no nome da arma não pode ser um número\n"); valor = input("digite o nome novamente: ")
        self._weapon = valor


    def level_up(self,exp_ganho):
        self.xp += exp_ganho
        if self.xp >= 10:
            self.lv += 1
            self.xp -= 10
            self.hp_cap += 10 * self.lv
            self.hp += 10 * self.lv
            self.atk += 5 * self.lv
            print(f"\n level up!! ganhastes {self.lv * 10} de vida e {self.lv *  5} de ataque")

    def money(self, valor):
        self.wallet += valor

    def drink_hp(self,font):
      if self.hp == self.hp_cap:
        print("\n já estás revigorado ")

      elif font:
          max_heal = self.hp_cap - self.hp
          self.hp += min(max_heal,10)

      elif self.hp_potions > 0:
          max_heal = self.hp_cap - self.hp
          self.hp_potions -= 1
          self.hp += min(max_heal,10)
          print(f"\n Curastes {min(max_heal,10)} de vida, agora estas com  {self.hp} de {self.hp_cap}\nAgora te restas {self.hp_potions} poções de cura")
