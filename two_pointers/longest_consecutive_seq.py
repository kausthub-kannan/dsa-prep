class Solution:
    def __init__(self):
        self.t, self.best = 0, 0

    def longestConsecutive(self, nums: List[int]) -> int:
        l = list(set(nums))
        heapq.heapify(l)
        while l:
            pop_val = heapq.heappop(l)
            self.t += 1
            if l == [] or l[0] != pop_val + 1:
                self.best = max(self.t, self.best)
                self.t = 0
                
        return self.best

'''
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
