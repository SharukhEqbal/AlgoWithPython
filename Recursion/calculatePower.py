def calculatePower(base, exp):
    assert exp >= 0 and int(exp) == exp, "Constraints failed: Exp can only be a positive number"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * calculatePower(base, exp-1)
    
    
print(calculatePower(10, 2))
print(calculatePower(1,1))
print(calculatePower(3,-1))
