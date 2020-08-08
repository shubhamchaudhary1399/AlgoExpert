#time complexity O(n^2) | space complexity O(1)
# def twoNumberSum(array, target):
#     for i in range(len(array)):
#         firstSum = array[i]
#         for j in range(i+1, len(array)):
#             secondSum = array[j]
#             targetSum = firstSum + secondSum
#             if targetSum == target:
#                 return [i, j]
#     return []

#O(n) time | O(n) space
# def twoNumberSum(array, target):
#     seen = {}
#     for i, v in enumerate(array):
#         remaining = target - v
#         if remaining in seen:
#             return [seen[remaining], i]
#         else:
#             seen[v] = i
#     return []

# O(nlogn) time | O(1) space | array order is not preserved
def twoNumberSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        targetSum = array[left] + array[right]
        if targetSum == target:
            return [array[left], array[right]]
        elif targetSum < target:
            left += 1
        elif targetSum > target:
            right -= 1
    return []



print(twoNumberSum([3,2,4], 6))
