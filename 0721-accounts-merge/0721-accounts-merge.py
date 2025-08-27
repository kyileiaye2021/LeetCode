class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))
    
    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # hashmap {account_name: {emails}}
        # first we have to find the same email
        # to be the same account person, at least one of the emails has to be the same

        # {email: account index}
        # if email already exist, we can union two indices
        uf = UnionFind(len(accounts))
        emailtoAcc = {}
        for i, account in enumerate(accounts):
            email = account[1:]
            for e in email:
                if e not in emailtoAcc:
                    emailtoAcc[e] = i
                else:
                    uf.unite(i, emailtoAcc[e])
        
        print(emailtoAcc)

        # accountToEmail {index : [emails]}
        accountToEmail = defaultdict(list)
        res = []
        for email, acc_id in emailtoAcc.items():
            leader = uf.find(acc_id)
            accountToEmail[leader].append(email)

        for i, e in accountToEmail.items():
            name = accounts[i][0]
            emails = sorted(e)
            res.append([name] + emails) 

        return res
            
