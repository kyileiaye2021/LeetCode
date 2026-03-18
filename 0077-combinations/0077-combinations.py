class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # recur(i, []):
        #   if len of curr list == k
        #       add the curr list to the res list
        #       return 
        #   if i >= n:
        #       return 
        #   iterate thru the ele from i + 1
        #       add the curr ele to curr list
        #       call recur(i + 1, curr list)
        #       backtrack and remove the curr ele 
        #   

        # iterate thru the ele n times
        #   call recur func (i)

        # return res
        res = []

        def recur(i, lst):
            if len(lst) == k:
                res.append(lst.copy())
                return

            if i > n:
                return 

            for j in range(i, n + 1):
                lst.append(j)
                recur(j + 1, lst)
                lst.pop()

        recur(1, [])

        return res


        