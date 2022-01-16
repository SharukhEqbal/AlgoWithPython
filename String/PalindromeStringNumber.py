# palindrome 
# abcba use pointer to travel from both end and compare

# O(N)
def palindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

if palindrome("abcbba"):
    print("palindrome")
else:
    print("Not palindrome")
    
    
# 78987
# 78987 // 10 = 7898 (round down to floor value) 78987 / 10 = 7898.7 78987 % 10 = 7 (remainder)
# create a new reversed number by using above operator get the last digit using % add it in new value by newvalue*10 + digit
# then use floor value to remove last digit do this in loop
def palindromeNumber(number):
    n = number
    reversed_number = 0
    
    while number > 0:
        lastdigit = number % 10
        reversed_number = reversed_number * 10 + lastdigit
        number = number // 10
        
    if reversed_number == n:
        print("Number is a palindromeNumber")
    else:
        print("Number is not a palindromeNumber")

palindromeNumber(78987)
    
            
