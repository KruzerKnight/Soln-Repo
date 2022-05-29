# Write your MySQL query statement below
UPDATE SALARY
SET SEX=( 
    CASE 
        WHEN SEX='F'
        THEN 'm'
        ELSE 'f'
    END
);