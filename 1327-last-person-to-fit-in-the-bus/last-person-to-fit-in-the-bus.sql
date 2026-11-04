# Write your MySQL query statement below
with person_with_rolling_weight as (
select person_name , sum(weight) over(order by turn rows between unbounded preceding and current row) as rolling_weight from queue )
select person_name from person_with_rolling_weight where rolling_weight <= 1000 order by rolling_weight desc limit 1;



-- window = Window.orderBy(col("turn")).rowsBetween(Window.unboundedPreceding , Window.currentRow)
-- result = queue.withColumn("rolling_weight" , sum(col("weight")).over(window))
--             .filter(col("rolling_weight") <= 1000)
--             .orderBy(desc("rolling_weight"))
--             .select(col("person_name")).limit(1)