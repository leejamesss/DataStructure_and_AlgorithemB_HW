total=0
result=[]
stack=[]
s=""
def proc(i):
    global total 
    global stack
    global result 
    global s 
    if i==len(s):
        while len(stack)>0:
            result.append(stack.pop())
        total+=1
        r="".join(result)
        print(r)
    else:
        if len(stack)>0:
            tmpStack=stack[:]
            tmpResult=result[:]
            result.append(stack.pop()) #处理元素出栈的做法
            proc(i)
            stack = tmpStack[:] #恢复stack
            result = tmpResult[:]
            stack.append(s[i]) #处理新元素入栈的做法
            proc(i+1)
        else:
            stack.append(s[i])
            proc(i+1)
s = input()
proc(0) #0个元素入过栈
print(total)


###################################

#中上 85分

#考试10-12道
#非线性给分：后续