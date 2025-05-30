class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_element = val
        elif val >= self.min_element:
            self.stack.append(val)
        else:
            self.stack.append(2 * self.min_element - val)
            self.min_element = val

    def pop(self) -> None:

    def top(self) -> int:

    def getMin(self) -> int:

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()