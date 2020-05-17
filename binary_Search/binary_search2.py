def binary_search(ordered_list, n):
  lower_index = 0
  higher_index = len(ordered_list) - 1

  while lower_index <= higher_index:
    middle_index = (lower_index + higher_index) // 2
    guess = ordered_list[middle_index]

    if guess == n:
      return f'N = {n} was found at index {middle_index}'
    elif guess > n:
      higher_index = middle_index - 1
    elif guess < n:
      lower_index = middle_index + 1 
  
  return f'N = {n} is not on the list'


ordered_list = [1, 3, 5, 7, 9]

print(binary_search(ordered_list, 3))
print(binary_search(ordered_list, 0))
print(binary_search(ordered_list, 9))
print(binary_search(ordered_list, -1))
print(binary_search(ordered_list, 7))
print(binary_search(ordered_list, 4.5))