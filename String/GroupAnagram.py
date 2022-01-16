# ['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']
# sort and count 'oy'= ['oy', 'yo'] 'act'= ['act', 'cat']

# O(n) time
def groupAnagram(array):
    dict1 = {}
    for i in array:
        sortedWord = ''.join(sorted(i))
        if sortedWord in dict1:
            dict1[sortedWord].append(i)
        else:
            dict1[sortedWord] = [i]
    return dict1
    
print(groupAnagram(['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']))
