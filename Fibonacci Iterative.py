def f(n):
    previous = 0
    current = 1
    for i in range(2, n):
        next = current + previous
        previous = current
        current = next
    return next

print(f(9))