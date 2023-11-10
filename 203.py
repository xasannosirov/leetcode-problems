class Solution:
    def removeElements(self, head, val: int):
        prev = None
        cur_node = head
        while cur_node:
            if cur_node.val == val:
                if prev:
                    prev.next = cur_node.next
                else:
                    head = cur_node.next
                cur_node = cur_node.next  
            else: 
                prev = cur_node
                cur_node = cur_node.next
        return head
