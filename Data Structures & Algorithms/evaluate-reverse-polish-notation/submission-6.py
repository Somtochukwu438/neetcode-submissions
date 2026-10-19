class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            # print(stack)
            if item in "+-*/":
                b, a = stack[-1], stack[-2]
                for _ in range(2):
                    stack.pop(-1)
                temp = 0
                if item == "+":
                    temp = a + b
                elif item == "-":
                    temp = a - b
                elif item == "*":
                    temp = a * b
                else:
                    temp = a / b
                stack.append(int(temp))
            else:
                stack.append(int(item))
        return stack[0]