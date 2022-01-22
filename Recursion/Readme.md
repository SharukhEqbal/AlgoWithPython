To Solve a recursive problem think with three steps:

1. Find the recursive flow
2. Find the base condition to exit the recursion
3. Find the unintentional case - the constraint (mostly will in the question itself)

e.g.

Sum of digits:
  recursive flow: seperate the number 10  --> 10/10 = 1 remainder 0     114 --> 114/10 = 11 remainder 4, 11/10 = 1 remainder 1 4+1+1 = 5 
                  f(n) = f(n/10) + n % 10
  Base condition:
                  when int(x/10) == 0 we can return it e.g. 1/10 == 0
  Constraint case:
                  number needs to be positive


Similarly for power
  recursive flow:  2^3= 2*2*2 = 2*2^(3-1)     f(x^n) = x * x^(n-1) = x * f(x^(n-1))
  base condition: 2^0 = 1 or 1^1 = 1 so either x == 1 or n == 0 
  constraint case: exp needs to be positive
  
