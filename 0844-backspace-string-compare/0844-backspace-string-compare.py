class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s = "a#b#c", t = "bd##c"
        # output: true

        # s = "abc#", t = "abd#"
        # output: true

        # s = "aef##", t = "ab#c#"
        # output: true

        # s = "a", t = "a#"
        # output: false

        # s = "a#", t = "bc##"
        # output: true

        # from backwards we iterate the s and t
        #   while the curr char is #
        #       increment the count
        #   while count > 0
        #       iterate thru the chars backwards
        # add the curr char to the new s
        count = 0
        new_s = ""
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '#':
                count += 1
                continue

            if count > 0:
                count -= 1
                continue
                
            new_s += s[i]

        new_t = ""
        count = 0
        for i in range(len(t) - 1, -1, -1):
            if t[i] == '#':
                count += 1
                continue

            if count > 0:
                count -= 1
                continue
                
            new_t += t[i]

        return True if new_s == new_t else False

        
        

