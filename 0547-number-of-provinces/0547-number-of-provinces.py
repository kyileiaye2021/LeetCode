class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # adj_lst = defaultdict(set) # {nodes -> connected nodes}
        visited = set()

        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected)):
        #         if i != j:
        #             adj_lst[i].add(j)
        #             adj_lst[j].add(i)

        count = 0
        queue = deque()
        for i in range(len(isConnected)):
            if i not in visited:
                queue.append(i)

                while queue:
                    cur_node = queue.popleft()
                    visited.add(cur_node)

                    for j in range(len(isConnected[cur_node])):
                        if j != cur_node and j not in visited and isConnected[cur_node][j] == 1:
                            queue.append(j)
                            visited.add(j)
                
                count += 1

        return count 
