class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        u=0
        l=0
        s=0
        n=0
        sc='!@#$%^&*()-+'
        if len(password)<8:
            return False
        for i in range(len(password)):
            #print(i,password[i],u,l,s,n)
            if i>0 and password[i]==password[i-1]:
                return False
            if password[i].isupper():
                u=1
            elif password[i].islower():
                l=1
            elif password[i].isdigit():
                n=1
            if password[i] in sc:
                s=1
        if (u and l and s and n):
                return True