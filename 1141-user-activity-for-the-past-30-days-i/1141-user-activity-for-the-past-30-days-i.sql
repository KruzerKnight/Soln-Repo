select activity_date as day, count(distinct user_id) as active_users 
from Activity
where datediff('2019-07-27', activity_date) <30 AND ACTIVITY_DATE<'2019-08-20'
group by activity_date


#DONT KNOW WHY BUT JUST THE TEST CASES WONT ACCEPT IF THE SECOND CONDITION ISN'T MENTIONED