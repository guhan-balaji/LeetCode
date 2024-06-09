class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_stack = None
        if not self.stack:
            min_stack = val
        else:
            min_stack = min(val, self.getMin())

        self.stack.append((val, min_stack))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        (top_val, _) = self.stack[-1]
        return top_val

    def getMin(self) -> int:
        (_, min_stack) = self.stack[-1]
        return min_stack

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
