def selectionSort(a):
    n = len(a)
    for i in range(n-1):
        minPos = i
        for j in range(i+1, n):
            if a[j] < a[minPos]:
                minPos = j
        if minPos != i:
            a[i], a[minPos] = a[minPos], a[i]
