class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # s = ((
        # locked = 00
        # output: ()
        # true

        # s = ()
        # true

        # s= (()
        # locked = 000
        # false

        # s = ((()
        # locked = 1100
        # true

        # s = ())
        # locked = 110
        # false

        # s = )())
        # locked = 0001
        # true

        # stack
        # iterate thru s
        #   if s[i] is (
        #       add the ( to stack
        #   else
        #       if stack 
        #           pop the stack
        #       else
        #           if lock[i] != 0
        #               return false
        #           else:
        #               add ( to stack
        # return True if not stack else false

        locked_s = []
        unlocked_s = []
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked_s.append(i)
            else:
                if s[i] == '(':
                    locked_s.append(i)
                else:
                    if locked_s:
                        locked_s.pop()
                    elif unlocked_s:
                        unlocked_s.pop()
                    else:
                        return False

        while locked_s:
            if unlocked_s and locked_s[-1] < unlocked_s[-1]:
                unlocked_s.pop()
                locked_s.pop()
            else:
                return False
    
        return True if len(unlocked_s) % 2 == 0 else False
