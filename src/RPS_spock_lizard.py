
class GameAction:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    SPOCK = 3
    LIZARD = 4

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