def minimumMaximumArray(array):
    arrayLength = len(array)

    if arrayLength % 2 == 0:
        if array[0] > array[1]:
            maximum = array[0]
            minimum = array[1]
        else:
            maximum = array[1]
            minimum = array[0]
        i = 2

    else:
        maximum = array[0]
        minimum = array[0]
        i = 1

    while i < arrayLength - 1:
        if array[i] < array[i + 1]:
            if maximum < array[i + 1]:
                maximum = array[i + 1]
            if minimum > array[i]:
                minimum = array[i]
        else:
            if maximum < array[i]:
                maximum = array[i]
            if minimum > array[i + 1]:
                minimum = array[i + 1]
        i += 2

    return maximum, minimum

print(minimumMaximumArray([0,3,4,2,-6,2,20,-2,12]))