# Write your MySQL query statement below
select activity_date as day , count(distinct user_id) as active_users from activity where activity_date between '2019-06-28' AND '2019-07-27' group by activity_date;

#Pyspark :
-- result = (
--     activity
--         .filter(
--             (col("activity_date") >= "2019-06-28") &
--             (col("activity_date") <= "2019-07-27")
--         )
--         .groupBy(
--             col("activity_date")
--         )
--         .agg(
--             countDistinct(col("user_id")).alias("active_users")
--         )
--         .select(
--             col("activity_date").alias("day"),
--             col("active_users")
--         )
-- )