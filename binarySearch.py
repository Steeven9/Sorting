from constants import test_array


def binary_search(A, x):
    # Assume A is sorted
    m = len(A) // 2
    if x > A[m]:
        return binary_search(A[m + 1:len(A)], x)
    elif x < A[m]:
        return binary_search(A[0:m], x)
    else:
        return True


print(binary_search(test_array, 88))
print(binary_search(test_array, 8))
