class MinStack:

    def __init__(self):
        self.stk: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            min_stk = self.getMin() if self.getMin() < val else val
            self.stk.append((val, min_stk))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        (val, _) = self.stk[-1]
        return val        

    def getMin(self) -> int:
        (_, min_stk) = self.stk[-1]
        return min_stk


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
