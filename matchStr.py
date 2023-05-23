# def match(s): #复杂度O(n)
#     stack = []
#     pairs = {")":"(","]":"[","}":"{" }
#     for x in s:
#         if x in "([{":
#             stack.append(x)
#         elif x in ")]}":
#             if len(stack) == 0 or stack[-1] != pairs[x]:
#                 return False
#             stack.pop()
#     return len(stack) == 0
# print(match(input()))





# def matches(s):
#     stack=[]
#     pairs={")":"(","]":"[","}":"{"}
#     for x in s:
#         if x in "({[":
#             stack.append(x)
#         elif x in ")]}":
#             if len(stack)==0 or stack[-1]!=pairs[x]:
#                 return False
#             stack.pop()
#     return len(stack)==0
# print(matches(input()))


def matches(s):
    stack=[]
    pairs={")":"(","]":"[","}":"{"}
    for i in s:
        if i in "({[":
            stack.append(i)
        else:
            if len(stack)==0 or stack[-1]!=pairs[i]:
                return False
            stack.pop()
    return len(stack)==0
print(matches(input()))
