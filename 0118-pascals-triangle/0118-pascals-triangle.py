class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # happy cases
        # inputs: 2
        # output: [[1], [1,1]]

        # input: 4
        # output: [[1], [1,1], [1,2,1], [1,3,3,1]]

        # edge cases
        # input: 1
        # output: [[1]]

        # tabulation
        # res = [] the size of n
        # res[0] = [[1]]
        # if n > 1
        #   res[1] = [[1], [1,1]]

        # iterate thru the from 2 to n
        #   curr_lst = []
        #   add 1 to the curr lst
        #   iterate thru the prev array from second ele to the end
        #       add the curr - 1 and curr ele
        #       append it to the curr lst
        #   add 1 to the curr lst
        #   curr res list = curr lst
        # return res list

        res = [[] for _ in range(numRows)] 
        res[0] = [1]
        if numRows > 1:
            res[1] = [1,1]

        for i in range(2, len(res)):
            res[i].append(1)
            prev_lst = res[i - 1]
            for j in range(1, len(prev_lst)):
                res[i].append(prev_lst[j] + prev_lst[j - 1])

            res[i].append(1)
            
        return res

        

        