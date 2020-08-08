# O(N^2) time | O(1) space
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestidx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if array[smallestidx] > array[i]:
                smallestidx = i
        array[currentIdx], array[smallestidx] = array[smallestidx], array[currentIdx]
        currentIdx += 1
    return array

print(selectionSort([5,4,3,2,1]))
