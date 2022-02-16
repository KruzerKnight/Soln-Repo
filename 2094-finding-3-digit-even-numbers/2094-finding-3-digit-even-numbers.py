# We sort the digits list and form the greatest 3 digit number that can be made from the list and traverse from 100 to the number we formerd ( or ) 100 to 999.
# Each iteration, i is incremented by 2, since only even number is asked
# We convert the number into a string and store the digits as a ,band c respectively
# For each even number we first check whether their digits (i.e a ,band c ) are present in the digits list, if not next iteration continues
# To check if any repeated digits like 222 , 224, 886 etc.., we check a is equal to b or c or b == c, so if digits are repeated we check their count in digits, if the count in digits is equal or greater than that in i we append it to l
# If not digits are repeated append it to l

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        l=[]
        digits.sort()
        maxi=digits[-1]*100+digits[-2]*10+digits[-3]
        for i in range(100,maxi+1,2):
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
    
