class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        vis=[0]*n
        
        q=[]
        q.append(0)
        vis[0]=1
        
        while q:
            node=q.pop()
            for i in rooms[node]:
                if not vis[i]:
                    vis[i]=1
                    q.append(i)
        
        for i in vis:
            if not i:
                return False
        return True