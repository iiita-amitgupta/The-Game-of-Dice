from Models.WinnerBoard import WinnerBoard

class WinnerBoardService(object):

    def __init__(self, winnerBoardDaoObject):
        self.winnerBoardDaoObject = winnerBoardDaoObject

    def getWinnerList(self, boardId):
        return self.winnerBoardDaoObject.getWinnerPlayerList(boardId)

    def createWinnerBoard(self, boardId):
        winnerBoardObj = WinnerBoard()
        winnerBoardObj.setId(boardId)
        self.winnerBoardDaoObject.setWinnerBoard(boardId, winnerBoardObj)
        return boardId

    def setWinnerBoard(self, boardId, playerId):
        self.winnerBoardDaoObject.setWinnerPlayer(boardId, playerId)
