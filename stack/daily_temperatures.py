class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack = []

        for i,v in enumerate(temp):
            while stack and stack[-1][0]<v:
                t, idx = stack.pop()
                res[idx] = (i-idx)
            stack.append((v,i))

        return res
