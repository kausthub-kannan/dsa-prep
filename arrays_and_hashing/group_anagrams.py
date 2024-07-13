class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        import collections as c

        d = {}

        for i in strs:
            curr = i
            curr = "".join(sorted(curr))

            if curr in d:
                d[curr].append(i)
            else:
                d[curr] = [i]
        
        return list(d.values())


s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
s.groupAnagrams([""])

# Leetcode URL: https://leetcode.com/problems/group-anagrams/description/
