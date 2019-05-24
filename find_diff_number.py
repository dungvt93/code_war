def diff_number(numbers):
    temp = [int(x) % 2 for x in numbers.split(" ")]
    return temp.index(0) + 1 if temp.count(0) == 1 else temp.index(1) +1


print(diff_number("5 1 3 3 6"))