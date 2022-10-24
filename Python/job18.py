L=[8,5,14,18,12,9,4,1,3]

for i in range(len(L)):
    for j in range(len(L)):
        if L[i]<=L[j]:
            L[i],L[j],=L[j],L[i]
print(L)