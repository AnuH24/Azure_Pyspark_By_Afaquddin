def sum(func,lb,ub):
    total=0
    while (lb<=ub):
        total+=func(lb)
        lb+=1
    return total

def id(i):
    return  i

def square(i):
    return i*i

def cube(i):
    return i*i*i

print(sum(id,1,2))
print(sum(id,2,3))

print("\n",sum(square,1,2))
print(sum(square,2,3))

print("\n",sum(cube,1,2))
print(sum(cube,2,3))

print("\n",sum(lambda i:i*2,2,3))
print(sum(lambda i:i*3,1,2))
print(sum(lambda i:i*i,1,2))
