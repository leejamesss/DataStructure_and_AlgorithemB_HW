result=[]
stack=[]
def permutation(instack,ori):
    global result
    global stack
    if len(ori)==0:                                       #出栈总数
        back=result[:]                                  #出栈的情况打印
        record=stack[:]                                 
        while stack:                                        
            result.append(stack.pop())                  #计算机专业的内容
        print("".join(result))                          #出栈的情况打印
        result=back[:]                                  #出栈的情况打印
        stack=record[:]
    elif instack==0:                                    #判断是不是合法序列
        stack.append(ori.pop())                         #
        permutation(1,ori)
        ori.append(stack.pop())
    else:
        stack.append(ori.pop())
        permutation(instack+1,ori)
        ori.append(stack.pop())
        result.append(stack.pop())
        permutation(instack-1,ori)
        stack.append(result.pop())
def main():
    ori=input("请输入待入栈元素：")
    permutation(0,list(ori))
main()


