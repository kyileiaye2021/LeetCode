class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # create a first hashmap for the first str
        # iterate over the ele in the lst
        #   create a new hashmap for curr str
        #   create a common hashmap
        #   check if the eles in the new hashmap is in first hashmap
        #       add them to common hashmap
        #       update first to common hashmap
        # iterate over the common hashmap
        #   append the ele in the list

        map = Counter(words[0])

        for w in words:
            curr_map = Counter(w)
            
            for key in map:

                map[key] = min(curr_map[key], map[key])

        res = []
        for key, value in map.items():
            while value > 0:
                res.append(key)
                value -= 1

        return res


                    