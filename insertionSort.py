from constants import test_array


# complexity: O(n^2)
# in-place: true
# https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(A):
    i = 1
    while i < len(A):
        k = i
        while k > 0 and A[k] < A[k - 1]:
            A[k], A[k - 1] = A[k - 1], A[k]
            print(A)
            k -= 1
        i += 1
    return A


insertion_sort(test_array)
