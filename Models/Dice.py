import random


class Dice(object):

    def __init__(self):
        self.diceId = None
        self.lastDiceMove = None

    def getId(self):
        return self.diceId

    def setId(self, diceId):
        self.diceId = diceId

    def getLastDiceMove(self):
        return self.lastDiceMove

    def setLastDiceMove(self, lastDiceMove):
        self.lastDiceMove = lastDiceMove

    @staticmethod
    def rollDice():
        return random.randint(1, 6)
