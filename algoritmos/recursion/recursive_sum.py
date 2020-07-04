def soma(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + soma(arr[1:])
         

arr = [2, 4, 6]

print(soma(arr))
