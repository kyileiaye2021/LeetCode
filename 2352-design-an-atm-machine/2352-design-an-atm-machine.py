class ATM:
    # [20, 50, 100, 200, 500]
    # before
    # [0,0,1,2,1]
    # after
    # [0,0,0,2,0]

    # [0,1,0,3,1]
    # after
    # [0,1,0,3,1]

    # [0, 0, 0, 3, 0]
    # [550]

    # [0, 0, 0, 3, 1]
    # [510]
    # [-1]

    # hashmap to store the num of $

    def __init__(self):
        # create a hashmap
        # list of $
        self.dollars = [20, 50, 100, 200, 500]
        self.dollar_map = defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        # increment the count of each $ in the hashmap
        for i in range(len(banknotesCount)):
            self.dollar_map[self.dollars[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:

        # iterate thru the ele in the hashmap from the last
        #   divide the withdraw amount by the curr ele, get the min between curr count and the division and keep track of how much is used    #   update the curr amount 
        #   subtract the used amount from withdraw amount
        
        # if withdraw amount > 0
        #   return -1

        # iterate thru the ele in list and check in the hashmap
        #   add it to the res

        count = [0] * len(self.dollars)
        for i in range(len(self.dollars) - 1, -1, -1):

            d = self.dollars[i]
            used = min(amount // d, self.dollar_map[d])
            amount -= d * used
            count[i] += used

        if amount > 0:
            return [-1]

        for i in range(len(count)):
            self.dollar_map[self.dollars[i]] -= count[i]

        return count

        
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)