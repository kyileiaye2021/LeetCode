class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
      
        # Happy cases
        # input: words = ["bella", "label", "roller"]
        # output: ["e", "l", "l"]

        # Edge cases
        # input: words = ["a"]
        # output: []
        # input: words = ["a", "b"]
        # output: []
        # input: words = ["a", "a"]
        # output: ["a"]

        # Hashmap
        # create a res list
        # create a comm hashmap for the 1st ele with Counter
        # iterate over the list from index 1
        #   create a hashmap for each curr ele
        #   iterate over the 1st ele hashmap 
        #       update curr ele with the min of the curr ele in the comm hashmap and that in the curr hashmap
        # iterate over the comm hashmap 
        #   append the curr key with its frequence in the res list
        
        res_lst = []
        comm_map = collections.Counter(words[0])

        for i in range(1, len(words)):
            curr_map = collections.Counter(words[i])

            for key in comm_map:
                comm_map[key] = min(curr_map[key], comm_map[key])

        for key, value in comm_map.items():
            for _ in range(value):
                res_lst.append(key)

        return res_lst
