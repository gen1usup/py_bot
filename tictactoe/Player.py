

player_mark = '[x]'
comp_mark = "[o]"
empty_mark = "[ ]"


class Player:
    def __init__(self, name, mark):
        self.mark = mark
        self.name = name


class HumanPlayer(Player):
    def __init__(self, name, mark):
        self.mark = mark
        self.name = name

    def turn(self, field):
        coordinate_x = list(input())
        field[int(coordinate_x[0]) - 1][int(coordinate_x[1]) - 1] = self.mark
        return field


class CompPlayer():
    def __init__(self, name, mark):
        self.mark = mark
        self.name = name

    def turn(self, field):

        for stroka in range(3):
            if field[stroka][1] == field[stroka][0] == player_mark:
                if field[stroka][2] != comp_mark and field[stroka][2] == empty_mark:
                    field[stroka][2] = comp_mark
                    return field
            if field[stroka][1] == field[stroka][2] == player_mark:
                if field[stroka][0] != comp_mark and field[stroka][0] == empty_mark:
                    field[stroka][0] = comp_mark
                    return field
            if field[stroka][0] == field[stroka][2] == player_mark:
                if field[stroka][1] != comp_mark and field[stroka][1] == empty_mark:
                    field[stroka][1] = comp_mark
                    return field

        for stolbec in range(3):
            if field[1][stolbec] == field[0][stolbec] == player_mark:
                if field[2][stolbec] != comp_mark and field[2][stolbec] == empty_mark:
                    field[2][stolbec] = comp_mark
                    return field
            if field[1][stolbec] == field[2][stolbec] == player_mark:
                if field[0][stolbec] != comp_mark and field[0][stolbec] == empty_mark:
                    field[0][stolbec] = comp_mark
                    return field
            if field[0][stolbec] == field[2][stolbec] == player_mark:
                if field[1][stolbec] != comp_mark and field[1][stolbec] == empty_mark:
                    field[1][stolbec] = comp_mark
                    return field

        for i in range(0, 3, 2):
            if field[2 - i][2 - i] == field[1][1] == player_mark:
                if field[0 + i][0 + i] != comp_mark and field[0 + i][0 + i] == empty_mark:
                    field[0 + i][0 + i] = comp_mark
                    return field
            if field[2 - i][0 + i] == field[1][1] == player_mark:
                if field[0 + i][2 - i] != comp_mark and field[0 + i][2 - i] == empty_mark:
                    field[0 + i][2 - i] = comp_mark
                    return field

        for k in range(3):
            for p in range(3):
                if field[k][p] == empty_mark:
                    field[k][p] = comp_mark
                    return field
