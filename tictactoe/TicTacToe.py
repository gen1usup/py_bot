from Player import HumanPlayer, CompPlayer

player_mark = '[x]'
comp_mark = "[o]"
empty_mark = "[ ]"


class TicTacToe:


    def __init__(self, player1, player2):

        self.player1 = player1
        # if player2.name == "Comp":
        #     self.player2 = player2
        #     self.player2.name = "Компьютер"
        # else:
        self.player2 = player2
        self.is_win = False
        self.field = [["[ ]" for j in range(3)] for i in range(3)]


    def game_process_with_human(self):
        print("Начало игры двух людей")
        turn_que = 1
        while self.is_win != True:
            # print(self.field)
            if turn_que == 1:
                print("Ход игрока " + self.player1.name)
                self.print_field()
                self.field = self.player1.turn(self.field)
                turn_que = 2
            else:
                print("Ход игрока " + self.player2.name)
                self.print_field()
                self.field = self.player2.turn(self.field)
                turn_que = 1

            self.is_win = self.win_calc()

    def game_process_with_comp(self):
        print("Начало игры с компьютером")
        turn_que = 1
        while self.is_win != True:
            # self.print_field()
            if turn_que == 1:
                print("Ход игрока " + self.player1.name)
                self.print_field()
                self.field = self.player1.turn(self.field)
                turn_que = 2
            else:
                print("Ход компьютера")
                self.field = self.player2.turn(self.field)
                turn_que = 1

            self.is_win = self.win_calc()


    def game_start(self):
        # print(self.field)
        if isinstance(self.player2, CompPlayer):
            self.game_process_with_comp()
        else:
            self.game_process_with_human()

    def win_calc(self):
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != empty_mark:
            self.print_field()
            print("Победа " + list(self.field[1][1])[1])
            return True
        if self.field[2][0] == self.field[1][1] == self.field[0][2] != empty_mark:
            self.print_field()
            print("Победа " + list(self.field[1][1])[1])
            return True
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != empty_mark:
                self.print_field()
                print("Победа " + list(self.field[i][1])[1])
                return True
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != empty_mark:
                self.print_field()
                print("Победа " + list(self.field[1][i])[1])
                return True
        return False

    def print_field(self):
        for i in range(3):
            for j in range(3):
                print(str(self.field[i][j]) + " ", end='')
            print()



