class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Can there be like that there is no common str in the words? No
        # Can the words list be empty or null? no
        # Can there be repetitive word in the str?
        # Can there be repetitive char in each str?
        
        # High Level Plan
        # * Iterative Approach
        #   * iterate over the list. in each iteration, iterate again to check the 
        #       curr ele with other ele in the list
        # * Dictionary Approach
        
        # Low Level Plan
        # * create a frequency map for the first word using Counter()
        # * iterate over the lst
        #   * create the curr frequency map for the curr word using Counter()
        #   * compare the curr frequency map with the min frequency map
        # * iterate over the min frequency
        #   * iterate the amount of value of each key
        
        min_common = Counter(words[0])
        
        for word in words:
            curr_cnt = Counter(word)
            for c in min_common:
                min_common[c] = min(min_common[c], curr_cnt[c])
                
        common_list = []    
        for key in min_common:
            for i in range(min_common[key]):
                common_list.append(key)
        return common_list
                
                