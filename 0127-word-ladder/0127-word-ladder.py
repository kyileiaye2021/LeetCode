class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # create variations for each word in the wordList
        #   add each variation with its word

        # queue
        # add the beginword to the queue with the len of 1
        # total len = 1

        # until queue is empty
        #   pop out the curr word and len 
        #   update the total len
        #   create variations for the curr word
        #   for each variation
        #       go to its related words 
        #           add them to the queue and len + 1
        # return total len

        wordList.append(beginWord)
        var_map = defaultdict(list)
        visited = set()

        for w in wordList:
            for i in range(len(w)):
                cur_var = w[:i] + '*' + w[i + 1 :]
                var_map[cur_var].append(w)

        # bfs
        queue = deque()
        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            curr_word, curr_len = queue.popleft()

            if curr_word == endWord:
                return curr_len

            for i in range(len(curr_word)):
                curr_var = curr_word[ : i] + '*' + curr_word[i + 1: ]
                
                for nei in var_map[curr_var]:
                    if nei not in visited:
                        queue.append((nei, curr_len + 1))
                        visited.add(nei)

        return 0
                



        