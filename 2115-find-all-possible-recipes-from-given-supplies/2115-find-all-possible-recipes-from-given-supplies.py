class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        indegree=defaultdict(int)
        graph=defaultdict(list)
        
        for rec,ing in zip(recipes,ingredients):
            indegree[rec]=len(ing)
            for i in ing:
                graph[i].append(rec)
                
        result=[]
        q=deque(supplies)
        recipes=set(recipes)

        while q:
            item=q.popleft()
            if item in recipes:
                result.append(item)
            for rec in graph[item]:
                indegree[rec]-=1
                if indegree[rec]==0:
                    q.append(rec)
        return result