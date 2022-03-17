# def ordinalOfDate(self, date):
#         Y, M, D = map(int, date.split('-'))
#         return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)


class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d=map(int,date.split('-'))
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400==0 or (y%100!=0 and y%4==0):
            months[1]=29
        return sum(months[:m-1])+d