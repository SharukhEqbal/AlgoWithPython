# 0, 1, 1, 2, 3, 5, 8, 13, 21
# n=5 f(5) = f(4) + f(3) --> f(4) = f(3) + f(2), f(3) = f(2) + f(1), call recursively

def nthFibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return nthFibonacci(n - 1) + nthFibonacci(n - 2)
        
print(nthFibonacci(3))
