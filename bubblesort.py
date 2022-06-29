mylist = [7,1,8,3,4,2]
temporary = 0
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[i] > mylist[j+1]:
            temporary = mylist[i]
            mylist[i] = mylist[j+1]
            mylist[j+1] = temporary


print(mylist)