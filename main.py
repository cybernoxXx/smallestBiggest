def getSmallest(numbers):

    if len(numbers) == 0:
        return None
    else:
        smallest = numbers[0]

        for element in numbers:
            if element < smallest:
                smallest = element

    return smallest

def getBiggest(numbers):
    if len(numbers) == 0:
        return None
    else:
        biggest = numbers[0]

        for element in numbers:
            if element > biggest:
                biggest = element

    return biggest



assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None