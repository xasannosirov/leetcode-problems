class Solution:
    def isPalindrome(self, head) -> bool:
        res = list()
        cur_node = head
        while cur_node:
            res.append(cur_node.val)
            cur_node = cur_node.next
        return res == res[::-1]
