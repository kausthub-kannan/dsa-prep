"""
LINK: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""

def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1 #LEFT AND RIGHT POINTERS
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[r]:
            r = mid
        else:
            l = mid + 1
    return nums[l]

f = open('user.out', 'w')
for case in map(loads, stdin):
    f.write(f"{findMin(case)}\n")
