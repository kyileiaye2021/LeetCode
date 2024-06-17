class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #Brute Force Method
        #create a list to store the indices
        #iterate over the list 
        #use the nested loop 
        #for each outer iteration, add each curr element to each ele in inner loop
        #check if it is equal to target val

        index_lst = []
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_lst.append(i)
                    index_lst.append(j)
        return index_lst

        '''
        #Using Hashmap to store 
        prevMap = {} #value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            
            else:
                prevMap[n] = i



        