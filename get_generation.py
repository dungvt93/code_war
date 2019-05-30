# Conway's Game of Life - Unlimited Edition
# Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.
#
# The rules of the game are:
#
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell.
# Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)
#
# For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:
#
# print htmlize(cells)
# trace (htmlize cells)

from copy import copy, deepcopy
def get_generation(cells, generations):
    print(cells,generations)
    result = deepcopy(cells)
    for time in range(generations):
        base = deepcopy(result)
        print(base)
        for i in range(len(base)):
            for j in range(len(base[i])):
                result[i][j] = check(base,i,j)
    print(result)
    return result

def check(base,i,j):
    neighbours = []
    for m in [-1,0,1]:
        for n in [-1,0,1]:
            if m == 0 and n ==0 :
                continue
            if i+m < 0 or j+n < 0 or i+m >= len(base) or j+n >= len(base[i]):
                neighbours.append(0)
            else:
                neighbours.append(base[i+m][j+n])
    #     print(neighbours)
    #     exit()
    if base[i][j] == 1:
        if neighbours.count(1) == 2 or neighbours.count(1) == 3:
            return 1
        else:
            return 0
    if base[i][j] == 0:
        if neighbours.count(1) == 3:
            return 1
        else:
            return 0
test = [[0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]]
# test = [[1, 0, 0],
#         [0, 1, 1],
#         [1, 1, 0]]
print(check(test,1,1))