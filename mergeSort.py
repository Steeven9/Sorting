from constants import test_array


# complexity: O(n log(n))
# in-place: false
# https://en.wikipedia.org/wiki/Merge_sort
def merge_sort(A):
    if len(A) > 1:
        print("called with ", A)
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1
            print(A)

        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1
            print(A)

        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1
            print(A)
    return A


merge_sort(test_array)
