# Write your MySQL query statement below
select date_format(trans_date , '%Y-%m') as month , 
country , count(id) as trans_count , 
sum(case when state = 'approved' then 1 else 0 end) as approved_count , 
sum(amount) as trans_total_amount , 
sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by country , date_format(trans_date , '%Y-%m');


-- result = (transactions.withColumn("month" ,  (date_format(col("trans_date")) , 'yyyy-MM')
--             .groupBy(col("month") , col("country"))
--             .agg(
--                 count("*").alias("trans_count"),
--                 sum(when(state == 'approve' , 1).otherwise(0)).alias("approved_count"),
--                 sum(amount).alias("trans_total_amount")
--                 sum(when(state == 'approved' , amount).otherwise(0)).alias("approved_total_amount")
--             )
--             .select(
--                 col("month"),
--                 col("country"),
--                 col("trans_count"),
--                 col("approved_count"),
--                 col("trans_total_amount"),
--                 col("approved_total_amount")
--             )
-- )
