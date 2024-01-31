class MyQueue:

    def __init__(self):
        self.primary_stack = []
        self.secondary_stack = []
        self.first = None

    def push(self, x: int) -> None:
        self.first = x if not self.first else self.first
        self.primary_stack.append(x)

    def pop(self) -> int:
        while(self.primary_stack):
            self.secondary_stack.append(self.primary_stack.pop())
        
        first = self.secondary_stack.pop()
        self.first = self.secondary_stack.pop() if self.secondary_stack else None
        
        if self.first:
            self.primary_stack.append(self.first)

            while(self.secondary_stack):
                self.primary_stack.append(self.secondary_stack.pop())

        return first

    def peek(self) -> int:
        return self.first

    def empty(self) -> bool:
        return len(self.primary_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
