def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


arr = [1, 4, 6, 3]

print(count(arr))
