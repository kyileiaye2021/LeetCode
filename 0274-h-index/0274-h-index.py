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
        
        # creating bucket sort
        n = len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            if c > n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        paper_count = 0
        for i in range(len(bucket) - 1, -1, -1):
            paper_count += bucket[i]
            if paper_count >= i:
                return i
