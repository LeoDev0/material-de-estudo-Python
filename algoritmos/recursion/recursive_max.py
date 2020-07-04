def max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        tmp_max = max(arr[1:])
        return arr[0] if arr[0] > tmp_max else tmp_max


arr = [3, 5, 1, 8, 9, 2, 0]

print(max(arr))
