class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        subs=[]
        num_str=str(num)
        l=len(num_str)
        for i in range(l-k+1):
            subs.append(num_str[i:i+k])
        count=0
        # print(subs)
        for i in subs:
            if int(i)!=0 and num%int(i)==0:
                count+=1
        return count