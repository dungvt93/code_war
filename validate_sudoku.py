import numpy as np
import math
class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.shape = np.array(self.data).shape
    def is_valid(self):
        if len(self.shape) != 2 or self.shape[0] != self.shape[1] or math.sqrt(self.shape[0]).is_integer() != True:
            print('1')
            return False

        for test in self.data:
            if all(type(n) == int for n in test) == False:
                return False
        self.data = np.array(self.data)
        square_row = 0
        square_column = 0
        square_size = int(math.sqrt(self.shape[0]))
        for i in range(0,self.shape[0]):
            column = self.data[i,:]
            row = self.data[:,i]

            # check row and column
            if len(np.where((column <= 0) |  (column > self.shape[0]))[0]) > 0:
                print('2')
                return False
            if len(np.where((row <= 0) |  (row > self.shape[0]))[0]) > 0:
                print('3')
                return False
            if len(set(column)) != len(column) or len(set(row)) != len(row):
                print('4')
                return False

            # check square
            flatten_x = np.concatenate(self.data[square_row:square_row+square_size,square_column:square_column+square_size])
            if (len(set(flatten_x)) != len(flatten_x)):
                return  False
            square_column += square_size
            if square_column > self.shape[0]:
                square_column = 0
                square_row += square_size
        return True

