# Write your MySQL query statement below
select query_name , round(avg(rating / position) , 2) as quality , 
coalesce(round((sum(case when rating < 3 then 1 end) * 100.00 / count(query_name)) , 2), 0) as poor_query_percentage from queries group by query_name;

# Pyspark :
-- result = (queries.groupBy(col("query_name"))
--             .agg(
--                 round(avg(col("rating") / col("position")),2).alias("quality"),
--                 coalesce(round(sum(when(col("rating") < 3 , 1)) * 100.00 / count("query_name"), 2) , 0).alias("poor_query_percentage")
--             )
--             .select(
--                 col("query_name"),
--                 col("quality"),
--                 col("poor_query_percentage")
--             )

-- )