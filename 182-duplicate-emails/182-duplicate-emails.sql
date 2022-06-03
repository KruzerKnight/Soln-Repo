# Write your MySQL query statement below
SELECT EMAIL FROM PERSON
GROUP BY EMAIL HAVING COUNT(EMAIL)>1



 # SELECT DISTINCT a.Email
 # FROM Person a JOIN Person b
 # ON (a.Email = b.Email)
 # WHERE a.Id <> b.Id