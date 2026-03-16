class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # input: ["is", "is", "the", "the"], k = 2
        # output: is, the

        # input: ["i", "am", "sweet", "smart", "smart"], k = 1
        # output: smart

        # input: ["the", "joy", "u", "u", "the"], k = 1
        # output: the

        # freq of each word
        # sort the freq according to freq count
        # consider the str with the most k freq count
        # sort them in lexicographical order

        # max heap
        # str and freq count
        # add all pairs in a temp list
        # sort_by_freq = heapify the temp list according to the freq count 
        # sort_by_lexi = heapify the sort_by_freq according to lexicographical str
        # extract the first k ele from sort by lexi
        res = []
        freq_map = Counter(words)
        temp_list = [(-f, w) for w, f in freq_map.items()]
        print(temp_list)

        heapq.heapify(temp_list)
        for _ in range(k):
            freq, word = heapq.heappop(temp_list)
            res.append(word)
        return res
        