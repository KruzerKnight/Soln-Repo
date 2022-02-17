class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=list(map(str,title.split()))
        for i in range(len(l)):
            if(len(l[i])<3):
                l[i]=l[i].lower()
            else:
                l[i]=l[i].title()
            
        return ' '.join(l)