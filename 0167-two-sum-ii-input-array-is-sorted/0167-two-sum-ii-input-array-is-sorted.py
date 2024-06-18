class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #pretty similar to two sum
        #create a map {ele : index}
        #iterate over the list
            #diff = target - curr_ele
            #if the diff already in the map
                #return the list of [dict_value+1, curr_index+1]
            #add the key_val in the dict
            
        index_map = {}
        
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in index_map:
                return [index_map[diff] + 1, i + 1]
            index_map[numbers[i]] = i
        