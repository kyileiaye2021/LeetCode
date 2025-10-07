class Solution:
    
    def __init__(self, w: List[int]):
        
        # create ranges for each num
        # [1,2,4]
        # [1,3,7] from 1-3 belongs to ele 2
        # from 3-7 belongs to ele 4
        self.ranges = []

        self.total = 0
        for weight in w:
            self.total += weight
            self.ranges.append(self.total)
        
    def pickIndex(self) -> int:
        # use random to pick the ele from the res
        rand_num = random.randint(1,self.total)

        # we have to find that num in the range array
        # since the arrr is sorted, we can use binary search

        l = 0
        r = len(self.ranges) - 1
        while l < r:
            mid = (l + r) // 2

            if self.ranges[mid] > rand_num:
                r = mid

            elif self.ranges[mid] < rand_num:
                l = mid + 1

            else:
                return mid

        return r
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()