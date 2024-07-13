min_ = lambda x, y: y ^ ((x ^ y) & -(x < y)); # min(x, y)
max_ = lambda x, y: x ^ ((x ^ y) & -(x < y)); # max(x, y)

def maxArea(height: List[int]) -> int:
    l_wall, r_wall = 0, len(height) - 1
    max_area = 0
    while l_wall < r_wall:
        curr_area = min_(height[l_wall], height[r_wall]) * (r_wall - l_wall)
        max_area = max_(max_area, curr_area)
        
        if height[l_wall] < height[r_wall]:
            l_wall += 1
        else:
            r_wall -= 1
    return max_area

            
f = open('user.out', 'w')
for case in map(loads, stdin):
    f.write(f"{maxArea(case)}\n")

'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
'''
