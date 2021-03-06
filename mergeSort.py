# O(nLog(n)) time | O(N) space
def mergeSort(array):
    mergeSortHelper(array, 0, len(array) - 1)
    return array

def mergeSortHelper(array, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    mergeSortHelper(array, start, mid)
    mergeSortHelper(array, mid + 1, end)
    merge(array, start, mid, end)

def merge(array, start, mid, end):
    temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= end:
        temp.append(array[j])
        j += 1

    pos = 0
    for x in range(start, end + 1):
        array[x] = temp[pos]
        pos += 1

print(mergeSort([5,4,3,2,1]))
