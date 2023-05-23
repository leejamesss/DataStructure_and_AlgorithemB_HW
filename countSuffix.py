# def countSuffix(s): #计算后序表达式s的值，复杂度O(n)
#     s = s.split()
#     stack = []
#     for x in s:
#         if x in "+-*/":
#             a,b = stack.pop(),stack.pop()
#             stack.append(eval(str(b) + x + str(a)))
#         else:
#             stack.append(float(x))
#     return stack[0]


def countSuffix(s):
    s=s.split()
    stack=[]
    for x in s:
        if x in "+-*/":
            a,b=stack.pop(),stack.pop()
            stack.append(eval(str(a)+x+str(b)))
        else:
            stack.append(float(x))
    return stack[0]
