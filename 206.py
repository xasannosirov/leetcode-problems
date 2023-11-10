class Solution:
    def reverseList(self, head):
        prev = None
        cur_node = head
        while cur_node:
            temp = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = temp
        return prev
