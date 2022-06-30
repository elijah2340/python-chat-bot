mylist = [7,1,8,3,4,2]
temporary = 0
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[i] < mylist[j]:
            temporary = mylist[j]
            mylist[j] = mylist[i]
            mylist[i] = temporary


print(mylist)