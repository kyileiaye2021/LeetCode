class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the list
        candidates.sort()
        res = []

        def recur(i, cur_lst, cur_sum):
            # base case
            if cur_sum == target:
                res.append(cur_lst.copy())
                return

            if cur_sum > target:
                return

            for j in range(i, len(candidates)):
                # check if the curr ele is equal to prev ele
                #   continue
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                cur_lst.append(candidates[j])
                cur_sum += candidates[j]
                recur(j + 1, cur_lst, cur_sum)
                cur_lst.pop()
                cur_sum -= candidates[j]

        recur(0, [], 0)
        return res

