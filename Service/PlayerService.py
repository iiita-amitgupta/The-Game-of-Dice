from Models.Player import Player

class PlayerService():

    playerDaoObject = None

    def __init__(self, playerDaoObject):
        self.playerDaoObject = playerDaoObject

    def createPlayers(self, N):
        for player in range(1, N+1):
            playerId = "player_"+ str(player)
            playerName = "PLAYER_" + str(player)
            playerObj = Player()
            playerObj.setPlayerId(playerId)
            playerObj.setPlayerName(playerName)
            self.playerDaoObject.createPlayerRecord(playerId, playerObj)
        return self.playerDaoObject.getListOfPlayers()



