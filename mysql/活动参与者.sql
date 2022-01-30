'''mysql 建表：with tmp as'''
with tmp as
(select activity,count(*) as cnt
from Friends group by activity)
select activity from tmp where cnt < (select max(cnt) from tmp)
and cnt > (select min(cnt) from tmp)




select activity as ACTIVITY
from friends
group by activity
having count(*)> any(
    select count(*) from friends group by activity
) and count(*)<any(
    select count(*) from friends group by activity
)


