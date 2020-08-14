def fizz_buzz(numbers):
    '''
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    # for i in range(len(numbers)):
    #     num = numbers[i]
    #     if num % 3 == 0:
    #         numbers[i] = "fizz"
    #     if num % 5 == 0:
    #         numbers[i] = "buzz"
    #     if num % 5 == 0 and num % 3 == 0:
    #         numbers[i] = "fizzbuzz"
    
    '''
    Enumerate is a built-in function that allows us to loop over
    something and have an automatic counter. Enumerate also accepts
    an optional argument that allows us to specify the starting 
    index of the counter.
    '''
    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"