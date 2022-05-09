class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        arr=[d[i] for i in digits]
        arr=product(*arr)
        r=[]
        for i in arr:
            if i:
                r.append(''.join(i))
        return r