class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # hashmap {ele : freq}
        # sliding window

        # fruits = [1,1,1,2]
        # output: 4

        # fruit = [1,2,3,2,2]
        # output: 4

        # fruit = [1,2,3,1,1]
        # output: 3

        # fruit = [0,1,0,0]
        # output: 4

        # fruit = [0,0,0,0]
        # output: 4

        # fruit = [1,2,4,3,4]
        # output: 3

        # l and r at index 0
        # hashmap to store the ele and their freq
        # iterate thru the ele until r reaches the end
        #   if curr ele is in the hashmap
        #       increment the freq of the ele in hashmap
        #       keep track of the max ele
        #       increment the r 
        #   else
        #       check if hashmap size is already 2
        #           decrement freq of the l ele 
        #           if l ele becomes 0, remove the ele from hashmap
        #           decrement l
        #       else: 
        #           add the ele to the hashmap with freq of 1

        # return max window

        l = 0
        r = 0
        map = {}
        max_window = 0
        while r < len(fruits):
            if fruits[r] in map:
                map[fruits[r]] += 1
            
            else:
                while len(map) >= 2:
                    map[fruits[l]] -= 1
                    if map[fruits[l]] == 0:
                        del map[fruits[l]]
                    l += 1
                
                map[fruits[r]] = 1

            curr_window = r - l + 1
            max_window = max(max_window, curr_window)
            r += 1 

        return max_window

        