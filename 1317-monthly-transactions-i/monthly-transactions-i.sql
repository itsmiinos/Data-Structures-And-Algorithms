# Write your MySQL query statement below
select date_format(trans_date , '%Y-%m') as month , 
country , count(id) as trans_count , 
sum(case when state = 'approved' then 1 else 0 end) as approved_count , 
sum(amount) as trans_total_amount , 
sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by country , date_format(trans_date , '%Y-%m');

# Pyspark : 
-- result = (transactions
--         .groupBy(date_format(col("trans_date") , 'yyyy-MM') , col("country"))
--         .agg(
--             count(col("id")).alias("trans_count"),
--             sum(when(col("state") == "approved" , 1).otherwise(0)).alias("approved_count"),
--             sum(col("amount")).alias("trans_total_amount"),
--             sum(when(col("state") == "approved" , col("amount")).otherwise(0)).alias("approved_total_amount")
--         )

-- )