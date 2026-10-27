# Write your MySQL query statement below
with machine_start_time as (
select machine_id , activity_type , timestamp , lag(timestamp) over(partition by machine_id , process_id order by timestamp) as start_time from activity )
select machine_id , round(avg(timestamp - start_time),3) as processing_time from machine_start_time where activity_type = 'end' group by machine_id; 




-- window = Window.partitionBy(col("machine_id") , col("process_id")).orderBy(col("timestamp"))
-- result = (activity.withColumn("start_time" , lag(col("timestamp")).over(window))
--                 .filter(col("activity_type") == 'end')
--                 .groupBy(col("machine_id"))
--                 .agg(
--                     avg(col("timestamp") - col("start_time")).alias("processing_time")
--                 )
--                 .select(
--                     col("machine_id"),
--                     col("processing_time")
--                 )
-- )
