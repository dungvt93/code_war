# Given an array of positive or negative integers
#
# I= [i1,..,in]
#
# you have to produce a sorted array P of the form
#
# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
#
# P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.
#
# Example:
#
# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

import numpy as np
def sum_for_list(lst):

    result = []
    lst = np.array(lst)
    prime_list = find_prime_factors(lst)
    prime_list.sort()

    for prime in prime_list:
        list_total = np.where(lst % prime == 0, lst, 0)
        total = sum(list_total[0:len(list_total)])
        result.append([prime,total])
    return result


def find_prime_factors(lst):
    result = []
    for number in lst:
        i = 2
        if number < 0:
            number = -number
        while(number >= i*i):
            if number % i == 0:
                number = number / i
                if i not in result:
                    result.append(int(i))
                i = 2
            else:
                i += 1
        if number not in result:
            result.append(int(number))
    return result