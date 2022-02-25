class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split('.')))
        v2=list(map(int,version2.split('.')))
        n=min(len(v1),len(v2))
        for i in range(n):
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
        if(len(v1)>len(v2)):
            for i in range(n,len(v1)):
                if v1[i]!=0:
                    return 1
        if(len(v2)>len(v1)):
            for i in range(n,len(v2)):
                if v2[i]!=0:
                    return -1
        return 0