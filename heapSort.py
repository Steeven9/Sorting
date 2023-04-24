from constants import test_array


# complexity: O(n log(n))
# in-place: true
# https://en.wikipedia.org/wiki/Heapsort
def max_heapify(A, x):
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
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    global size

    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        size -= 1
        max_heapify(A, 0)
        print(A)


size = len(test_array)
heap_sort(test_array)
