class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # hashmap to store the ele , freq
        # max heap (freq, ele)
        # pop out the tuples for k times
        # output - num of ele left

        ele_count = Counter(arr)

        min_heap = [(count, ele) for ele, count in ele_count.items()]
        heapq.heapify(min_heap)

        for _ in range(k):
            count, ele = heapq.heappop(min_heap)
            count -= 1
            if count > 0:
                heapq.heappush(min_heap, (count, ele))

        return len(min_heap)

        