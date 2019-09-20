def num_k_n(n,k):
    if k == n or k == 1 or n-k == 1:
        return 1
    elif k > n:
        return 0
    else:
        return num_k_n(n-k,k) + num_k_n(n-1,k-1)

def exp_sum(n):
    total = 0
    for i in range(2,n):
        total += num_k_n(n,i)
    print(total+2)

#OR

def exp_sum(n):
    if n < 0:
        return 0
    dp = [1]+[0]*n
    for num in xrange(1,n+1):
        for i in xrange(num,n+1):
            dp[i] += dp[i-num]
    return dp

print(exp_sum(5))