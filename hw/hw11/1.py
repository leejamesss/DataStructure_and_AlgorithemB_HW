def main():
    n,m=map(int,input().split())
    pre=[[]for i in range(n)]
    post=[[]for i in range(n)]
    earlytime=[-1 for i in range(n)]
    for i in range(m):
        a,b,c=map(int,input().split())
        pre[b-1].append((a-1,c))#科考站b必须等a建完c时长才能建
        post[a-1].append((b-1,c))#科考站a建好c时长后方可建b
    dests=[]
    for i in range(n):
        if post[i]==[]:
            dests.append(i)
    def findmaxtime(station):
        nonlocal pre,post,earlytime
        maxtime=0
        if earlytime[station]==-1:
            for i in pre[station]:
                maxtime=max(maxtime,findmaxtime(i[0])+i[1])
            earlytime[station]=maxtime
        return earlytime[station]
    maxt=0
    for station in dests:
        earlytime[station]=findmaxtime(station)
        maxt=max(maxt,earlytime[station])

    print(maxt)
    latetime=[maxt for i in range(n)]
    def getlatetime(station):
        nonlocal latetime,pre,post
        for i in pre[station]:
            for j in post[i[0]]:
                latetime[i[0]]=min(latetime[i[0]],latetime[j[0]]-j[1])
            getlatetime(i[0])
    for station in dests:
        getlatetime(station)

    for i in range(n):
        if post[i]:
            for tuples in post[i]:
                if earlytime[i]+tuples[1]==latetime[tuples[0]]:
                    print(i+1,tuples[0]+1)
main()

#由Wellington提出的解法
