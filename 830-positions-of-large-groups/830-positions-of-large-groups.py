class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        prev=s[0]
        count=0
        j=0
        l=[]
        for i in range(1,len(s)):
            if s[i]==prev:
                count+=1
            else:
                prev=s[i]
                if(count>=2):
                    l.append([j,i-1])
                j=i
                count=0
        if(count>=2):
                    l.append([j,i])
        return l
                
        
# alternative method
# return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]

# Explanation
# For every groups,
# find its start index i and end index j - 1.

# Group length is j - i,
# if it's no less than 3, add (i, j) to result.

# def largeGroupPositions(self, S):
#         i, j, N = 0, 0, len(S)
#         res = []
#         while i < N:
#             while j < N and S[j] == S[i]: j += 1
#             if j - i >= 3: res.append([i, j - 1])
#             i = j
#         return res
