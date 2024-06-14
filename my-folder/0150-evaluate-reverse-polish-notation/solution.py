class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = [ '+', '-', '*', '/']
        for token in tokens:

            match token:
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    if a / b < 0:
                        stack.append(ceil(a / b))
                    else:
                        stack.append(floor(a / b))
                case _:
                    stack.append(int(token))
        
        return stack.pop()


