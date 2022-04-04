#User function Template for python3
import heapq

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
       jobs.sort(key=lambda x: x.profit , reverse=True)
       maxDeadline = -1
       for i in jobs:
           if i.deadline > maxDeadline:
               maxDeadline = i.deadline
               
       sequence = [-1]*maxDeadline
       count=0
       total_jobs=0
       total_profit=0
       
       while count<n:
           index=jobs[count].deadline -1
           
           while index>=0 and sequence[index] != -1:
                   index -= 1
           
           if index>=0:
               sequence[index] = jobs[count].id
               total_jobs += 1
               total_profit += jobs[count].profit
           
           count+=1
       
       return [total_jobs, total_profit]
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends