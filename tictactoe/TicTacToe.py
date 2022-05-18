from Player import HumanPlayer, CompPlayer

player_mark = '[x]'
comp_mark = "[o]"
empty_mark = "[ ]"

class TicTacToe:
    def __init__(self, player2):
        player1 = HumanPlayer
        if player2 == "comp":
            player2 = CompPlayer
        else:
            player2 = HumanPlayer
        self.field = [[empty_mark for j in range(3)] for i in range(3)]

    def game_process(self):
        pass

    def win_calc(field):
        if field[0][0] == field[1][1] == field[2][2] != empty_mark:
            return True
        if field[2][0] == field[1][1] == field[0][2] != empty_mark:
            return True
        for i in range(3):
            if field[i][0] == field[i][1] == field[i][2] != empty_mark:
                return True
            if field[0][i] == field[1][i] == field[2][i] != empty_mark:
                return True
        return False