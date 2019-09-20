import numpy as np
def part(n):
    result_set = set()
    enum_rs = enum(n)
    for ar in enum_rs:
        new_val = np.prod(ar)
        result_set.add(new_val)
    result_prod = np.array(list(sorted(result_set)))
    mean = np.mean(result_prod)
    range = result_prod[-1]  - result_prod[0]
    if len(result_prod) % 2 != 0:
        median = result_prod[int(len(result_prod)/2)]
    else:
        median = (result_prod[int(len(result_prod)/2)] + result_prod[int(len(result_prod)/2) - 1] ) / 2
    return "Range: %i Average: %.2f Median: %.2f" % (range, mean, median)

def enum(n):
    result_n = []
    if n == 1:
        result_n.append([1])
        return result_n
    else:
        for i in range(1,n):
            for temp in enum(n-i):
                temp.append(i)
                temp.sort()
                if temp not in result_n:
                    result_n.append(temp)
        result_n.append([n])
        return result_n


#dap an

def prod(n):
    ret = [{1.}]
    for i in range(1, n+1):
        ret.append({(i - x) * j for x, s in enumerate(ret) for j in s})
    return ret[-1]

def part(n):
    p = sorted(prod(n))
    return "Range: %d Average: %.2f Median: %.2f" % \
           (p[-1] - p[0], sum(p) / len(p), (p[len(p)//2] + p[~len(p)//2]) / 2)

