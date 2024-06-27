class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Is one of the list can be empty?
        # Can the index sum of the two pairs of str be the same? #Yes we have to 
        # return both
        # Is it possible that there is no common ele in two strings? #No
        # Are there repetitive strings in the list? #No
        # Can there be more than 1 common ele in the list #Yes
        
        #Assumption
        # all ele in str 1 and 2 are unique
        # there will be at least one common string in both str 1 and str 2.
        
        # High Level Planning
        # * Brute Force Approach
        #       * iterate over the list1 and find curr ele in lst 2
        #       * create a list to store the index sum
        # * Index Mapping Approach
        #       * iteate over list 1 and fill the map {ele: index}
        #       * iterate over list 2 and check the common ele
        #       * check index sum
        
        #Low level Planniing
        #create a index map for list1
        #iterate over list1 to fill up the index_map1
        #create a index map for sum
        #create a min_index_sum
        #iterate over list2
            #check if the curr ele in index_map1
                # add the curr ele index and index_map1 curr key value
                # add the key index pair to sum_index map dict
                # also check the curr sum is min_index_sum and update that var
        #create a list        
        #iterate over dict 
            #check the curr key value is the same as min_index_sum
                #append to the list
        
        #filling up indices of eles in list1 into dict
        index_map1 = {} 
        for i, ele in enumerate(list1):
            index_map1[ele] = i
        
        index_sum_map = {} #common ele dict with sum index
        min_index_sum = float('inf')
        for i, ele in enumerate(list2):
            if ele in index_map1: 
                temp_index = i + index_map1[ele] 
                index_sum_map[ele] = temp_index
                
                if temp_index < min_index_sum:
                    min_index_sum = temp_index
        
        min_index_sum_ele_lst = [] 
        for key, value in index_sum_map.items():
            if value == min_index_sum:
                min_index_sum_ele_lst.append(key)
                
        return min_index_sum_ele_lst