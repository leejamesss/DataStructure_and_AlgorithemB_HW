def proc(i,stackLen):
    if i==n:
        return 1 
    else:
        result=0
        if stackLen>0:
            result+=proc(i,stackLen-1)
            result+=proc(i+1,stackLen+1)
        else:
            result=proc(i+1,stackLen+1)
    return result 

n=int(input())
print([proc(0,0)])


#中下

