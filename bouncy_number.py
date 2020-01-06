def bouncy_count(number):
    if number < 3:
        return 0
    total = 10**number
    increase = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #end with 0,1,2,3,4,5,6,7,8,9
    for i in range(3,number+1):
        increase_temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(10):
            increase_temp[j] += sum(increase[0:j+1])
        increase = increase_temp
    return total - sum(increase)*2 + 10



# total = 0
# number = []
# for i in range(1000):
#     number.append('%03d'%i)
#
# for i in number:
#     if int(i[0]) <= int(i[1]) <= int(i[2]):
#         total+= 1
# print(total)

print(bouncy_count(4)) #525