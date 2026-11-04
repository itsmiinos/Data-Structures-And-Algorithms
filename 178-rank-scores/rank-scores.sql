# Write your MySQL query statement below
select score , dense_rank() over(order by score desc) as 'rank' from scores;


-- window = Window.orderBy(desc(col("score")))
-- windowTwo = Window.orderBy(desc(col("score"))).rowsBetween(Window.unboundedPreceding , Window.currentRow)
-- result = (scores.withColumn("last_score" , lag(col("score")).over(window))
--             .withColumn("rank_addition" , when((col("last_score").isNull()) | (col("last_score")!=col("score")) , 1).otherwise(0))
--             .withColumn("rank" , sum(col("rank_addition")).over(windowTwo))
--             .select(col("score") , col("rank")))