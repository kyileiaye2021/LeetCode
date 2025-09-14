class Solution:
    def candy(self, ratings: List[int]) -> int:

        # happy cases
        # input: ratings: [1,0,2]
        # output: 5

        # input: ratings: [1,2,2]
        # output: 4

        # input: ratings = [1,2,3]
        # output: 5

        # input: ratings = [1,0,1,1,0]
        # output: 8

        # edge cases
        # input: ratings = [2]
        # output: 1

        # inupt: ratings = [3,3]
        # output: 2

        # if there is only one ele, return 1
        # total = 1
        # iterate thru the list from the second one
        #   increment the total
        #   check if curr ele is greater than or less than the prev ele
        #       increment the total
        
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)