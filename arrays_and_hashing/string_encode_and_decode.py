"""
Link: https://neetcode.io/problems/string-encode-and-decode
"""

class Solution:
    def __init__(self):
        self.idx = list()

    def encode(self, strs: List[str]) -> str:
        # return "$^_^$".join(strs)
        curr = 0
        for i in map(len, strs):
            self.idx.append(i+curr)
            curr = self.idx[-1]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        # return s.split(sep="$^_^$")
        print(self.idx)
        print(*zip([0] + self.idx, self.idx))
        return [s[i:j] for i,j in zip([0] + self.idx, self.idx)]

s = Solution()
encoded_s = s.encode(["neet","code","love","you"])
decoded_s = s.decode(encoded_s)

encoded_s = s.encode(["we","say",":","yes"])
decoded_s = s.decode(encoded_s)


