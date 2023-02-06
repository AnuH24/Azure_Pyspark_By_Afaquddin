a= """Blackbird singing in the dead of night
Take these broken wings and learn to fly
All your life
You were only waiting for this moment to arise"""
words=a.split()
print(words)
print("total words=",len(words))
print("occurance of a=",words.count("a"))
print("occurance of an=",words.count("an"))
print("occurance of the=",words.count("the"))
counts={}
for word in words:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1
print(counts)

#we can also get the values using below statements
print("occurance of a=",counts.get("a"))
print("occurance of an=",counts.get("an"))
print("occurance of the=",counts.get("the"))

