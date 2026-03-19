class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        # res = []
        # recur(i, cur_lst)
        # base case
        # if i >= len(s)
        #   create a full str and add to res
        #   return
        #
        # add the cur ele to cur list
        # call recur on (i + 1)
        # pop the curr ele 
        # if the cur ele is alphabet
        #   add the cur ele (capital) to cur list
        #   call recur on (i + 1)
        #   pop the curr ele
        
        # call recur(0, cur_lst)
        # return res

        res = []
        cur_lst = []

        def recur(i, cur_lst):
            if i >= len(s):
                res.append(''.join(cur_lst))
                return

            cur_lst.append(s[i].lower())
            recur(i + 1, cur_lst)
            cur_lst.pop()

            if s[i].isalpha():
                cur_lst.append(s[i].upper())
                recur(i + 1, cur_lst)
                cur_lst.pop()
        
        recur(0, cur_lst)
        return res



            




        