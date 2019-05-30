# A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
# Within that sequence, he chooses two numbers, a and b.
# He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
# Given a number n, could you tell me the numbers he excluded from the sequence?
# The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:
#
# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
# with all (a, b) which are the possible removed numbers in the sequence 1 to n.
#
# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".
#
# It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).
#
# (See examples of returns for each language in "RUN SAMPLE TESTS")

def removNb(n):
    print(n)
    sum_list = sum(range(1,n+1))
    result = []
    for i in range(1,n+1):
        if (sum_list-i)%(i+1) == 0 and (sum_list-i)/(i+1) in range(1,n+1) and int((sum_list-i)/(i+1)) != i:
            result.append((i,int((sum_list-i)/(i+1))))

    return result

# OR

import math

def removNb(n):
    res = []
    tot = sum(range(n+1))
    for a in range(n,int(math.sqrt(tot)),-1):
        b = tot%a
        if a*b==tot-a-b:
            res.append((b,a))
            res.append((a,b))
    return sorted(res)