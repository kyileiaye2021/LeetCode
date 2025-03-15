class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # happy case
        # input: candies = [2,3,4], extracandies = 3
        # output: [true, true, true]

        # edge case
        # input: candies = [3,3], extracandies = 2
        # output: [true, true]

        # input: canides = [3,2], extracandies = -1
        # output: []

        # if the extracandies is less than 1
        #   return empty list
        # find the largest element in the list
        # res list
        # iterate the list
        #   add the extracandies to the curr candy
        #   check if the added candy is greater than or equal to the largest one
        #       add it to the res list
        # return res list

        if extraCandies <= 0:
            return []

        max_candy = 0
        for ele in candies:
            max_candy = max(max_candy, ele)

        res = []

        for candy in candies:
            new_candy = candy + extraCandies
            if new_candy >= max_candy:
                res.append(True)

            else:
                res.append(False)

        return res





