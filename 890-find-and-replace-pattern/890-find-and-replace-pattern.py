class Solution:
    def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if F(w) == F(p)]