# l=list
l=[1,2,1,6,3,4,5,1,2,8]
print("l=",type(l))
print("l=",l)

#indexing
print("\nfirst element in list =",l[0])
print("second element in list =",l[1])

#reverse indexing
print("\nlast element in list =",l[-1])
print("last 4th element in list =",l[-4])

#slicing
print("\n",l[2:5])
print(l[:4])
print(l[2:])

#index of element WRT index position
print("\n",l.index(2,0))
print(l.index(2,6))
print(l.index(1,3))

print("\nthe popped element is =",l.pop(2))

#this method is used to see how many times the element is repeated
print("\nthe number 1 is repeated ",l.count(1),"times.")
print("the number 2 is repeated",l.count(2),"times.")
print("the number 5 is repeated",l.count(5),"times.")

#list converting to set will eliminate the duplicate values
#s=set
s=set(l)
print("\ns= ",type(s))
print("s=",s)