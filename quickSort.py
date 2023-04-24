from constants import test_array


# complexity: O(n log(n)) average, O(n^2) worst
# in-place: true
# https://en.wikipedia.org/wiki/Quicksort
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


def quick_sort(A, begin, end):
    if begin < end:
        q = partition(A, begin, end)
        quick_sort(A, begin, q - 1)
        quick_sort(A, q + 1, end)
    return A


quick_sort(test_array, 0, len(test_array) - 1)
