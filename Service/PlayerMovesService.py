from Models.PlayerMoves import PlayerMoves

class PlayerMoveService():

    playerMoveDoaObj = None

    def __init__(self, playerMoveDoaObj):
        self.playerMoveDoaObj = playerMoveDoaObj

    def initPlayerMove(self, listOfPlayers):
        for playerId in listOfPlayers:
            playerMovObj = PlayerMoves()
            playerMovObj.setId(playerId)
            playerMovObj.setLastMove(None)
            playerMovObj.setCurrMove(None)
            playerMovObj.setCurrScore(0)
            self.playerMoveDoaObj.setPlayerMove(playerId, playerMovObj)


    def getPlayerMoveStatus(self, playerId):
        obj = self.playerMoveDoaObj.getPlayerMove(playerId)
        return obj




