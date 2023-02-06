l=[1,2,["a","b",["anu","abhi"]]]
print(type(l))

#indexing
print(l[0])
print(l[2])
print(l[2][1])
print(l[2][2])
print(l[2][2][0])

#reverse indexing
print(l[-1])
print(l[-2])
print(l[-1][-1])
print(l[-1][-1][0])
print(l[-1][-1][-1])

#changing nested list items
l[1]=3
print(l)

#add items to nested list
l.append("hari")
print(l)
l[2][2].append("raj")
print(l)
l[2].insert(0,"satya")
print(l)

#merge one list into another
l.extend(["suni"])
print(l)

#remove items from nested list
x=l[2].pop(0)
print(l)
#removed item
print(x)

#del will remove the value from the list
print(l)
del l[2][2][1]
print(l)

#remove by value
l[2][2].remove("anu")
print(l)

#length of the list
print(len(l))
print(len(l[2]))

#iterate through the list
for i in l:
    print(i)