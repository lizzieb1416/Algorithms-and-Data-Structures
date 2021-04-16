

def fib(n):
    '''Assuming that n is a positive integer'''
    if n == 0 or n == 1:
        return n
    elif n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1
    
    
print(fib(9))