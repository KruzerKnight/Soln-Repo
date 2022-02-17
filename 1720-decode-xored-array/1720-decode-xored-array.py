# Since that encoded[i] = arr[i] XOR arr[i+1], then arr[i+1] = encoded[i] XOR arr[i].

class Solution:
    def decode(self, encoded: List[int], r: int) -> List[int]:
        l=[r]
        for i in encoded:
            r=r^i
            l.append(r)
        return l