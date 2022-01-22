def sumOfDigit(number):
    assert number >= 0 and int(number) == number, "Constraint fail: Not a positive number"
    
    if number == 0:
        return 0
    else:
        return sumOfDigit(int(number / 10)) + int(number % 10)

print(sumOfDigit(144))
print(sumOfDigit(4))
print(sumOfDigit(-11))
