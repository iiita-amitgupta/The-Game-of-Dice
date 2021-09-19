

class WinnerBoardDAO(object):
    records = {}

    def getWinnerPlayerList(self, boardId):
        return self.__class__.records[boardId]

    def setWinnerBoard(self, boardId, winnerBoardObj):
        self.__class__.records[boardId] = winnerBoardObj
        return winnerBoardObj

    def setWinnerPlayer(self, boardId, playerId):
        data = self.getWinnerPlayerList(boardId)
        data.setPlayer(playerId)
