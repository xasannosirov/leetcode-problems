class Solution:
    def searchBST(self, root, val: int):
        while (root != None and root.val != val):
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root
