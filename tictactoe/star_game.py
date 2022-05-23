#
#
# player_mark = '[x]'
# comp_mark = "[o]"
# empty_mark = "[ ]"
#
# field = [[empty_mark for j in range(3)] for i in range(3)]
#
# def print_field():
#     for i in range(3):
#         for j in range(3):
#             print(str(field[i][j]) + " ", end='')
#         print()
#
#
# def win_calc(field):
#     if field[0][0] == field[1][1] == field[2][2] != empty_mark:
#         print("Победа " + list(field[1][1])[1])
#         return True
#     if field[2][0] == field[1][1] == field[0][2] != empty_mark:
#         print("Победа " + list(field[1][1])[1])
#         return True
#     for i in range(3):
#         if field[i][0] == field[i][1] == field[i][2] != empty_mark:
#             print("Победа " + list(field[i][1])[1])
#             return True
#         if field[0][i] == field[1][i] == field[2][i] != empty_mark:
#             print("Победа " + list(field[1][i])[1])
#             return True
#     return False
#
# def turn(field):
#     for stroka in range(3):
#         if field[stroka][1] == field[stroka][0] == player_mark:
#             if field[stroka][2] != comp_mark and field[stroka][2] == empty_mark:
#                 field[stroka][2] = comp_mark
#                 return field
#         if field[stroka][1] == field[stroka][2] == player_mark:
#             if field[stroka][0] != comp_mark and field[stroka][0] == empty_mark:
#                 field[stroka][0] = comp_mark
#                 return field
#         if field[stroka][0] == field[stroka][2] == player_mark:
#             if field[stroka][1] != comp_mark and field[stroka][1] == empty_mark:
#                 field[stroka][1] = comp_mark
#                 return field
#
#     for stolbec in range(3):
#         if field[1][stolbec] == field[0][stolbec] == player_mark:
#             if field[2][stolbec] != comp_mark and field[2][stolbec] == empty_mark:
#                 field[2][stolbec] = comp_mark
#                 return field
#         if field[1][stolbec] == field[2][stolbec] == player_mark:
#             if field[0][stolbec] != comp_mark and field[0][stolbec] == empty_mark:
#                 field[0][stolbec] = comp_mark
#                 return field
#         if field[0][stolbec] == field[2][stolbec] == player_mark:
#             if field[1][stolbec] != comp_mark and field[1][stolbec] == empty_mark:
#                 field[1][stolbec] = comp_mark
#                 return field
#
#     for i in range(0, 3, 2):
#         if field[2 - i][2 - i] == field[1][1] == player_mark:
#             if field[0 + i][0 + i] != comp_mark and field[0 + i][0 + i] == empty_mark:
#                 field[0 + i][0 + i] = comp_mark
#                 return field
#         if field[2 - i][0 + i] == field[1][1] == player_mark:
#             if field[0 + i][2 - i] != comp_mark and field[0 + i][2 - i] == empty_mark:
#                 field[0 + i][2 - i] = comp_mark
#                 return field
#
#     for k in range(3):
#         for p in range(3):
#             if field[k][p] == empty_mark:
#                 field[k][p] = comp_mark
#                 return field
#
#
# print_field()
# win = False
# while not win:
#     coordinate_x = list(input())
#     field[int(coordinate_x[0]) - 1][int(coordinate_x[1]) - 1] = player_mark
#     field = turn(field)
#     print_field()
#     win = win_calc(field)
#
# print("Победа!")
#
#
#
#
#
