import game_model

class GameController():
    gameModel = None

    def __init__(self, teamOne, teamTwo):
        self.gameModel = game_model.EuchreGame(teamOne, teamTwo)

    def checkIfWinner(self):
        return True
        # self.__gameModel


class RoundController():

    roundModel = None

    def __init__(self, game):
        self.roundModel = game_model.Round(game)

# class PlayerController():

