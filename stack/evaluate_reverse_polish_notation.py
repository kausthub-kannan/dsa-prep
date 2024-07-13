class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def calculate(b, a, opt):
            match opt:
                case '+': return a + b
                case '-': return a - b
                case '*': return a * b
                case '/': return int(a / b) 

        stack = []
        op = {'+', '-', '*', '/'}

        for i in tokens:
            if i in op:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(calculate(b, a, i))
            else:
                stack.append(int(i))

        return stack[0]


# Leetcode URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
