# Write your MySQL query statement below
SELECT USER_ID, MAX(TIME_STAMP) AS LAST_STAMP FROM LOGINS
WHERE (SELECT YEAR(A.TIME_STAMP) FROM LOGINS A WHERE LOGINS.TIME_STAMP=A.TIME_STAMP)='2020'
GROUP BY USER_ID

# SELECT
#     user_id,
#     MAX(time_stamp) AS last_stamp #obtaining latest login for all users
# FROM Logins
# WHERE YEAR(time_stamp) = 2020 #filtering for login dates with year 2020 in timestamp
# GROUP BY user_id;
