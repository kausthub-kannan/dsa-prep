"""
LINK: https://leetcode.com/problems/car-fleet/
Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Example 2:

Input: target = 10, position = [3], speed = [3]

Output: 1

Explanation:

There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]

Output: 1

Explanation:

The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
"""

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []

    for pos, speed in sorted(zip(position, speed), reverse=True):
        eta = (target - pos) / speed
        if not stack or eta > stack[-1]:
            stack.append(eta)

    return len(stack)

def read_n_lines(N):
    while True:
        lines = list(islice(map(loads, stdin), N))
        if not lines:
            break
        yield lines

f = open('user.out', 'w')
for case in read_n_lines(3):
    f.write(f"{carFleet(*case)}\n")
