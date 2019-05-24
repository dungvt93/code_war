a = np.array([[1, 2, 3, 4],
              [12, 13, 14, 5],
              [11, 16, 15, 6],
              [10, 9, 8, 7]])

a = np.array([[1,2,3,4,5],
              [16,17,18,19,6],
              [15,24,25,20,7],
              [14,23,22,21,8],
              [13,12,11,10,9],
              ])
i = 1
result = []

while a.shape != (0,0):
    if i == 1:
        result.extend(a[0, :])
        a = a[1:,:]
    if i == 2:
        result.extend(a[:, -1])
        a = a[:,:-1]
    if i == 3:
        temp = a[-1, :]
        result.extend(temp[::-1])
        a = a[:-1,:]
    if i == 4:
        temp = a[:, 0]
        result.extend(temp[::-1])
        a = a[:,1:]
        i = 0
    i+=1
print(result)
