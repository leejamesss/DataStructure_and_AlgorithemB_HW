def fib(n):
    class Status:
        def __init__(self,b,t,r):
            self.n,self.t,self.r=n,t,r
    stack=[Status(n,None,'c')]
    retVal=retAdr=None
    while stack!=[]:
        status=stack[-1]
        n=status.n
        if n==2 or n==1:
            retVal=1
            retAdr=status.r
            stack.pop()
        else:
            if retAdr==None:
                stack.append(Status(n-1,None,'a'))
            elif retAdr=='a':
                stack[-1].t=retVal
            elif retAdr=='b':
                retVal = status.t + retVal
                retAdr = status.r
                stack.pop()
            else:
                stack.pop()
    return retVal




    
#判断是不是合法序列
#出栈总数
#出栈的情况打印
#计算机专业的内容
