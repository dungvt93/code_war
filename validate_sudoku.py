
import numpy as np
class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.shape = np.array(self.data).shape
    def is_valid(self):
        if len(self.shape) != 2 or self.shape[0] != self.shape[1]:
            print('1')
            return False

        for test in self.data:
            if all(type(n) == int for n in test) == False:
                return False
        self.data = np.array(self.data)
        for i in range(0,self.shape[0]):
            column = self.data[i,:]
            row = self.data[:,i]
            if len(np.where((column <= 0) |  (column > self.shape[0]))[0]) > 0:
                print('2')
                return False

            if len(np.where((column <= 0) |  (column > self.shape[0]))[0]) > 0:
                print('3')
                return False

            if len(set(self.data[i,:])) != len(self.data[i,:]) or len(set(self.data[:,i])) != len(self.data[:,i]):
                print('4')
                return False
        return True

goodSudoku1 = Sudoku([
    [7,8,4, 1,5,9, 3,2,6],
    [5,3,9, 6,7,2, 8,4,1],
    [6,1,2, 4,3,8, 7,5,9],

    [9,2,8, 7,1,5, 4,6,3],
    [3,5,7, 8,4,6, 1,9,2],
    [4,6,1, 9,2,3, 5,8,7],

    [8,7,6, 3,9,4, 2,1,5],
    [2,4,3, 5,6,1, 9,7,8],
    [1,9,5, 2,8,7, 6,3,4]
])
print(goodSudoku1.is_valid())