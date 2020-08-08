# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or threeLargest[2] < num:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or threeLargest[1] < num:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or threeLargest[0] < num:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]



print(findThreeLargestNumbers([5,6,1,7,11,2,8]))
