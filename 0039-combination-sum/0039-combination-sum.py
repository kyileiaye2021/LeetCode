class Solution:
    def dp_helper(self, candidates, i, remaining, memo):

        # base case
        if remaining == 0:
            # find the path that sum up to target
            return [[]]

        if i >= len(candidates) or remaining < 0:
            # if the path sum exceed the target
            return []

        # dp case
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # include the curr ith ele
        include_combo = self.dp_helper(candidates, i, (remaining - candidates[i]), memo)
        include_combo = [[candidates[i]] + combo for combo in include_combo]

        # exclude the curr ith ele
        exclude_combo = self.dp_helper(candidates, i + 1, remaining, memo)

        # combine the two paths
        total_combo = include_combo + exclude_combo
        memo[(i, remaining)] = total_combo

        return memo[(i, remaining)]
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # happy cases
        # input: [2,3,6,7], target = 7
        # output: [[2,2,3], [7]]

        # input: [2], target - 2
        # output: [[2]]

        # edge cases
        # input: [], target = 0
        # output: []

        # input: [2, 3], target = 1
        # output: []

        # brute force  - tree to create the paths that ends with 0 at the end O(2^t)
        # backtracking 
        # create a res list
        # curr sum = 0
        # curr list - empty list
        memo:Dict[Tuple(int, int): List[List[int]]] = {}
        return self.dp_helper(candidates, 0, target, memo)
        


    
        




