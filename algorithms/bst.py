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
    
    # this builds a binary tree not a BST
    def build_tree_from_in_pre_order(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_position_inorder = inorder.index(root.val)
        root.left = self.build_tree_from_in_pre_order(preorder[1:root_position_inorder+1], inorder[:root_position_inorder])
        root.right = self.build_tree_from_in_pre_order(preorder[root_position_inorder+1:], inorder[root_position_inorder+1:])
        return root


if __name__ == "__main__":
    preorder = [7, 4, 3, 2, 1, 11, 9, 25, 29]
    inorder = [1, 2, 3, 4, 7, 9, 11, 25, 29]
    bst = BST()
    root = bst.build_tree_from_in_pre_order(preorder, inorder)
    