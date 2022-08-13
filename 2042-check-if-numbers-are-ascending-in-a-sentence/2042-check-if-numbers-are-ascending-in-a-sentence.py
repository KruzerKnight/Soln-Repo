class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=s.split()
        a=[]
        for i in l:
            if i[0]<='9' and i[0]>='1':
                #print(i)
                a.append(int(i))
        #print(a)
        if len(a)==len(set(a)) and a==sorted(a):
            return True
        return False