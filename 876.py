class Solution:
    def middleNode(self, head):
        res = list()
        cur_node = head
        while cur_node:
            res.append(cur_node.val)
            cur_node = cur_node.next

        ind = len(res)//2
        cur_node = head
        while ind:
            cur_node = cur_node.next
            ind-=1
        return cur_node
