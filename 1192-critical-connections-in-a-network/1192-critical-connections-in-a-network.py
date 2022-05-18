class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Time complexity: O(V + E) because we only visit each node (and therefore, each edge) once.
        # m is an adjacency list for the graph
        m = [set() for _ in range(n)]
        for i, j in connections:
            m[i].add(j)
            m[j].add(i)
            
        # s will keep track of the connections that are still potentially critical
        # we'll remove elements from this set as we get more information about the graph,
        # and whatever's left after we're done is what's critical.
        s = set(tuple(el) for el in connections)
        # seen tells us the position of the node in the current path of nodes
        # we've visited in O(1) time. a stack isn't necessary, but this basically simulates one
        # so for a path 0 -> 2 -> 1, seen = {0: 0, 2: 1, 1: 2}
        seen = {}
        # settled is a hash set of nodes we've already seen, and therefore no longer need to visit
        settled = set()
        
        # our depth-first-search function returns a number. This number represents how far back
        # we've found a cycle after traversing the edge from "last" to "i." It's infinity if 
        # there is no cycle at all.
        def dfs(i = 0, last = None):
            if i in seen:
                # if i is in the hash map representing our state, "seen," then we've found a cycle.
                # how big the cycle is depends on how far back this element is; that's why we need
                # "seen" to be a hash map and not a hash set. If i is at position x for some path
                # of nodes of length N where x < N, then we need to mark *at least* the last (N - x - 1) 
                # edges in this cycle as non-critical, because we don't need them to keep the graph connected.
                return seen[i]
            elif i in settled:
                # we don't need to visit a node twice because we already know we've handled its cycles.
                # so, if we revisit one, just treat this node as if it doesn't have any cycles
                return float('inf')
            else:
                # i is a new node, so add it to our path of nodes of length N at position N; 
                seen[i] = len(seen)
                # now our path of nodes is length N + 1

                # we want to learn two things using the information we get from each neighbor:
                # 1. how many of this node's edges are non-critical and need to be removed?
                # 2. how *far back* do we have to go in this node's path before we find
                #    edges that may be critical?
                ret = float('inf')
                for j in m[i]:
                    # don't revisit the last node
                    if j != last:
                        res = dfs(j, i)
                        # its possible that whatever non-critical node this neighbor's logic identified
                        # isn't actually in the path anymore. if so, treat it like it's float('inf')
                        if res < len(seen):
                            # we're going to return "ret" in the end to tell our previous nodes in the
                            # path which edges are not critical. if we find more than one cycle, we want
                            # to tell the previous nodes about the cycle that connects to the earliest 
                            # possible node in the path, so take the min.
                            # for example, consider the path 0 -> 1 -> 2 -> 3
                            # if 3 is connected to both 0 and 2, which one's position do we want to return
                            # from this function? the answer is 0's position, because if 3 -> 0, then
                            # all of the edges in this path after 0 are non-critical. if 3 -> 0, then
                            # it doesn't matter if 3 is connected to 1 or 2 directly or indirectly,
                            # so return the earliest one
                            ret = min(ret, res)
                            
                            # remove the node from our critical set
                            for t in ((i, j), (j, i)):
                                if t in s:
                                    s.remove(t)
                                    
                del seen[i]
                
                settled.add(i)
                return ret
                
        dfs()
        return list(list(el) for el in s)