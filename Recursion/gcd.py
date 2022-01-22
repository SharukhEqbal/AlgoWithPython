# a/b q r if r == 0 return b else: return gcd(b/r)
# 48, 18    48/18  r = 12   18/12 remainder = 6   12/6 remainder = 0 so 6 is the gcd of both the no.

def gcd(a,b):
    assert int(a) == a and int(b) == b, "Constraints failed:  Number must be an integer"
    if a == 0:
        return b
    if b == 0:
        return a
    a = abs(a)
    b = abs(b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
print(gcd(2, 4))
