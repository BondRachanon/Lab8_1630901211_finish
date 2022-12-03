def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def Sort1(arr, low, high):
    i = (low - 1)
    for j in range(low, high):
        if (arr[j] <= arr[high]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def Sort2(arr, low, high):
    i = low - 1
    j = high + 1
    while (True):
        i += 1
        while (arr[i] < arr[low]):
            i += 1
        j -= 1
        while (arr[j] > arr[low]):
            j -= 1
        if (i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]

def Qsort(arr, low, high):
    if (low < high):
        pi = Sort1(arr, low, high)
        Qsort(arr, low, pi - 1)
        Qsort(arr, pi + 1, high)

arr = [29, 10, 14, 37, 14 ,20 ,7 ,16 ,12]
n = len(arr)
print("Defalut Arr :")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergeSort(arr, 0, n - 1)
print("\n\nMergesort Arr is :")
for i in range(n):
    print("%d" % arr[i], end=" ")

Qsort(arr, 0, len(arr) - 1)
print("\n\n Lomuto Qsort Arr is :")
for i in range(n):
    print("%d" % arr[i], end=" ")

Qsort(arr, 0, n - 1)
print("\n\nHoare Qsort Arr is : ")
for i in range(n):
    print("%d" % arr[i], end=" ")