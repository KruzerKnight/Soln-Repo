class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        l=[]
        for i in range(100,1000):
            if(i%2==0):
                s=str(i)
                a=int(s[0])
                b=int(s[1])
                c=int(s[2])
                if(a not in digits or b not in digits or c not in digits):
                    continue
                if(a==b or b==c or a==c):
                    if(a==b and b==c):
                        if(digits.count(a)>=3):
                            l.append(i)
                    elif(a==b):
                        if(digits.count(a)>=2):
                            l.append(i)
                    elif a==c:
                        if(digits.count(a)>=2):
                            l.append(i)
                    elif b==c:
                        if(digits.count(b)>=2):
                            l.append(i)
                else:
                    l.append(i)
        return l