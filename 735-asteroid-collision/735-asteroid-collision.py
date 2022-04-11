class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                while stack and stack[-1]<-1*i and stack[-1]>0:
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(i)
                elif i==-1*stack[-1]:
                    stack.pop()
        return stack