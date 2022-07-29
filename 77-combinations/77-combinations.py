class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        @cache
        def getCombos(a: int, b: int) -> List[List[int]]:
            if b == 1:
                # base case
                return [[i] for i in range(a, n + 1)]
            res = []
            for i in range(a, n + 1):
                for combo in getCombos(i + 1, b - 1):
                    n_combo = [i]
                    n_combo.extend(combo)
                    res.append(n_combo)
            return res
        return getCombos(1, k)