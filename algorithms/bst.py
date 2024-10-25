#!/usr/bin/env python3

from typing import List, Optional

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def insert(self, root: Optional[TreeNode], item: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(item)
        if root.val >= item:
            if not root.left:
                root.left = TreeNode(item)
            else:
                self.insertIntoBST(root.left, item)
        else:
            if not root.right:
                root.right = TreeNode(item)
            else:
                self.insertIntoBST(root.right, item)
        return root

    def dfs_inorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (self.dfs_inorder(root.left) +
        [root.val] +
        self.dfs_inorder(root.right))

    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.delete_node(root.left, key)
        elif root.val < key:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            root.val = self._find_left_most_on_the_right(root.right)
            root.right = self.delete_node(root.right, root.val)
        return root

    def _find_left_most_on_the_right(self, root: Optional[TreeNode]) -> int:
        while root.left:
            root = root.left
        return root.val 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k  # Instance variable to track k across recursive calls
        self.result = None  # Instance variable to store the result
        self._inorder_traversal(root)
        return self.result

    def _inorder_traversal(self, node):
        if node is None:
            return
        self._inorder_traversal(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self._inorder_traversal(node.right)

                
        

