s={1,2,3,4,5,6}
print("s=",s)

# #indexing
#print("\nfirst element in set s =",s[0])
# print("second element in set s =",s[1])
#
# #reverse indexing
# print("\nlast element in set s =",s[-1])
# print("last 4th element in set s =",s[-4])

# #slicing
# print("\n",s[2:5])
# print(s[:4])
# print(s[2:])
#
# #index of element WRT index position
# print("\n",s.index(2,0))
# print(s.index(2,6))
# print(s.index(1,3))

#print("\nthe popped element is =",s.pop(2))


s2={5,6,7,8,9}
print("s2=",s2)

#intersection of sets
print(s.intersection(s2))
print(s.union(s2))

# the numbers which are not present in s WRT s2
print(s2.difference(s))