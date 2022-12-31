def c(n, k):
    if (k == 0 or n == k): 
        return 1
    else:
        return c(n-1, k-1) + c(n-1, k)

print(c(4, 2))