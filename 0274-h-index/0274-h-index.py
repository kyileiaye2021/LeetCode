class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # input: [1,3,3,3,4]
        # output: 3

        # input: [3,1,2,6,7,1]
        # output: 3

        # [1,1,2,3,6,7]
       
        # input: [1,2,2,0,3]
        # output: 2

        # input: [1,2,3]
        # output: 2

        # input: [0,1,0,3]
        # output: 1

        # input: [0,0,0]
        # output: 0

        # input: [3, 100]
        # output: 2

        # input: [5]
        # output: 1

        # input: [1]
        # output: 1

        # input: [1,3,1]
        # output: 1

        # # brute force --> nested loop
        # # sort the array / count the nums when iterating the array from end '
        # citations.sort()
        # n = len(citations)
        
        # for i in range(n):

        #     # num of books that have at least citations[i] in the arr => n-i
        #     # check if citations at ith position is at least n-i

        #     if citations[i] >= n - i:
        #         return n - i
        # return citations[0]
        
        # descending order and keep track of how many papers have at least ith ciations
        citations.sort(reverse=True)
        count = 1

        for ct in citations:
            if ct >= count:
                count += 1
            else:
                return count - 1
        return count - 1
