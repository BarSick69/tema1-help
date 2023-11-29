test = [[1,2,3,4,9],
        [5,6,7,8,0]]
width=len(test[0])
height=len(test)
for i in range(0,height):
    for j in range(0,width//2):
        if j==width-j-1:
            break
        else:
            temp=test[i][j]
            test[i][j]=test[i][width-j-1]
            test[i][width-j-1]=temp
print(test) 
