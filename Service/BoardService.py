class BoardService():

    listOfPlayerMoves = []

    def __init__(self, playerMoveService):
        self.playerMoveService = playerMoveService

    def setListPlayerMove(self, playerMove):
        self.listOfPlayerMoves = playerMove

    def getBoardStatus(self):
        print("\nShowing Board Status")
        for playerId in self.listOfPlayerMoves:

            playerMoveObj = self.playerMoveService.getPlayerMoveStatus(playerId)
            print("{} = {}".format(playerId, playerMoveObj.currScore))
