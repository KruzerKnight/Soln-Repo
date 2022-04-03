class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=[x[0] for x in matches]
        loss=[x[1] for x in matches]
        res=[sorted(list(set(win)-set(loss)))]
        l=Counter(loss)
        r=[]
        for i in l:
            if l[i]==1:
                r.append(i)
        res.append(sorted(r))
        return res