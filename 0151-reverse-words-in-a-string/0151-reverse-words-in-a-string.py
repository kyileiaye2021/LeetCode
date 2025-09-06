class Solution:
    def reverseWords(self, s: str) -> str:
        # split the words into the ele in the list
        # in the list, reverse the ele with 2 pointers
        # combine them back to the str
        s = s.strip()
        temp_lst = s.split(" ")
        temp_lst2 = []
        i = 0
        j = len(temp_lst) - 1
        while i < j:
            temp_lst[i], temp_lst[j] = temp_lst[j], temp_lst[i]
            i += 1
            j -= 1
        
        for ele in temp_lst:
            if ele != "":
                temp_lst2.append(ele)
        print("temp_lst: ", temp_lst)
        print("temp_lst2: ", temp_lst2)
        new_str = " ".join(temp_lst2)
        return new_str
        