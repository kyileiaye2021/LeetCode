class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # base case
        # if cur str len == n 
        #   add the cur str to res
        # iterate thru the mapped str of curr
        #   add the curr char to curr str
        #   call recursive call on mapped letter
        #   back track to prev state
        # return res
        ph_map = {"2": ["a","b","c"],
                  "3": ["d","e", "f"],
                  "4": ["g", "h", "i"],
                  "5": ["j","k", "l"],
                  "6": ["m","n", "o"],
                  "7": ["p","q", "r", "s"],
                  "8": ["t","u", "v"],
                  "9": ["w","x", "y", "z"]
                }
        cur_str = []
        res = []
        def recur(i):
            nonlocal cur_str
            # base case
            if i >= len(digits) or len(cur_str) == len(digits):
                res.append(''.join(cur_str))
                return
            
            for j in range(len(ph_map[digits[i]])):
                print(ph_map[digits[i]][j])
                cur_str.append(ph_map[digits[i]][j])
                recur(i + 1)
                cur_str.pop()

        recur(0)
        return res



