# Write your MySQL query statement below
SELECT sell_date,COUNT(DISTINCT(PRODUCT)) AS num_sold, GROUP_CONCAT(DISTINCT PRODUCT ORDER BY PRODUCT SEPARATOR ',') AS products
FROM ACTIVITIES
GROUP BY SELL_DATE
ORDER BY SELL_DATE

