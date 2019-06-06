# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
#
# such as
#
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
#
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
#
# F(n) * F(n+1) = prod.
#
# Your function productFib takes an integer (prod) and returns an array:
#
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
#
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
#
# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.
#
# Examples
# productFib(714) # should return [21, 34, true],
# # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
#
# productFib(800) # should return [34, 55, false],
# # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34
def productFib(prod):
    a =[0,1]
    while True:
        if a[1] * a[0] == prod:
            return [a[0],a[1],True]
        elif a[0] * a[1] > prod:
            return [a[0],a[1],False]
        a[0] = a[1]
        a[1] = a[0] + a[1]

def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

def productFib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)