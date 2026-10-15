# Write your MySQL query statement below
with earning as (
    select stock_name , case when operation = 'Buy' then -price when operation = 'Sell' then price end as profit , operation , operation_day from stocks
)

select stock_name , sum(profit) as capital_gain_loss from earning group by stock_name;





-- window = Window.partitionBy(col("stock_name")).orderBy(col("operation_day"))
-- result = (stocks.withColumn("buying_price" ,  
--                 lag(col("price")).over(window))
--                 .filter(col("operation") == 'Sell')
--                 .groupBy(col("stock_name"))
--                 .agg(
--                     sum(col("price") - col("buying_price")).alias("capital_gain_loss")
--                 )
--                 .select(
--                     col("stock_name"),
--                     col("capital_gain_loss")
--                 )
-- )