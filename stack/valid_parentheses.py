def isValid(s: str) -> bool:
    stack = []
    closed = {'}', ')', ']'}

    def check(a,b):
        match a:
            case '(': return b == ')'
            case '{': return b == '}'
            case '[': return b == ']'

    for i in s:
        if i in closed:
            if not stack: return "false"

            if check(stack[-1], i):
                stack.pop()
            else:
                return "false"
        else:
            stack.append(i)

    if stack:
        return "false"

    return "true"
    


f = open('user.out', 'w')
for case in map(loads, stdin):
    f.write(f"{isValid(case)}\n")

# Leetcode: https://leetcode.com/problems/valid-parentheses/
