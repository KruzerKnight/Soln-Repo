class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        gcd, r = max(x, y), min(x, y)
        while r: gcd, r = r, gcd % r
        return z == 0 or x + y >= z and z % gcd == 0