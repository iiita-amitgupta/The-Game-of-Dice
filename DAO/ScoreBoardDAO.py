from Models import ScoreBoard

class ScoreBoardDAO(object):
    record = {}

    def getBoard(self, boardId):
        return self.__class__.records[boardId]

    def setBoard(self, boardId, playerScores):
        boardObject = ScoreBoard()
        boardObject.setBoardId(boardId)
        boardObject.setPlayerScore(playerScores=playerScores)
        self.__class__.records[boardId] = boardObject


