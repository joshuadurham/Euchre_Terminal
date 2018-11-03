import game_params
from random import shuffle

class EuchreGame():

    teamOne = None
    teamTwo = None
    dealer = None
    roundNumber = None

    def __init__(self, teamOne, teamTwo):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.dealer = teamOne.playerOne
        self.roundNumber = 0


class Round():

    game = None
    cardPool = []
    roundState = None
    handWinners = []
    trumpSuit = None

    def __init__(self, game):
        self.cardPool = self.__shuffleCards__()

    def __shuffleCards__(self):
        for value in range(game_params.NUM_CARD_VALUES):
            for suit in range(game_params.NUM_CARD_SUITS):
                newCard = Card(value, suit)
                self.cardPool.append(newCard)
        shuffle(self.cardPool)
        

class Team():

    playerOne = None
    playerTwo = None
    score = None

    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.score = 0


class Player():

    name = None
    currentHand = []

    def __init__(self, name):
        self.name = name

class Card():

    value = None
    suit = None

    def __init__(self, value, suit):
        value = value
        suit = suit
