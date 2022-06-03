SELECT max(Salary) AS SECONDHIGHESTSALARY
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)

# Using max() will return a NULL if the value doesn't exist. So there is no need to UNION a NULL. Of course, if the second highest value is guaranteed to exist, using LIMIT 1,1 will be the best answer.