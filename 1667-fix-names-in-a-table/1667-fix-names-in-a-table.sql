# Write your MySQL query statement below
SELECT USER_ID,CONCAT(UCASE(SUBSTR(NAME,1,1)),LCASE(SUBSTR(NAME,2))) AS NAME
FROM USERS
ORDER BY USER_ID;