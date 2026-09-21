class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # happy cases
        # egg, add
        # true

        # tap, pit
        # true

        # add, gap
        # false

        # f3, g1
        # true

        # ss4, tte
        # true

        # edge cases
        # ab, cde
        # false

        # '', ''
        # true

        # map
        # itereate thru s and t 
        #   if curr s char not in map
        #       curr s char : curr t char
        #       add pair to map
        #   else:
        #       if curr t char == t char in the map
        #           move s and t ptrs
        #       else
        #           return False

        # return True

        s_to_t_pairs = {}
        t_to_s_pairs = {}
        if len(s) != len(t):
            return False

        s_ptr = 0
        t_ptr = 0

        while s_ptr < len(s):
            if s[s_ptr] not in s_to_t_pairs:
                s_to_t_pairs[s[s_ptr]] = t[t_ptr]

            else:

                if t[t_ptr] != s_to_t_pairs[s[s_ptr]]:
                    return False

            if t[t_ptr] not in t_to_s_pairs:
                t_to_s_pairs[t[t_ptr]] = s[s_ptr]

            else:
                if s[s_ptr] != t_to_s_pairs[t[t_ptr]]:
                    return False

            s_ptr += 1
            t_ptr += 1

        return True





    
        