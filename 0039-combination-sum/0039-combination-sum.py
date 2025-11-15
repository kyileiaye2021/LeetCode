class Solution:
    def backtrack(self, i, candidates, target, curr_sum, curr_lst, res_lst):

        # unique combination
        #  if the num is included in one path, exclude it in another path

        # base case
        # if curr sum becomes target
        #   make a copy of curr lst and add it to res list
        #   return 
        # if curr i becomes the len of candidates or curr sum exceed target
        #   return 

        # add the curr ith ele to the curr list
        # add the curr ith ele to the sum
        # call recursive func on the curr sum and list
        # remove the curr ith ele from the curr list
        # remove the curr ith ele from the sum
        # call recursive func on the curr sum and list

        # if the path sum becomes target, store it in the res
        if curr_sum == target:
            res_lst.append(curr_lst.copy())
            return

        if i >= len(candidates) or curr_sum > target:
            return 

        # include the curr ith ele 
        curr_lst.append(candidates[i])
        curr_sum += candidates[i]
        self.backtrack(i, candidates, target, curr_sum, curr_lst, res_lst)

        # backtrack and exclude the curr ith ele
        curr_lst.pop()
        curr_sum -= candidates[i]
        self.backtrack(i + 1 , candidates, target, curr_sum, curr_lst, res_lst)

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
        curr_sum = 0
        i = 0
        curr_lst = []
        res_lst = []
        self.backtrack(0, candidates, target, curr_sum, curr_lst, res_lst)
        return res_lst





