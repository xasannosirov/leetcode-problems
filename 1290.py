class Solution:
    def getDecimalValue(self, head) -> int:
        res = str()
        cur_node = head
        while cur_node:
            res += str(cur_node.val)
            cur_node = cur_node.next
        return int(res,2)
