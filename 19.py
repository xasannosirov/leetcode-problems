class Solution:
    def removeNthFromEnd(self, head, n: int):
        slow = head
        fast = head
        
        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
