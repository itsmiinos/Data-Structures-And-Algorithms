# Write your MySQL query statement below
select actor_id , director_id from actordirector group by actor_id , director_id having count(*) >= 3;

# Pyspark :
-- result = (actordirector.groupBy(col("actor_id") , col("director_id"))
--             .agg(col("*").alias("count_rows"))
--             .where(col("count_rows"))
--             .select(col("actor_id") , col("director_id"))
-- )