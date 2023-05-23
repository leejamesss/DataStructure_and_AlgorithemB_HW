def stairs(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return stairs(n-1)+stairs(n-2)
    
# def stairs(n):
#     if n<2:
#         return 1
    
#     else:
#         a1,a2=1,1
#         for i in range(2,n+1):
#         a3=a1+

