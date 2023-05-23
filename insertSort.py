# def insertSort(a):
#     for i in range(1, len(a)):
#         e, j = a[i], i
#         while j > 0 and a[j-1] > e:
#             a[j] = a[j-1]
#             j -= 1
#         a[j] = e


def insertionSort(a, key=lambda x, y: x < y):
    for i in range(1, len(a)):
        e, j = a[i], i
        while j > 0 and key(e, a[j-1]):
            a[j] = a[j-1]
            j -= 1
        a[j] = e


a = [5, 47, 74, 3, 4, 12, 8]
insertionSort(a, key=lambda x, y: x > y)
print(a)
