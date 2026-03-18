class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recur
        res = []
        cur_lst = []
        cur_sum = 0

        def recur(i, cur_lst, cur_sum):

            if cur_sum == target:
                res.append(cur_lst.copy())
                return

            if cur_sum > target:
                return

            for j in range(i, len(candidates)):
                cur_lst.append(candidates[j])
                cur_sum += candidates[j]
                recur(j, cur_lst, cur_sum)
                cur_lst.pop()
                cur_sum -= candidates[j]

                # recur(j + 1, cur_lst, cur_sum)
                # cur_lst.pop()
                # cur_sum -= candidates[i]

        recur(0, cur_lst, cur_sum) 
        return res
