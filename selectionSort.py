from constants import test_array


def selection_sort(A):
    for i in range(len(A) - 1):
        smallest = i
        for j in range(i + 1, len(A)):
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
        print(A)
    return A


selection_sort(test_array)
