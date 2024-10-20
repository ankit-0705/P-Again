l=["a","a","b","b","c","c","c"]
temp=[]
c=0
for i in l:
    if i not in temp:
        temp.append(i)
for i in temp:
    for j in l:
        if i==j:
            c+=1
    print(i+str(c),end="")
    c=0