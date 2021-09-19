from Models import Player


class PlayerDAO(object):
    records = {}

    def getPlayerRecord(self, playerId):
        return self.__class__.records[playerId]

    def createPlayerRecord(self, playerId, playerObj):
        self.__class__.records[playerId] = playerObj
        return playerObj

    def getListOfPlayers(self):
        listOfPlayer = []
        for key, value in self.__class__.records.items():
            listOfPlayer.append((key))
        return listOfPlayer
