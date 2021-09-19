class PlayerMoves(object):

    def __init__(self):
        self.Id = None
        self.lastMove = None
        self.currMove = None
        self.currScore = 0

    def getId(self):
        return self.Id

    def setId(self, Id):
        self.Id = Id

    def getLastMove(self):
        return self.lastMove

    def setLastMove(self, lastMove):
        self.lastMove = lastMove

    def getCurrMove(self):
        return self.currMove

    def setCurrMove(self, currMove):
        self.currMove = currMove

    def getCurrScore(self):
        return self.currScore

    def setCurrScore(self, currScore):
        self.currScore = currScore
