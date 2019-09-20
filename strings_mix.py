import re
from functools import cmp_to_key
def mix(s1, s2):
    print(s1)
    print(s2)
    dict_temp = {}
    for c in s1+s2:
        if c.isalpha() and not c.istitle():
            if c in dict_temp:
                dict_temp[c] += 1
            else:
                dict_temp[c] = 1
    result = []
    for key,value in dict_temp.items():
        val1 = s1.count(key)
        if value == 1 or val1==(value-val1)==1:
            continue
        if val1 > value - val1:
            result.append("1:"+key*val1 +"/")
        elif val1 == value - val1:
            result.append("=:"+key*val1 +"/")
        elif val1 < value - val1:
            result.append("2:"+key*(value-val1) +"/")
    result = sorted(result, key=cmp_to_key(compair))
    return ''.join(result)[:-1]

def compair(a,b):
    if len(a) != len(b):
        return -1 if len(a) > len(b) else 1
    else:
        return -1 if a < b else 1

#OR

from collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                       ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))
