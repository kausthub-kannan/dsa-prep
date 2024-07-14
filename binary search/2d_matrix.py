"""
LINK: https://leetcode.com/problems/search-a-2d-matrix/
Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    i, j = 0, m * n - 1
    while i <= j:
        mid = (i + j) // 2
        row, col = mid // n, mid % n
        guess = matrix[row][col]
        if guess == target:
            return 'true'
        elif guess > target:
            j = mid - 1
        else:
            i = mid + 1
    return 'false'

def read_n_lines(N):
    while True:
        lines = list(islice(map(loads, stdin), N))
        if not lines:
            break
        yield lines

f = open('user.out', 'w')
for case in read_n_lines(2):
    f.write(f"{searchMatrix(*case)}\n")
    

        
