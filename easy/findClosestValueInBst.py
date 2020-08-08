class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# Average: O(Log(n)) time | O(Log(n)) space
# Worst: O(n) time | O(n) space
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float('inf'))
#
# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         return closest

# Average: O(Log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest




root = Node(50)
insert(root, Node(30))
insert(root, Node(20))
insert(root, Node(40))
insert(root, Node(70))
insert(root, Node(60))
insert(root, Node(80))

print(findClosestValueInBst(root, 76))
