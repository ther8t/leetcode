import collections


class Solution:

    # 17%
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] += 1

        recipesWhichCanBeMade = []
        queue = collections.deque()

        for i in supplies:
            queue.append(i)
            indegree[i] = 0

        while queue:
            popped = queue.popleft()
            if popped in recipes:
                recipesWhichCanBeMade.append(popped)

            for child in graph[popped]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return recipesWhichCanBeMade

    # # 5%
    # def findAllRecipes(self, recipes, ingredients, supplies):
    #     graphMap = {}
    #
    #     for i in range(len(recipes)):
    #             graphMap[recipes[i]] = 0
    #
    #     for i in range(len(ingredients)):
    #         for j in range(len(ingredients[i])):
    #             graphMap[ingredients[i][j]] = 0
    #
    #     for i in supplies:
    #         graphMap[i] = 1
    #
    #     changeCount = 1
    #
    #     recipesWhichCanBeMade = []
    #
    #     while changeCount > 0:
    #         changeCount = 0
    #         for i in range(len(recipes)):
    #             if graphMap[recipes[i]] == 1:
    #                 continue
    #             canBeMade = True
    #             for j in range(len(ingredients[i])):
    #                 if graphMap[ingredients[i][j]] == 0:
    #                     canBeMade = False
    #                     break
    #             if canBeMade:
    #                 graphMap[recipes[i]] = 1
    #                 recipesWhichCanBeMade.append(recipes[i])
    #                 changeCount += 1
    #     return recipesWhichCanBeMade


if __name__ == '__main__':
    # print(Solution().findAllRecipes(recipes=["bread", "sandwich"], ingredients=[["sandwich"], ["bread"]],
    #                                 supplies=["bread"]))
    print(Solution().findAllRecipes(recipes = ["bread","sandwich", "x"], ingredients = [["yeast","flour", "x"],["bread","meat"],["sandwich"]], supplies = ["yeast","flour","meat"]))
