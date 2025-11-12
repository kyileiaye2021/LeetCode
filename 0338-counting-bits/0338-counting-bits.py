class Solution:
    def countBits(self, n: int) -> List[int]:
        # input:n = 1
        # output: [0, 1]

        # input: n = 2
        # output: [0, 1, 1]

        # input n = 3
        # output: [0, 1, 1, 2]

        # create a res list with the size of n + 1 initialized to 0
        # add 0 to the first place 

        # total

        # iterate thru from 1 to n + 1
            # curr = i
            # iterate thru curr until it becomes 0
            #   check if ele at the curr pos is not 0
            #       retrieve the num of 1s in that pos and add it to res[i]
            #       
            #   else
            #       res[i] += n % 2 = v and add v to total
            #       update n to n // 2
            #   
            # return the res list

        res  = [0] * (n + 1) # O(n) space
        res[0] = 0

        for i in range(1, n + 1): # O(n) time??
            curr = i

            while curr != 0:

                if res[curr] != 0: # if the res is already stored in the res, retrieve and reuse it
                    res[i] += res[curr]
                    curr = 0

                else:
                    res[i] += curr % 2
                    curr = curr // 2

        return res 



