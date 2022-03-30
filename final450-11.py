
def rearrange(a,n):
    j=0
    for i in range(0,n):
        if (a[i]<0):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            
            j +=1
    
    print(a)       


a = [1,2,-4,-1,6,-2]
n = len(a)
    
rearrange(a,n)


#[-4, -1, -2, 2, 6, 1]
#rearrange -ve nums to left side of array
