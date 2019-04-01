def maxHeapify(A, x):
    l = 2 * x
    r = 2 * x + 1
    if l < size and A[l] > A[x]:
        largest = l
    else:
        largest = x

    if r < size and A[r] > A[largest]:
        largest = r

    if largest != x:
        A[x], A[largest] = A[largest], A[x]
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in range(len(A) // 2, -1, -1):
        maxHeapify(A, i)

def heapSort(A):
    global size

    buildMaxHeap(A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        size -= 1
        maxHeapify(A, 0)
        print(A)

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]
size = len(A)

heapSort(A)