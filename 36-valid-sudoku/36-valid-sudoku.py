class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxs = defaultdict(set)
        for i in range(9):
            for j in range(9):
                d=board[i][j]
                if(d=='.'):
                    continue
                if(d in cols[j] or d in rows[i] or d in boxs[(i//3,j//3)]):
                        return False
                cols[j].add(d)
                rows[i].add(d)
                boxs[(i//3,j//3)].add(d)
                
        return True