class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # happy cases
        # input: list1 - ['a','b', 'c'], list2 - ['a', 'c', 'd']
        # output: ['a']

        # edge cases
        # input: list1- ['a'], list2 - ['a']
        # output: ['a']

        # input: list1 - ['a', 'b'], list2 - ['b', 'a']
        # output: ['a', 'b'] or ['b', 'a']

        # Brute Force
        # hashmap

        # craete an empty common string hashmap
        # iterate over the ele in list1
        #   check if the  curr ele in list2
        #       add that ele with its index

        # iterate over list2 
        #   check if the curr ele is in common string hashmap
        #       update the value of the corresponding key to the sum of index

        # create a res list
        # create a min var 
        # iterate over the hashmap
        #   check if the curr value is smaller than min 
        #       update min var
        # iterate over the hashmap
        #   check if the value is equal to the min
        #   append the key to the res lisst

        # return res list 

        # Time - O(n)
        # Space - O(n)
        
        common = {}
        for i, ele in enumerate(list1):
            if ele in list2:
                common[ele] = i

        for i, ele in enumerate(list2):
            if ele in common:
                common[ele] += i

        res = []
        min_sum = float('inf')

        for sum in common.values():
            min_sum = min(min_sum, sum)

        for key, value in common.items():
            if value == min_sum:
                res.append(key)

        return res



