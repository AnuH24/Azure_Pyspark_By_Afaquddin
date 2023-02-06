def sum(lb,ub):
    total=0
    while (lb<=ub):
        total+=lb
        lb+=1
    return total
    #print(total)

print(sum(1,10))
print(sum(1,5))
