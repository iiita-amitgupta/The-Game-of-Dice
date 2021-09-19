

from Service.PlayerService import PlayerService
from DAO.PlayerDAO import PlayerDAO
from DAO.WinnerBoardDAO import WinnerBoardDAO
from Service.PlayerMovesService import PlayerMoveService
from DAO.PlayerMovesDAO import PlayerMoveDAO

from Service.GameService import GameService
from Service.BoardService import BoardService
from Service.WinnerBoardService import WinnerBoardService
def programDriver():
    print("!!@@.......... Game Started ........@@@!!\n")
    print("!!........... Initialize Game .........!!\n")

    N = 5  #int(input("Please Enter Number of Players\n"))
    M = 10 #int(input("Please Enter Target Points\n"))

    playerServiceObj = PlayerService(PlayerDAO())
    playerList = playerServiceObj.createPlayers(N)
    print("List of Player")
    print(playerList)

    playerMoveObj = PlayerMoveService(PlayerMoveDAO())
    playerMoveObj.initPlayerMove(playerList)
    playerObj = playerMoveObj.getPlayerMoveStatus("player_1")


    boardServiceObj = BoardService(PlayerMoveService(PlayerMoveDAO()))
    boardServiceObj.setListPlayerMove(playerList)

    gameObj = GameService("game_1",
                          PlayerService(PlayerDAO()),
                          PlayerMoveService(PlayerMoveDAO()),
                          M,
                          boardServiceObj,
                          WinnerBoardService(WinnerBoardDAO()))
    gameObj.orderPlayerTurn(playerList)
    print("\nTurn order of players")
    print(playerList)
    gameObj.startGame()






if __name__ == '__main__':
    programDriver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Roll dice randomly
# Round-Robin turn of player
# Press r to continue rolling die for next player
# if current dice-value is 6, then same player roll the dice
# if current player dice is 1 and prev roll dice is also 1 then next turn skips
