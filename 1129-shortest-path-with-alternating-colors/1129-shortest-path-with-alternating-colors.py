class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(lambda : defaultdict(set))
        red, blue = 0, 1
        for st, end in redEdges:
            graph[st][red].add(end)
        for st, end in blueEdges:
            graph[st][blue].add(end)
        res = [float('inf')] * n
        
        q = deque([(0,red), (0,blue)])
        level = -1
        while q:
            level += 1
            size = len(q)
            for i in range(size):
                node, color = q.popleft()
                opp_color = color^1
                res[node] = min(level, res[node])
                neighbors = graph[node][opp_color]
                for child in list(neighbors):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
        return [r if r != float('inf') else -1 for r in res]