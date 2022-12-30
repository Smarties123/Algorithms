def factorial(n) :

    if(n == 0): 
        return 1
    else:
        return factorial(n-1)*n


a = 5
print(factorial(a))