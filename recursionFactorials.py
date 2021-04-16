

def factorial(n):
    '''Assuming that n is a positive integer or 0'''
    if n >= 1:
        return n*factorial(n-1)
    else:
        return 1
    
    
print(factorial(1))