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
        can_cook = {s:True for s in supplies} # items : T
        recipes_index = {r: i for i, r in enumerate(recipes)}
        def dfs(r):
            if r in can_cook:
                return can_cook[r]

            if r not in recipes_index:
                return False

            can_cook[r] = False

            for ingre in ingredients[recipes_index[r]]:
                if not dfs(ingre):
                    return False

            can_cook[r] = True
            return can_cook[r]

        res = []
        for r in recipes:
            if dfs(r):
                res.append(r)

        return res




