class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # start from most freq num of tasks
        # keep track of start time with tasks
        # hashmap to keep track of freq
        # heap to keep track of tasks
        # another heap to keep track of remaining tasks

        freq = Counter(tasks)
        max_heap= []

        for t, f in freq.items():
            heapq.heappush(max_heap,-f)

        queue = deque() # to store the remaining items
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                remaining_task = -heapq.heappop(max_heap) - 1
                time_to_process = time + n
                if remaining_task > 0:
                    queue.append((time_to_process, remaining_task))

            if queue and queue[0][0] == time:
                time_to_process, task = queue.popleft()
                heapq.heappush(max_heap, -task)
        
        return time

        