"""
LINK: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4
"""

def largestRectangleArea(heights: List[int]) -> int:
    max_area = 0
    stack = []
    for i , h in enumerate(heights):
        idx = i
        if not stack:
            stack.append((i , h))
            continue
        while stack and stack[-1][1] > h:
            idx , he = stack.pop()
            max_area = max(max_area , (i - idx ) * he)
        stack.append((idx , h))
        
    while stack:
        idx , he = stack.pop()
        max_area = max(max_area , (i - idx + 1) * he) 
    return max_area

f = open('user.out', 'w')
for case in map(loads, stdin):
    f.write(f"{largestRectangleArea(case)}\n")
