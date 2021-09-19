class ScoreBoard(object):

    def __init__(self):
        self.scoreBoardId = None
        self.playerScores = {}

    def getBoardId(self):
        return self.scoreBoardId

    def setBoardId(self, scoreBoardId):
        self.scoreBoardId = scoreBoardId

    def getPlayersScore(self):
        return self.playerScores

    def setPlayerScore(self, playerScores):
        self.playerScores = playerScores
