class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = [[] for _ in range(rowIndex + 1)]
        res[0] = [1]
        if rowIndex > 0:
            res[1] = [1,1]

        for i in range(2, len(res)):
            prev_lst = res[i - 1]

            res[i].append(1)

            for j in range(1, len(prev_lst)):
                res[i].append(prev_lst[j] + prev_lst[j - 1])

            res[i].append(1)
            
        return res[-1]
        