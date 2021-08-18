def greaterThanRightSideArray(array):
    result = []
    arrayLength = len(array)
    maxNumber = array[arrayLength-1]

    for i in range(arrayLength):
        if array[arrayLength-i-1] >= maxNumber:
            maxNumber = array[arrayLength-i-1]
            result.append(maxNumber)

    result = reverseArray(result)

    print(result)
    return result


def reverseArray(array):
    reversedArray = []
    for i in range(len(array)):
        reversedArray.append(array[len(array) - i - 1])
    return reversedArray


greaterThanRightSideArray([16,17,4,3,5,2])
