class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = set()
        self.n = n
        self.backtrack("", 0, 0)
        return list(self.result)

    def backtrack(self, res, cntO, cntC):
        if len(res)==self.n*2:
            if res not in self.result:
                self.result.add(res)
            return

        if cntO<self.n:
            self.backtrack(res+"(", cntO+1, cntC)

        if cntC<cntO:
            self.backtrack(res+")", cntO, cntC+1)

# Leetcode URL: https://leetcode.com/problems/generate-parentheses/description/
