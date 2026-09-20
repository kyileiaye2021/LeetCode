class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        # sorting
        # O(nlogn)

        # [1,2,4,5]
        
        # create a set of values ranging from i to j 
        # iterate thru nums
        #   check if the curr n is in the set
        #       remove from the set
        # return the list

        smallest = min(nums)
        largest = max(nums)

        num_set = set(nums)
        res = []

        for i in range(smallest, largest + 1):
            if i not in num_set:
                res.append(i)

        return res