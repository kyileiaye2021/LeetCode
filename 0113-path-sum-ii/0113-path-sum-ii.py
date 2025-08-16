# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, targetSum, currSum, currList, allList):
        if not root:
            return 

        currSum += root.val
        currList.append(root.val)
        print(f'CurrList: {currList}')
        if not root.left and not root.right:
            if currSum == targetSum:
                allList.append(list(currList))
        
        self.dfs(root.left, targetSum, currSum, currList, allList)
        self.dfs(root.right, targetSum, currSum, currList, allList)
        currList.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # base case
        # if the curr node becomes null --> return
        # currSum += root.val
        # currList.append(root.val)
        # check if we reach the leaf node
        #   check if the currSum is equal to the targetSum
        #       add the currList to all list
        # go to the left subtree
        # go to the right subtree

        currList = collections.deque()
        allList = []
        currSum = 0
        self.dfs(root, targetSum, currSum, currList, allList)
        return allList 

    
