class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        
        for e,i in enumerate(nums):
            if target-i not in d:
                d[target-i] = e
                
        for e,i in enumerate(nums):
            if i in d and d[i]!=e:
                return [e, d[i]]

s = Solution()
s.twoSum([2,7,11,15], 9)
s.twoSum([[3,2,4], 6)

# Leetcode URL: https://leetcode.com/problems/two-sum/description/
