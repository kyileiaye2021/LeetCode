class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        def recur(i, cur_lst):
            # base case
            if i >= len(nums):
                return

            for j in range(i, len(nums)):
                cur_lst.append(nums[j])
                recur(j + 1, cur_lst)
                res.append(cur_lst.copy())
                cur_lst.pop()

        recur(0, [])
        return res

            

        