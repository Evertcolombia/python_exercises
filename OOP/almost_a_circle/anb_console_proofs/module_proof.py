#!/usr/bin/python3

# Fibonacci numbers module

def fib(n): # Write a Fibonacci series up to n
    a, b = 0, 1

    while b <= n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # Return a Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b <= n:
        result.append(b)
        a, b = b, a+b
    return result

# ---------------- Try the next ibn the console -----------------

    """
        >>> import module_proof # importa el archivo con su nombre
        >>> fibo = module_proof # asigna el modulo a una variable

        >>> fibo.fib(1000) # executes the method fib in the  fibo module
        1123581321345589144233377610987

        >>> fibo.fib2(100) # executes the method fib in the  fibo module

        >>> fibo.__name__ #show the name of the module
        'module_proof'

        >>> fib = fibo.fib #assgin a specific method from the module
        >>> fib(500)
        1 1 2 3 5 8 13 21 34 55 89 144 233 377 
    """
