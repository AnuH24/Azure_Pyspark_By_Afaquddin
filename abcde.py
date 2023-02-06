#
# ab=input("enter name:")
# ab=ab.split()
# i=0
# cnt=0
# while i<len(ab):
#     cnt=0
#     for j in ab:
#         if ab[i]==j:
#             cnt=cnt+1
#     print(ab[i],"present",cnt,"times")
#     i=i+1
















my="Blackbird to singing in the dead of night Take these broken wings and learn to fly All your life You were only waiting for this moment to arise"
#print(len(my.split()))
b=my.split()
print("b=",b)
print(len(b))
# print(b.count("a"))
# print(b.count("an"))
# print(b.count("the"))
word_occurance={}
for d in b:
    if d in word_occurance:
        word_occurance[d]+=1
    else:
        word_occurance[d]=1
print(word_occurance)
print(word_occurance.get("a"))
print(word_occurance.get("an"))
print(word_occurance.get("the"))


