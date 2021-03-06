import random
import time
def spinning_rings(inner_max, outer_max):
    i = inner_max + 1
    j = outer_max + 1
    x =1
    while True:
        a = -x%i
        b = x%j
        if a==b:
            return x
        elif a > b:
            if a > j:
                x+= a-j
            else:
                if a-b ==1:
                    x+= min(a+1,j-b)
                else:
                    x+= max((a-b)//2,1)
        elif a < b:
            if  b > i:
                x+=j-b
            else:
                x+= max(min(a+1,j-b),1)

def spinning_rings2(inner_max, outer_max):

    i = inner_max+1
    j = outer_max+1

    x = 1
    while x < i*j:
        a = -x % i
        b = x % j
        if a == b:
            return x
        elif a > b:
            if a > j:
                x += a-j
            else:
                x+= max((a-b)//2,1)
        elif b > a:
            if b > i:
                x+= j-b
            else:
                x+= max(min(j-b,a),1)

def spinning_rings3(inner_max, outer_max):
    p = inner_max + 1
    q = outer_max + 1
    move = 1
    while (-move) % p != move % q:
        if (-move) % p >= q:
            move = move // p * p + p - q + 1
        elif move % q >= p:
            move = move // q * q + q
        elif (-move) % p > move % q and ((-move) % p + move % q) % 2 == 0:
            move += ((-move) % p - move % q) // 2
        else:
            move = min((move - 1) // p * p + p, (move - 1) // q * q + q) + 1
    return move


total1 = 0
total2 = 0
total3 = 0
for i in range(100000):
    inner,outer=random.randrange(1,2**48),random.randrange(1,2**48)
    start = time.time()
    spinning_rings(inner,outer)
    total1 += time.time() -start

    start = time.time()
    spinning_rings2(inner,outer)
    total2 += time.time() -start

    start = time.time()
    spinning_rings3(inner,outer)
    total3 += time.time() -start

print(total1)
print(total2)
print(total3)

