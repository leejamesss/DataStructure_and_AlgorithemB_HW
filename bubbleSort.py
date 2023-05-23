# def bubbleSort(a):
#     n = len(a)
#     for i in range(1, n):
#         for j in range(n-i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

def bubbleSort(a):
    n = len(a)
    for i in range(1, n):
        done = True
        for j in range(n-i):
            if a[j-1] < a[j]:
                a[j], a[j-1] = a[j-1], a[j]
                done = False

        if done:
            break
