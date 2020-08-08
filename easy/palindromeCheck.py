# O(n^2) time | O(n) space
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return reversedString == string

# O(n) time | O(n) space
def isPalindrome(string):
    reversedString = []
    for i in reversed(range(len(string))):
        reversedString.append(string[i])
    return string == "".join(reversedString)

# O(n) time | O(n) space
def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)

# O(n) time | O(1) space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string)-1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
