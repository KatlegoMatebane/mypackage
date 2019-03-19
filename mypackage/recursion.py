# FUNCTION ONE
def sum_array(array):

    '''Return sum of all items in array'''

    total = 0
    index = 0
    while index < len(array):
        total = total + array[index]
        index = index + 1
    return total

print((sum_array([1,2,3,4,5,])))
# FUNCTION TWO
def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# FUNCTION THREE
def factorial(n):

    '''Return n!'''

    number = 1

    while n >= 1:
        number = number * n
        n = n - 1

    return number

#FUNCTION FOUR
def reverse(word):

    '''Return word in reverse'''
    return word[::-1]