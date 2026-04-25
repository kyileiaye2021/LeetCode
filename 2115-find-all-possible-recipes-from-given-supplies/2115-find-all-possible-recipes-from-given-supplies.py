class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # recipes = [bread, sandwish], ingredients = [[yeast, flour], [bread, meat]], supplies = [yeast, corn]
        # output: []

        # recipes = [bread, sandwish], ingredients = [[yeast, flour], [bread, meat]], supplies = [yeast, flour, corn]
        # output: [bread, sandwish]

        # iterate thru recipes
        #   check every ingredient of the curr recipes in supplies
        #       add curr recipes into res and add curr recipes into supplies
        # return res
        # res = []
        # supplies = set(supplies)
        # for r in range(len(recipes)):
        #     present = True
        #     for i in ingredients[r]:
        #         if i not in supplies:
        #             present = False

        #     if present:
        #         res.append(recipes[r])
        #         supplies.add(recipes[r])

        # return res
        # can_cook = {s:True for s in supplies} # items : T
        # recipes_index = {r: i for i, r in enumerate(recipes)}
        # def dfs(r):
        #     if r in can_cook:
        #         return can_cook[r]

        #     if r not in recipes_index: 
        #         return False

        #     can_cook[r] = False  # for circular

        #     for ingre in ingredients[recipes_index[r]]:
        #         if not dfs(ingre):
        #             return False

        #     can_cook[r] = True
        #     return can_cook[r]

        # res = []
        # for r in recipes:
        #     if dfs(r):
        #         res.append(r)

        # return res


        indeg = defaultdict(int) # item -> indegree for each item 
        graph = defaultdict(list) # ingredient -> recipes'
        res = []

        for i, r in enumerate(recipes):
            for ingre in ingredients[i]:
                graph[ingre].append(r)

            indeg[r] = len(ingredients[i])


        queue = deque(supplies)
        while queue:
            cur_item = queue.popleft()

            if cur_item in recipes:
                res.append(cur_item)

            for r in graph[cur_item]:
                indeg[r] -= 1

                if indeg[r] == 0:
                    queue.append(r)
        
        return res












