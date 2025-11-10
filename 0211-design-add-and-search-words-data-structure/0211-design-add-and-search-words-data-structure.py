class WordDictionary:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.leaf = False
        
    def letter_to_idx(self, letter: str):
        return ord(letter) - ord('a')
        
    def addWord(self, word: str) -> None:
        if word:
            first_letter = word[0]
            i = self.letter_to_idx(first_letter)
            if self.children[i] is None:
                self.children[i] = WordDictionary()
            self.children[i].addWord(word[1:])
        else:
            self.leaf = True
        
    def search(self, word: str) -> bool:
        if not word: return self.leaf
        first_letter = word[0]
        if first_letter == '.':
            return any(child is not None and child.search(word[1:]) for child in self.children)
        i = self.letter_to_idx(first_letter)
        return self.children[i] is not None and self.children[i].search(word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)