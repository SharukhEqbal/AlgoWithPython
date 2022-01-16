# (()()) Balanced Parenthesis
# {')':'(', '}':'{', ']','['}
# keys in dict is opening one iterate through the list if the value is closing bracket
# check for previous value whether it is opening brace of same parenthesis

def balancedParenthesis(string):
    openingBrackets = '{[('
    closingBrackets = '}])'
    dict1 = {')':'(', '}':'{', ']':'['}
    stack = []
    for i in string:
        if i in openingBrackets:
            stack.append(i)
        elif i in closingBrackets:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == dict1[i]:
                    stack.pop()
                else:
                    return False
    return len(stack) == 0
        
print(balancedParenthesis("((){(}))"))
