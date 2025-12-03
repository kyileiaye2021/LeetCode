class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # happy cases
        # pattern = "ab", s = "dog cat"
        # true

        # pattern = "aba", s = "dog cat dog"
        # true

        # pattern = "aba", s = "dog cat fish"
        # false

        # edge cases
        # pattern = "aaa", s = "dog cat dog"
        # false

        # pattern = "a", s = "dog"
        # true

        # pattern = "aaa", s = "aa aa aa aa"
        # false

        # pattern = "aaaa", s = "aa aa aa"
        # false

        # separate out the words in s
        # hashmap {a: dog, b: cat}
        # iterate thru the pattern
        #   check if the curr pattern c in hashmap
        #       check if the pattern c value is not the same as the curr s 
        #           return false
        #   else
        #       add the curr pattern with the corresponding word
        # return true

        pattern_map = {}
        s_map = {}
        s_lst = s.split()
        
        s_len = len(s_lst)
        pattern_len = len(pattern)

        if s_len != pattern_len:
            return False

        for i, c in enumerate(pattern):
            if c in pattern_map:
                if pattern_map[c] != s_lst[i]:
                    return False
            else:
                if s_lst[i] in s_map:
                    return False
                pattern_map[c] = s_lst[i]
                s_map[s_lst[i]] = c

        return True




