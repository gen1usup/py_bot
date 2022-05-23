from TicTacToe import TicTacToe
from Player import HumanPlayer, CompPlayer

ttt = TicTacToe(HumanPlayer("Дима1", "[x]"), CompPlayer("Компьютер", "[o]"))
# print(ttt.field)
ttt.game_start()
