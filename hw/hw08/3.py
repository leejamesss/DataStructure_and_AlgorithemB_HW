from math import sqrt
def radar():
    ans=0
    while True:
        try:
            n,d=map(int,input().split())
        except:
            break
        lst=[]
        ans+=1
        flag=0   #判断是否有解
        if n ==0 and d ==0:
            break
        for i in range(n):
            x,y=map(float,input().split())
            if y>d:
                flag=1
                continue
            start=x-sqrt(d*d-y*y)
            end=x+sqrt(d*d-y*y)
            lst.append((start,end))
        lst.sort(key=lambda x:x[0])
        count=1
        noCoveredMinX2=lst[0][1]
        if flag!=1:
            for i in range(n):
                if lst[i][0]<=noCoveredMinX2:
                    noCoveredMinX2=min(noCoveredMinX2,lst[i][1])
                elif lst[i][0]>noCoveredMinX2:
                    count+=1
                    noCoveredMinX2=lst[i][1]
            print(f"Case {ans}: {count}")        
        else:
            print(f"Case {ans}: -1") 
radar()
