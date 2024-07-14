"""
LINK: https://leetcode.com/problems/koko-eating-bananas/

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

def minEatingSpeed(piles: List[int], h: int) -> int:
    s, l = 1, max(piles)
    def neededSpeed(cnt):
        return sum(ceil(i/cnt) for i in piles) <= h

    while s < l:
        mid = (s + l) // 2
        if neededSpeed(mid):
            l = mid
        else:
            s = mid + 1
    return s


def read_n_lines(N):
    while True:
        lines = list(islice(map(loads, stdin), N))
        if not lines:
            break
        yield lines

f = open('user.out', 'w')
for case in read_n_lines(2):
    f.write(f"{minEatingSpeed(*case)}\n")
    
