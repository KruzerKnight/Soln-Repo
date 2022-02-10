class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[]
        for i in range(1,n+1):
            r3=i%3
            r5=i%5
            if(r3==0 and r5==0):
                l.append("FizzBuzz")
            elif(r3==0):
                l.append("Fizz")
            elif(r5==0):
                l.append("Buzz")
            else:
                l.append(str(i))
        return l