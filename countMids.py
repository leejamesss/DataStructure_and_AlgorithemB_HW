def countMid(s):
    s=s.split()
    stkNum=[] 
    stkOp=[]
    priority={'/':1,'*':1,'+':2,'-':2}

    for x in s:
        if x=="(":
            stkOp.append(x)
        elif x==")":
            while stkOp[-1]!="(":
                op=stkOp.pop()
                a,b=stkNum.pop(),stkNum.pop()
                stkNum.append(eval(str(b)+op+str(a)))
            stkOp.pop()
        elif x in "/*+-":
            while len(stkOp)>=1 and stkOp[-1]!='(' and priority[stkOp[-1]] <=priority[x]:
                op=stkOp.pop()
                a,b=stkNum.pop(),stkNum.pop()
                stkNum.append(eval(str(a)+op+str(b)))
            stkOp.append(x)
        else:
            stkNum.append(float(x))
            

        

