class Solution:
    def checkValidString(self, s: str) -> bool:
        # (())
        # true

        # ())
        # false

        # )(
        # false

        # (*))
        # true

        # ())*
        # false

        # (*)
        # true

        # ((**
        # true

        # **((
        # false

        # ***
        # true

        # ****
        # true

        # 2 stacks
        # 1 for (
        # 1 for *

        open_s = []
        asterisk_s = []

        for i in range(len(s)):
            if s[i] == '(':
                open_s.append(i)
            
            elif s[i] == '*':
                asterisk_s.append(i)

            else: # closing
                if open_s:
                    open_s.pop()
                elif asterisk_s:
                    asterisk_s.pop()
                else:
                    return False
        
        while open_s and asterisk_s:
            if open_s[-1] < asterisk_s[-1]:
                open_s.pop()
                asterisk_s.pop()
            
            else:
                return False
            
        return True if not open_s else False





        