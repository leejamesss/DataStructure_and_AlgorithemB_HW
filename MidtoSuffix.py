# def midToSuffix(s):
#     s = s.split()
#     stack,result = [],[]
#     priority = {"/": 1, "*": 1, "+": 2, "-": 2}
#     for x in s:
#         if x == "(":
#             stack.append(x)
#         elif x == ")":
#             while stack[-1] != "(":
#                 result.append(stack.pop())
#             stack.pop()
#         elif x in "/*+-":
#             while len(stack) >= 1 and stack[-1] != '(' and priority[stack[-1]] <= priority[x]:
#                 result.append(stack.pop())
#             stack.append(x)
#         else:
#             result.append(x)
#     while stack != []:
#         result.append(stack.pop())
#     return " ".join(result)



# def midtoSuffix(s):
#     s=s.split()
#     stack,result=[],[]
#     priority={"*":1,"/":1,"+":2,"-":2}
#     for x in s:
#         if x=="(":
#             stack.append(x)
#         elif x==")":
#             while stack[-1]!="(":
#                 result.append(stack.pop())
#             stack.pop()
#         elif x in "/*+-":
#             while len(stack)>=1 and stack[-1]!="(" and priority[stack[-1]]<=priority[x]:
#                 result.append(stack.pop())
#             stack.append(x)
#         else:
#             result.append(x)
#     while stack!=[]:
#         result.append(stack.pop())
#     return " ".join(result)



# def midtoSuffix(s):
#     s=s.split()
#     stack,result=[],[]
#     priority={"/":1,"*":1,"+":2,"-":2}
#     for x in s:
#         if x == "(":
#             stack.append(x)
#         elif x == ")":
#             while stack[-1]!="(":
#                 result.append(stack.pop())
#             stack.pop()
#         elif x in "+-*/":
#             while len(stack)>=1 and stack[-1]!='(' and priority[stack[-1]] <=priority[x]:
#                 result.append(stack.pop())
#             stack.append(x)
#         else:
#             result.append(x)
#     while stack !=[]:
#         result.append(stack.pop())
#     return " ".join(result)
# print(midtoSuffix(input()))

# def midtoSuffix(s):
#     s=s.split()
#     stack,result=[],[]
#     priority={"/":1,"*":1,"+":2,"-":2}
#     for x in s:
#         if x =="(":
#             stack.append(x)
#         elif x==")":
#             while stack[-1]!="(":
#                 result.append(stack.pop())
#             stack.pop()
#         elif x in "+-*/":
#             while len(stack)>=1 and stack[-1]!="(" and priority[stack[-1]]<=priority[x]:
#                 result.append(stack.pop())
#             stack.append(x)
#         else:
#             result.append(x)
#     while stack!=[]:
#         result.append(stack.pop())
#     return " ".join(result)
# print(midtoSuffix(input()))


# def midtoSuffix(s):
#     s=s.split()
#     stack,result=[],[]
#     priority={"/":1,"*":1,"+":2,"-":2}
#     for x in s:
#         if x=="(":
#             stack.append(x)
#         elif x==")":
#             while stack[-1]!="(":
#                 result.append(stack.pop())
#             stack.pop()
#         elif x in "+-*/":
#             if len(stack)>=1 and stack[-1]!="(" and priority[stack[-1]]<=priority[x]:
#                 result.append(stack.pop())
#             stack.append(x)
#         else:
#             result.append(x)
#     while stack!=[]:
#         result.append(stack.pop())
#     return " ".join(result)
# print(midtoSuffix(input()))

# def midtoSuffix(s):
#     s=s.split()
#     stack,result=[],[]
#     priority={"/":1,"*":1,"+":2,"-":2}
#     for x in s:
#         if x=="(":
#             stack.append(x)
#         elif x==")":
#             while stack[-1]!="(":
#                 result.append(stack.pop())
#                 stack.pop()
#         elif x in "+-*/":
#             if len(stack)>=1 and stack[-1]!="(" and priority[stack[-1]]<=priority[x]:
#                 result.append(stack.pop())
#             stack.append(x)
#         else:
#             result.append(x)
#         while stack!=[]:
#             result.append(stack.pop())
#         return " ".join(result)
# print(midtoSuffix(input()))

def midtoSuffix(s):
    s=s.split()                                                                         
    stack,result=[],[]
    priority={"/":1,"*":1,"+":2,"-":2}
    for x in s:
        if x=="(":
            stack.append(x)                                                                     #如果是左括号，直接入栈
        elif x==")":                                                                            #如果是右括号，将栈中元素弹出，直到遇到左括号
            while stack[-1]!="(":                                                               #将弹出的元素依次加入到后缀表达式的末尾
                result.append(stack.pop())                                                      
            stack.pop()                                                                         #将左括号弹出，但不加入到后缀表达式中
        elif x in "+-*/":
            if len(stack)>=1 and stack[-1]!='(' and priority[stack[-1]]<=priority[x]:           #如果栈顶元素为运算符，且其优先级大于或等于将要入栈的运算符，将栈顶元素弹出
                result.append(stack.pop())                                                      #并将其加入到后缀表达式的末尾，再次转到与新的栈顶元素相比较的步骤
            stack.append(x)                                                                     #将运算符压入栈中
        else:
            result.append(x)                                                                    #如果是操作数，将其加入到后缀表达式的末尾
    while stack!=[]:                                                                            #将栈中元素依次弹出，加入到后缀表达式的末尾
        result.append(stack.pop())                                                              #直到栈为空
    return " ".join(result)                                                                     #最后返回后缀表达式
print(midtoSuffix(input()))                                                                     #输入中缀表达式，输出后缀表达式


    


# #90+分


