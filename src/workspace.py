import pickle
from my_chars import Jogador
import random

class SaveGame:

    def __init__(self):
        self.personagens = []
        self.main_char = None

    def salvar_jogo(self, nome="save_game.pkl"):
        personagens_existentes = []
        try:
            with open(nome, 'rb') as arquivo:
                personagens_existentes = pickle.load(arquivo)
        except FileNotFoundError:
            print("Nenhum jogo salvo encontrado, criando novo arquivo.")
        except Exception as e:
            print(f"Erro ao carregar dados existentes: {e}")

        for personagem in self.personagens:
            if personagem not in personagens_existentes:
                personagens_existentes.append(personagem)

        with open(nome, 'wb') as arquivo:
            pickle.dump(personagens_existentes, arquivo)
            print("\nJogo salvo\n")

    def carregar_jogo(self, nome="save_game.pkl"):
        try:
            with open(nome, 'rb') as arquivo:
                personagens_existentes = pickle.load(arquivo)
            
        # Adiciona os personagens salvos sem duplicar
            for personagem in personagens_existentes:
                if personagem not in self.personagens:
                     self.personagens.append(personagem) 

            print("Jogo carregado com sucesso.")
        except FileNotFoundError:
            print("Nenhum jogo salvo encontrado.")
            self.personagens = []  
        except Exception as e:
            print(f"Erro ao carregar o jogo: {e}")

    def menu(self):
        while True:
            print("---------------------------//\\MENU//\\--------------------------------\n")
            try:
                play = int(input("APERTE [1] PARA INICIAR UM NOVO JOGO\nAPERTE [2] PARA CARREGAR JOGO: \n-> "))
                if play == 1:
                    self.criar_personagem()  # Permite criar novos personagens
                    break
                elif play == 2:
                    self.carregar_jogo()  # Carrega os personagens salvos
                    if len(self.personagens):
                        self.selecionar_personagem()  # Se houver personagens, o jogador escolhe qual usar
                    else:
                        print("Nenhum personagem salvo encontrado. Criando um novo personagem.")
                        self.criar_personagem()
                    break
                else:
                    print("Opção inválida")
            except ValueError or TypeError:
                print("invalido")

    def selecionar_personagem(self):
      while True:
         try:
            print("Lista de Personagens:\n")
            for i in range(len(self.personagens)):
                  print(f'#Save {i+1} -> aperte[{i+1}] para carrega-lo\nNome: {self.personagens[i].name}\nHp: {self.personagens[i].hp}\nAtk: {self.personagens[i].atk}\nFase atual: {self.personagens[i].fase} (fase 0 -> prologo)\n\n')
            escolha = int(input("aperte o numero correspondente ao personagem para seleciona-ló -> "))-1
            self.main_char = self.personagens[escolha]
            break
         except (IndexError, ValueError, TypeError):
             print("\ninput invalido")
      print("personagem selecionado com sucesso!\n")

    def criar_personagem(self):
        while self.main_char is None:
            try:
                personagem_pick = int(input("Escolha um personagem: Hero[1], Mage[2], Thief[3], Chaos[4]: "))
            except ValueError:
                print("Insira um número de 1 a 4")
                continue

            match personagem_pick:
                case 1:
                    name = input("Você escolheu ser herói, qual vai ser seu nome? -> ")
                    jogador = (Jogador(100, 7, 1, 0, 10, "espada comum",name))
                case 2:
                    name = input("Você escolheu ser mago! Qual vai ser seu nome? -> ")
                    jogador = (Jogador(70, 10, 1, 0, 10, "varinha de magica comum",name))
                case 3:
                    name = input("Você escolheu ser ladrão!! Qual vai ser seu nome? -> ")
                    jogador = (Jogador(80, 100, 1, 0, 30, "faca",name))
                case 4:
                    name = input("Você escolheu o Chaos! você sabe seu nome? -> ")
                    jogador = (Jogador(random.randint(0, 150), random.randint(0, 15), 1, 0, random.randint(0,30), "baralho de cartas mítico",name))
                case _:
                    print("Opção inválida")
                    continue

            self.main_char = jogador
            self.personagens.append(jogador)
            self.salvar_jogo()