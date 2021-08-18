def rotateArrayAnticlockwise(array, rotations):
    arrayLength = len(array)

    if abs(rotations) >= arrayLength:
        rotations = rotations % 10

    array[0:rotations] = reverseArray(array[0:rotations])
    array[rotations:arrayLength] = reverseArray(array[rotations:arrayLength])

    array = reverseArray(array)

    print(array)

    return array


def reverseArray(array):
    reversedArray = []
    for i in range(len(array)):
        reversedArray.append(array[len(array) - i - 1])
    return reversedArray


rotateArrayAnticlockwise([2,4,6,8,10,12,14,16,18,20], 10)
