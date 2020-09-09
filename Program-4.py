d = {}
lst = [1,2,3,4,5,6,7,8,9,10,11]

for i in lst:
    d[i] = 0
    for j in lst:
        if j%i==0:
            d[i] = d[i]+1

print(d)
