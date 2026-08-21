# Write your MySQL query statement below
select contest_id , round(count(user_id) * 100 / (select count(user_id) from users) , 2) as percentage from register group by contest_id order by percentage desc , contest_id asc;

# PySpark :
-- total_user_count = users.count()
-- result = register.groupBy(col("contest_id"))\
--                 .agg(
--                     round(
--                         count(col("user_id")) * 100.00 / total_user_count
--                     ,2)\
--                 .alias("percentage"))\
--                 .orderBy(desc(col("percentage")) , asc(col("contest_id")))