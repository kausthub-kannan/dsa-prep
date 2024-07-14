"""
LINK: https://leetcode.com/problems/binary-search/description/

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1  
"""

def search(nums: List[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1 

def read_n_lines(N):
    while True:
        lines = list(islice(map(loads, stdin), N))
        if not lines:
            break
        yield lines


f = open('user.out', 'w')
for case in read_n_lines(2):
    f.write(f"{search(*case)}\n")
            
