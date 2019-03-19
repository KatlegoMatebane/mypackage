#FUNCTION FIVE
def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    n = len(items)

    for i in range(n):

        for x in range(0, n - i - 1):

            if items[x] > items[x + 1]:
                items[x], items[x + 1] = items[x + 1], items[x]
    return items

#FUNCTION SIX
def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items) > 1:
        mid = len(items) // 2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        x = 0
        y = 0
        z = 0
        while x < len(lefthalf) and y < len(righthalf):
            if lefthalf[x] < righthalf[y]:
                items[z] = lefthalf[x]
                x = x + 1
            else:
                items[z] = righthalf[y]
                y = y + 1
            z = z + 1

        while x < len(lefthalf):
            items[z] = lefthalf[x]
            x = x + 1
            z = z + 1

        while y < len(righthalf):
            items[z] = righthalf[y]
            y = y + 1
            z = z + 1

    return items

#FUNCTION SEVEN
def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) <= 1:
        return items
    else:
        return quick_sort([i for i in items[1:] if i <= items[0]]) + [items[0]] + quick_sort([i for i in items[1:] if i > items[0]])
