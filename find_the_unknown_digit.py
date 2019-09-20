import re
def solve_runes(runes):
    print(runes)
    pattern1 =  '([-,+,=,*]+[?]{1}[0-9,?])'
    pattern2 =  '(^[?]{1}[0-9,?])'
    number_test = [0,1,2,3,4,5,6,7,8,9]
    result1 = re.search(pattern1, runes)
    result2 = re.search(pattern2, runes)
    if result1 is not None or result2 is not None:
        print('vao')
        number_test.remove(0)
    for i in number_test:
        if str(i) in runes:
            continue
        test = runes.replace("?",str(i))
        test = test.split('=')
        if eval(test[0]) == int(test[1]):
            return i
    return -1


# OR


def solve_runes(runes):
    for d in sorted(set("0123456789") - set(runes)):
        toTest = runes.replace("?",d)
        if re.search(r'([^\d]|\b)0\d+', toTest): continue
        l,r = toTest.split("=")
        if eval(l) == eval(r): return int(d)
    return -1