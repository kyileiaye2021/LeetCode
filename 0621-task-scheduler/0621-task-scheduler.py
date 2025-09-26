class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap to operate on the most freq task
        # time= 0
        # store the remaining task with the time when they will come back to be completed
        # until max heap is none or q is none
        #   increment time
        #   decrement the freq of the curr task
        #   the remaining task with the time will be stored in queue 
        #   if the time becomes the time when the same task can be completed
        #       push the remaining freq of the task back to the heapq
        # return time

        freq_map = Counter(tasks)
        max_heap = [-f for f in freq_map.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                curr = -heapq.heappop(max_heap)
                remaining = curr - 1
                if remaining > 0:
                    queue.append([remaining, time + n])

            if queue and time == queue[0][1]:
                rem_freq = -queue.popleft()[0]
                heapq.heappush(max_heap, rem_freq)

        return time

            
