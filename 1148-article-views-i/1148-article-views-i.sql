# Write your MySQL query statement below
SELECT DISTINCT author_id AS ID FROM VIEWS
WHERE AUTHOR_ID=VIEWER_ID
ORDER BY AUTHOR_ID