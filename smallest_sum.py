import time
import numpy as np
total = 0
def solution(a):

    #CASE 1
    temp = a[0]
    quantity = 1
    for i in a[1:]:
        temp = find_smallest_num(i, temp)
        quantity+=1
    return quantity * temp



def find_smallest_num(num_large, num_small):
    if num_large < num_small:
        num_large, num_small = num_small,num_large
    while num_large != num_small:
        so_du = num_large % num_small
        if so_du == 0:
            num_large = num_small
        else:
            num_large, num_small = num_small, so_du
    return num_small


for i in range(1000000):
    start = time.time()
    solution([6,9,21])
    total += time.time() -start
print(total)
