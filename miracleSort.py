from constants import test_array


# complexity: unbounded
# in-place: true
# https://en.wikipedia.org/wiki/Bogosort#Miracle_sort
def miracle_sort(A):
    is_sorted = True

    for i in range(len(A) - 1):
        if (A[i] < A[i + 1]):
            is_sorted = False

    if is_sorted:
        return A
    else:
        miracle_sort(A)


miracle_sort(test_array)
