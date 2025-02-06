def unique(x):
    listik = []
    for i in x:
        check = True
        for j in listik:
            if i == j:
                check = False
        if(check):
            listik.append(i)
    return listik

l = [1, 1,1,1,1,2,2,2,2,3,4,5,6,7,87,1,1,1,32,3]
print(unique(l))