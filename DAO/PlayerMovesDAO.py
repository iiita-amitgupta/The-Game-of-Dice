from Models import PlayerMoves


class PlayerMoveDAO(object):
    records = {}

    def getPlayerMove(self, playerId):
        return self.__class__.records[playerId]

    def setPlayerMove(self, playerId, playerObject):
        self.__class__.records[playerId] = playerObject
        return playerObject

    def updatePlayerMove(self, playerId, currMove, currScore):
        playerObject = self.getPlayerMove(playerId)
        playerObject.setLastMove(playerObject.getCurrMove())
        playerObject.setCurrMove(currMove)
        playerObject.setCurrScore(currScore)

