from constants import test_array


# complexity: O(n^2)
# in-place: true
# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                print(A)
    return A


bubble_sort(test_array)
