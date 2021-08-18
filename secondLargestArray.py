def secondLargestArray(array):
    arrayLength = len(array)
    defaultNumber = -1000000000000000000

    if arrayLength < 2:
        return "Error"

    largest = defaultNumber
    secondLargest = defaultNumber

    for i in range(0, arrayLength):
        if array[i] > largest:
            secondLargest = largest
            largest = array[i]

        elif array[i] > secondLargest and array[i] != largest:
            secondLargest = array[i]

    if(secondLargest == defaultNumber):
        return "Error"
    return secondLargest


secondLargestArray([10, 5, 10])
