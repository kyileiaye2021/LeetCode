class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input - array of ints, an int
        # output - array of ints

        # happy cases
        # input - nums = [1,1,1], k = 1
        # output - [1]

        # input - nums = [1,1,2], k = 2
        # output - [1,2] or [2,1]

        # edge cases
        # input - nums = [1], k =1
        # output - [1]

        # dict {ele: freq count}
        # for dict with freq count, we can only keep track of the 
        # largest freq count ele so we can sort the dict based on the freq vals
        # but it may take O(nlogn) time

        # so we will use bucket sort here
        # populate the dict with eles and their freq counts
        # create a bucket sort of input array size [index: count, [] of eles in the bucket]
        # insert the elements based on their freq count 
        # (index of the bucket is equal to the freq count of ele)
        # iterate over the bucket from the end and add the eles to the res list until the len of res list reaches to the k ele

        # create a dict {ele : freq_count} and populate the dict
        freq_dict = {}
        for ele in nums: 
            if ele not in freq_dict:
                freq_dict[ele] = 1

            else:
                freq_dict[ele] += 1

        # create a bucket (index will 
        count_bucket = [[] for i in range(len(nums) + 1)]

        # inserting the eles based on their freq count
        for ele in freq_dict:
            count_bucket[freq_dict[ele]].append(ele)

        res = []
        # iterate over the bucket in descending order to get the most k freq eles
        for i in range(len(count_bucket) - 1, 0, -1):
            for ele in count_bucket[i]:
                res.append(ele)
                if len(res) == k:
                    return res

        