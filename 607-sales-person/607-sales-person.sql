# Write your MySQL query statement below
SELECT SALESPERSON.NAME 
FROM ORDERS O JOIN COMPANY C ON (C.COM_ID=O.COM_ID AND C.NAME='RED')
RIGHT JOIN SALESPERSON ON SALESPERSON.SALES_ID = O.SALES_ID
WHERE O.SALES_ID IS NULL;


# The first inner join creates a view for just 'RED' orders
# The right join ensures all salespersons are included (even those who do not have RED orders)
# The WHERE IS NULL gives salespersons who did not have any RED orders due to the right join