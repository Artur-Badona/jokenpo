import time
import random

#Classe Jogador
class Jogador:
    def __init__(self, username):
        self.username = username
        self.score = 0

#Classe Jogo
class Jogo:
    def __init__(self, player):
        self.player = player
        self.computer_score = 0
        self.title = r'''
       _  ____  _  ________ _   _ _____   ____  
      | |/ __ \| |/ /  ____| \ | |  __ \ / __ \ 
      | | |  | | ' /| |__  |  \| | |__) | |  | |
  _   | | |  | |  < |  __| | . ` |  ___/| |  | |
 | |__| | |__| | . \| |____| |\  | |    | |__| |
  \____/ \____/|_|\_\______|_| \_|_|     \____/                                        
        '''

    #Exibe as opções para o jogador e retorna a escolhida
    def player_choice(self):
        choices = {"1" : "pedra", "2" : "papel", "3" : "tesoura", "4" : "sair"}
        print("Faça sua escolha:\n1. Pedra\n2. Papel\n3. Tesoura\n4. Sair")
        while True:
            choice = input(5*"\n")
            if choice not in choices:
                print("Escolha inválida. Tente novamente (1, 2, 3 ou 4)")
            else:
                if choice == "4":
                    print("Obrigado por jogar!")
                    print("Saindo do jogo...")
                    time.sleep(0.5)
                    quit()
                return choices[choice]
    
    #Analisa a escolha do jogador e do computador e determina o vencedor ou empate
    def get_winner(self, player_choice, computer_choice):
        rules = {
            "pedra" : "tesoura",
            "papel" : "pedra",
            "tesoura" : "papel"
        }

        if player_choice == computer_choice:
            return "draw"
        elif rules[player_choice] == computer_choice:
            return "player"
        else:
            return "computer"

    #Adiciona um ponto ao vencedor
    def score_winner(self, winner):
        if winner == "player":
            self.player.score += 1
            return print("Você Venceu!")
        elif winner == "computer":
            self.computer_score += 1
            return print("Você perdeu :(")
        else:
            return print("Empate! Jogue novamente")

    #Inicia uma nova partida caso o jogador queira
    def play_again(self):
        while True:
            choice = input("Jogar novamente? (s/n) ").lower()
            if choice == "s":
                self.start_game()
            elif choice == "n":
                print("Obridado por jogar!")
                print("Saindo do jogo...")
                time.sleep(0.5)
                quit()
            else:
                print("Escolha inválida. Tente novamente ('s' ou 'n')")

    def jokenpo(self):
        time.sleep(0.3)
        print("\nJO ", end='', flush=True)
        time.sleep(0.3)
        print("KEN ", end='', flush=True)
        time.sleep(0.2)
        print("PÔ!")
        time.sleep(0.1)

    #Inicia a função principal do jogo
    def start_game(self):
        print(9*"\n" + self.title)
        print(f"\n{self.player.username}: {self.player.score}                           Computador: {self.computer_score}")

        player_choice = self.player_choice()
        computer_choice = random.choice(["pedra", "papel", "tesoura"])

        winner = self.get_winner(player_choice, computer_choice)
        self.jokenpo()
        self.score_winner(winner)
        print(f"Você escolheu {player_choice} e o computador escolheu {computer_choice}")
        self.play_again()



user = input("Defina um username: ")
player = Jogador(user)

Jogo(player).start_game()