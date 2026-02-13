import random


class GameAction:
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"
    SPOCK = "SPOCK"
    LIZARD = "LIZARD"

    valid_actions = [ROCK, PAPER, SCISSORS, SPOCK, LIZARD]

class GameResult:
    DEFEAT = 0
    TIE = 1
    VICTORY = 2 
    
class Game:
    

    victories = {
        GameAction.ROCK: [GameAction.SCISSORS, GameAction.LIZARD],
        GameAction.PAPER: [GameAction.ROCK, GameAction.SPOCK],
        GameAction.SCISSORS: [GameAction.PAPER, GameAction.LIZARD],
        GameAction.LIZARD: [GameAction.SPOCK, GameAction.PAPER],
        GameAction.SPOCK: [GameAction.SCISSORS, GameAction.ROCK],
    }

    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            print("Empate")
            return GameResult.TIE

        if computer_action in self.victories[user_action]:
            
            print(f"Victoria: {user_action} vence a {computer_action}")
            return GameResult.VICTORY

        print(f"Derrota: {computer_action} vence a {user_action}")
        return GameResult.DEFEAT

    def user_action(self):
        
        valid_input = False
        while valid_input == False:
            user_action = input("Selecciona una de las siguientes opciones:'ROCK', 'PAPER', 'SCISSORS', 'SPOCK', 'LIZARD': ").upper()
            if user_action in GameAction.valid_actions:
                valid_input = True
                return user_action
            else:
                print("Acción denegada, inserte una opción válida")


    def computer_action(self):
        computer_action = random.choice(GameAction.valid_actions)
        print(f"Seleccion de la máquina: {computer_action}")
        return computer_action
    
    def replay():
        pass

    def play(self):
        computer = self.computer_action()
        user = self.user_action()
        
        

if __name__ == "__main__":
    
    game = Game()
    game.play()