class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs(i)
        # if i >= len(candidates)
        #   add curr list to res list
        # add curr ele to the list
        # increment the cur sum
        # dfs(i) # include
        # backtrack and pop the curr ele
        # decrement cur sum
        # dfs(i + 1) # exclude  

        res = []

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
