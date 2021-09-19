from random import random
from Models.Dice import Dice
import random
import copy


class GameService():
    gameId = None
    orderPlayerTurn = None
    playerServiceObj = None
    playerMoveServiceObj = None
    targetScore = None
    winnerBoardService = None

    def __init__(self, gameID, playerServiceObj, playerMoveServiceObj, targetScore, boardService, winnerBoardService):
        self.gameId = gameID
        self.playerServiceObj = playerServiceObj
        self.playerMoveServiceObj = playerMoveServiceObj
        self.targetScore = targetScore
        self.boardService = boardService
        self.winnerBoardService = winnerBoardService

    def orderPlayerTurn(self, listOfPlayer):
        random.shuffle(listOfPlayer)
        self.orderPlayerTurn = listOfPlayer
        return listOfPlayer

    def startGame(self):

        listOfPlayers = copy.deepcopy(self.orderPlayerTurn)
        winnerBoardId = self.winnerBoardService.createWinnerBoard("board_1")

        listTurnPlayerWithFlag = {}
        for player in listOfPlayers:
            listTurnPlayerWithFlag[player] = True

        processFlag = True
        while processFlag:

            for playerId in listTurnPlayerWithFlag:
                #rolling dice

                if listTurnPlayerWithFlag[playerId] is True:
                    diceOutcome = Dice.rollDice()
                    playerCurrMoveStatus = self.playerMoveServiceObj.getPlayerMoveStatus(playerId)

                    lastMove = playerCurrMoveStatus.getLastMove()
                    newScore = playerCurrMoveStatus.getCurrScore() + diceOutcome
                    if newScore <= self.targetScore:
                        playerCurrMoveStatus.setCurrScore(newScore)

                    self.boardService.getBoardStatus()
                    if newScore == self.targetScore:
                        listTurnPlayerWithFlag[playerId] = False
                        self.winnerBoardService.setWinnerBoard(winnerBoardId, playerId)
                        print("{} Won".format(playerId))

                    if diceOutcome == 1 and lastMove == 1:
                        continue

                    while diceOutcome == 6 and newScore < self.targetScore:
                        diceOutcome = Dice.rollDice()
                        self.boardService.getBoardStatus()
                        newScore = playerCurrMoveStatus.getCurrScore() + diceOutcome
                        if newScore <= self.targetScore:
                            playerCurrMoveStatus.setCurrScore(newScore)

                        if newScore == self.targetScore:
                            listTurnPlayerWithFlag[playerId] = False
                            self.winnerBoardService.setWinnerBoard(winnerBoardId, playerId)
                            print("{} Won\n".format(playerId))

                    playerCurrMoveStatus.setLastMove(diceOutcome)
                    
            processFlag = False
            for key, value in listTurnPlayerWithFlag.items():
                if value is True:
                    processFlag = True

        ranksOfWinners = self.winnerBoardService.getWinnerList(winnerBoardId).getWinnerPlayers()
        count = 1
        print("\n@@@@@@ Final Score Board Ranking of Winner @@@@@\n")
        for playerId in ranksOfWinners:
            print("\t \t Rank {} = {}".format(playerId, count))
            count = count + 1








