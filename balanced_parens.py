# Viết hàm tạo danh sách các chuỗi đại diện cho tất cả các cách bạn có thể cân bằng n cặp ngoặc đơn
# Examples
# balancedParens(0) returns ArrayList<String> with element:  ""
# balancedParens(1) returns ArrayList<String> with element:  "()"
# balancedParens(2) returns ArrayList<String> with
#     elements: "()()","(())"
# balancedParens(3) returns ArrayList<String> with elements: "()()()","(())()","()(())","(()())","((()))"

import itertools
def create_list(number):
    result = []
    for i in range(number):
        result.append(1)
        result.append(-1)
    temp = list(itertools.permutations(result))
    return list(set(temp))


def filter_pattern(input):
    result = input.copy()
    for pattern in input:
        cal = 0
        for elm in pattern:
            cal += int(elm)
            if cal < 0:
                # print(pattern)
                result.remove(pattern)
                break
    return  result

def print_pattern(input):
    for pattern in input:
        str_result = ""
        for elm in pattern:
            if elm == 1:
                str_result += "("
            if elm == -1:
                str_result += ")"
        print(str_result)

def balanced_parens(n):
    input = create_list(n)
    pattern = filter_pattern(input)
    print_pattern(pattern)

balanced_parens(4)


#answer
result = []
def brackets(result, open_stock, close_stock, str):
    if open_stock == 0 and close_stock == 0:
        result.append(str)

    if open_stock > 0:
        brackets(result,open_stock-1,close_stock+1, str +"(")

    if close_stock > 0:
        brackets(result,open_stock,close_stock-1, str +")")

brackets(result,4,0,"")
print(len(result))

