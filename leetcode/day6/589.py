from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution: 
    def preorder(self, root: 'Node') -> List[int]:        
        if not root:
            return []
        output = []
        output.append(root.val)
        for s in root.children:
            output += self.preorder(s) 
        return output