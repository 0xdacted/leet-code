# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return None
        
        fast, slow = head.next.next, head
        

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next
            
        return head