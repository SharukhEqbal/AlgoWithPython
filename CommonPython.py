a = ['s','b','s']
a.sort()
print(a)

b = 'sbs'
print(sorted(b))
print(b) # remains unchanged

l = [('hello', 5), ('ok', 2), ('bye', 3)]
print(sorted(l, key=lambda x:x[1]))
