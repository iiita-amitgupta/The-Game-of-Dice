class WinnerBoard(object):

    def __init__(self):
        self.winnerBoardId = None
        self.playerList = []

    def getId(self):
        return self.winnerBoardId

    def setId(self, winnerBoardId):
        self.winnerBoardId = winnerBoardId

    def getWinnerPlayers(self):
        return self.playerList

    def setPlayer(self, playerId):
        self.playerList.append(playerId)
        return self.playerList