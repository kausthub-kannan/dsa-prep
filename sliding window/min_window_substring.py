"""
LINK: https://leetcode.com/problems/minimum-window-substring/

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len, t_len = len(s), len(t)
        count = char = r = l = idx = 0
        hashmap = defaultdict(int)
        minlen = float('inf')

        for ch in t:
            hashmap[ch] += 1
        
        while r < s_len:
            if s[r] in hashmap:
                hashmap[s[r]] -= 1
                if hashmap[s[r]] >= 0:
                    count +=1 
            while count == t_len:
                if (r - l + 1) < minlen:
                    minlen = (r - l + 1)
                    idx = l
                
                if s[l] in hashmap:
                    hashmap[s[l]] += 1
                    if hashmap[s[l]] > 0:
                        count -= 1
                
                l += 1
            r += 1
        return "" if minlen == float('inf') else s[idx: idx+minlen]


# def read_n_lines(N):
#     while True:
#         lines = list(islice(map(loads, stdin), N))
#         if not lines:
#             break
#         yield lines

# f = open('user.out', 'w')
# for case in read_n_lines(2):
#     f.write(f'"{minWindow(*case)}"\n')
