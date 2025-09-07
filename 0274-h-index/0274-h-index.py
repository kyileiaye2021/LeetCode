class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        #          1, 4, 7, 9, 10
        # idex     0, 1, 2, 3, 4
        # curCount 5, 4, 3, 2, 1
        # curCount = n - i
        
        # in each iteration, all the num of paper has at least ith citation
        # we have to return when the num of citation becomes equal or greater than the num of paper
        
        # if we go thru the ele, the num of paper becomes smaller 
        for i, v in enumerate(citations):
            curCount = n-i
            if v >= n-i:
                return n-i
        
        return min(citations)