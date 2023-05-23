n=int(input())
def ischa(cha):
    if '\u4e00' <= cha <= '\u9fff':
        return True
    else:
        return False

def isnum(num):
    if '\u0030' <= num <= '\u0039':
        return True
    else:
        return False


for i in range(n):
    flag=1
    str=input()
    if len(str)!=13:
        flag=0

    for k in str[0:2]:
        if not ischa(k):
            flag=0
            break
    if not str[2] =="_":
        flag=0
    for j in str[3:11]:
        if not isnum(j):
            flag=0
            break
    if flag==1:
        print("YES")
    else:   
        print("NO") 
            
        
        
        
        



