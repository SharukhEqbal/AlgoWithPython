# "without,hello,bag,world"
# sentence.split(',') will return a list then use result.sort() 

def sortCommaSeparatedWord(sentence):
    list1 = sentence.split(',')
    list1.sort() # It will sort the list and returns None
    return list1

print(sortCommaSeparatedWord("without,hello,bag,world"))

# Sort a list based on second value
# [("without", 7), ("hello", 5), ("bag", 3), ("world", 5)]

def sortWordBasedOnSecondValueInTuple(list1):
    return sorted(list1, key= lambda x: x[1])

print(sortWordBasedOnSecondValueInTuple([("without", 7), ("hello", 5), ("bag", 3), ("world", 5)]))
