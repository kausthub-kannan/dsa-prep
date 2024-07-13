"""
LINK: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def removeNode(node, n):
            if not node:
                return 0
            cnt = removeNode(node.next, n)
            if cnt == n:
                node.next = node.next.next
            return cnt + 1
    
        return head.next if removeNode(head, n) == n else head
            
        
