reseven=0
resodd=0
for i in range(1,100):
#sum of even numbers from 1 to 100
    if (i%2==0):
        reseven+=i
    else:
#sum of odd numbers from 1 to 100
        resodd+=i
print(f"sum of even numbers = ",reseven)
print(f"sum of odd numbers = ",resodd)