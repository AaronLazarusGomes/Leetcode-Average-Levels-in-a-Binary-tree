# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        hashmap = {}
        tree_levels = self.getLevels(root, 0, 0, hashmap)
        answer = []
        for key, value in tree_levels.items():
            item = tree_levels[key]
            result = sum(item) / len(item)
            answer.append(result)
        return answer
    
    def getLevels(self, root, level, l, hashmap):
        if(root == None):
            return 0
        if(level in hashmap):
            hashmap[level].append(root.val)
        else:
            hashmap[level] = [root.val]
        self.getLevels(root.left, level + 1, l + 1, hashmap)
        self.getLevels(root.right, level + 1, l + 1, hashmap)
        return hashmap
