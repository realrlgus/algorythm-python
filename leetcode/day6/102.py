from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, depth ,ans):
    if not node:
        return
    if depth >= len(ans):
        ans.append([])
    ans[depth].append(node.val)
    dfs(node.left, depth + 1, ans)
    dfs(node.right, depth + 1, ans)
            
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        dfs(root, 0, ans)
        return ans