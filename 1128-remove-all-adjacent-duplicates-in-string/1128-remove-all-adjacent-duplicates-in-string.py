class Solution:
    def rev(self, i, s, res):
        if i == len(s):
            return 
        if s[i] == res[-1]:
            res.pop()

        else:
            res.append(s[i])
        self.rev(i + 1, s, res)

    def removeDuplicates(self, s: str) -> str:
        res = ['']
        self.rev(0, s, res)
        return ''.join(res)

    # def rev(self, s, prev, res):
    #     if len(s) == 0:
    #         return 
        
    #     if s[0] != prev[-1]:
    #         res.append(s[0])
    #         prev.append(s[0])

    #     else:
    #         res.pop()
    #         prev.pop()

    #     self.rev(s[1:], prev, res)

    # def removeDuplicates(self, s: str) -> str:
    #     res = []
    #     prev = ['']

    #     # recursively solve this
    #     self.rev(s, prev, res)
    #     res_str = ''.join(res)
    #     return res_str

        