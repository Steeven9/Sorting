def binarySearch(A, x):
    # Assume A is sorted
    if len(A) == 0:
        return False
    m = len(A)//2
    if x > A[m]:
        return binarySearch(A[m+1:len(A)], x)
    elif x < A[m]:
        return binarySearch(A[0:m], x)
    else:
        return True

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

print(binarySearch(A, 88))
print(binarySearch(A, 8))