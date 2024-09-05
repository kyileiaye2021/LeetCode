class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Happy case:
        # input: list1 = ["Shogun", "KFC", "Burger"], lst2 = ["Burger", "Shogun", "KFC"]
        # output: ["Shogun"]
        
        # Edge case:
        # input: lst1 = ["Shogun"], lst2= ["Shogun"]
        # output: ["Shogun"]
        # input: lst1 = ["KFC", "Burger"], lst2= ["Burger", "KFC"]
        # output: ["KFC", "Burger"]
        
        # Hashmap Approach
        # create a res lst
        # create a hashmap lst1_map
        # iterate over the lst1 and fill the hashmap up 
        # create another hashmap comm_str_map
        # iterate over the lst2
        #     check if the curr ele is in lst1_map
        #          add it to comm_str_map with the index sum
        # iterate over the comm_str_map
        #     get the min_index_sum
        # iterate over the comm_str_map
        #     check if the curr key value is the same as min_index_sum
        #       append the curr key in the res
        # return res
        
        res = []
        lst1_map = {}
        for i in range(len(list1)):
            lst1_map[list1[i]] = i
                
        comm_str_map = {}
        for i in range(len(list2)):
            if list2[i] in lst1_map:
                comm_str_map[list2[i]] = lst1_map[list2[i]] + i
        
        min_index_sum = float('inf')
        for key in comm_str_map:
            if comm_str_map[key] < min_index_sum:
                min_index_sum = comm_str_map[key]
            
        for key in comm_str_map:
            if comm_str_map[key] == min_index_sum:
                res.append(key)
                
        return res
        