# Write your MySQL query statement below
SELECT ID FROM WEATHER A
WHERE A.TEMPERATURE>(SELECT B.TEMPERATURE FROM WEATHER B WHERE DATEDIFF(A.RECORDDATE,B.RECORDDATE)=1);