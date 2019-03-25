def partition(A, begin, end):
    x = A[end]
    i = begin - 1
    for j in range(begin, end):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            print(A)
    A[i + 1], A[end] = A[end], A[i + 1]
    print(A)
    return i + 1

def quickSort(A, begin, end):
    if begin < end:
        q = partition(A, begin, end)
        quickSort(A, begin, q - 1)
        quickSort(A, q + 1, end)
    return A

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

quickSort(A, 0, len(A) - 1)