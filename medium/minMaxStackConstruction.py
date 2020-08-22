class MinMaxStack:
    def __init__(self):
        self.MinMaxStack = []
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # O(1) time | O(1) space
    def pop(self):
        self.MinMaxStack.pop()
        self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.MinMaxStack):
            lastMinMax = self.MinMaxStack[len(self.MinMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.MinMaxStack.append(newMinMax)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["max"]
