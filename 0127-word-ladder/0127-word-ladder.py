class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # adj list {variation:  word}
        # add beginWord to wordList
        # iterate thru wordList
        #   iterate thru c and make variations
        #   map variated word to cur word
        if endWord not in wordList:
            return 0
        variations = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                cur_variation = w[:i] + '*' + w[i + 1:]
                variations[cur_variation].append(w)
        # bfs
        # count = 0
        # visited = set()
        # start beginWord into the queue
        #   pop the cur word 
        #   if cur word == endWord
        #       return count 
        #   for c in cur word
        #   make variation s for each c
        #   for each mapped word for each variation
        #       if mapped word is not visited
        #           add them to queue
        #   increment count
        # return count

        queue = deque()
        visited = set()
        count = 1
        queue.append(beginWord)
        visited.add(beginWord)

        while queue:
            queue_len = len(queue)

            for _ in range(queue_len):
                cur_word = queue.popleft()
                if cur_word == endWord:
                    return count

                # finding variations for the cur word
                for i in range(len(cur_word)):
                    cur_variation = cur_word[:i] + '*' + cur_word[i+1:]
                    for nei in variations[cur_variation]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            count += 1
        return 0

