# test.assert_equals(has_exit(maze), True, "simplest case")
#
# maze = ["###",
#         "#k#",
#         "###"]
# test.assert_equals(has_exit(maze), False, "no exit case")
#
# maze = ["###",
#         "#k ",
#         "###"]
# test.assert_equals(has_exit(maze), True, "single exit case")
#
# maze = ["k ",
#         "kk"]
#
# test.expect_error("There should no be multiple Kates", lambda: has_exit(maze))
#
# test.describe("More difficult cases")
#
# maze = ["########",
#         "# # ####",
#         "# #k#   ",
#         "# # # ##",
#         "# # # ##",
#         "#      #",
#         "########"]
# test.assert_equals(has_exit(maze), True, "single exit big maze")
#
# maze = ["########",
#         "# # ## #",
#         "# #k#  #",
#         "# # # ##",
#         "# # #  #",
#         "#     ##",
#         "########"]
import numpy as np
def has_exit(maze):
    print(maze)
    matran = []
    out_door = []
    kate = None
    is_Kate = False
    for i,str in enumerate(maze):
        row = []
        for j,c in enumerate(str):
            if c == "#":
                row.append(1)
            elif c == " ":
                row.append(0)
                if i == 0 or j == 0 or i == len(maze)-1 or j == len(str)-1:
                    out_door.append((i,j))
            elif c == "k":
                if is_Kate:
                    raise Exception
                else:
                    if i == 0 or j == 0 or i == len(maze)-1 or j == len(str)-1:
                        out_door.append((i,j))
                    row.append(2)
                    kate = (i,j)
                    is_Kate = True
        matran.append(row)

    if not is_Kate:
        raise Exception
    return check_can_out(np.array(matran), kate, out_door)

def check_can_out(matran,kate,out_door):
    if kate in out_door:
        return True
    else:
        matran[kate[0]][kate[1]] = 1
        for num in (1,-1):
            try:
                if matran[kate[0]][kate[1]+num] == 0:
                    if check_can_out(matran,(kate[0],kate[1]+num), out_door):
                        return True

                if matran[kate[0]+num][kate[1]] == 0:
                    if check_can_out(matran,(kate[0]+num,kate[1]), out_door):
                        return True
            except IndexError:
                continue
        return False


# maze = ["########",
#         "# # ## #",
#         "# #k#  #",
#         "# # # ##",
#         "# # #  #",
#         "#     ##",
#         "########"]

# maze = ["########",
#         "# # ####",
#         "# #k#   ",
#         "# # # ##",
#         "# # # ##",
#         "#      #",
#         "########"]

maze = ['#########', '#k        #', '###########']
print(has_exit(maze))





