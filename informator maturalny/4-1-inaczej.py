def sortw(A):
    dominujaca = 0
    n = len(A)
    for i in range(1, n):
        v = A[i]
        j = i
        while j > 0 and v < A[j - 1]:
            A[j] = A[j - 1]
            j -= 1
            dominujaca += 1
        A[j] = v
    return A, dominujaca


arr = [5, 3, 8, 1, 2]
print(arr, end=" ")
sorted_arr = sortw(arr)
print(sorted_arr)

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr, end=" ")
sorted_arr = sortw(arr)
print(sorted_arr)

for i in range(1,15):
    arr = [x for x in range(i, 0, -1)]
    print(arr, end=" ")
    sorted_arr = sortw(arr)
    print(sorted_arr)
