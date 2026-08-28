# Write your MySQL query statement below
select email from person group by email having count(email) > 1;

#Pyspark : 
-- result = (person.groupBy(col("email"))
--         .agg(count(col("email")) > 1)
--         .select(col("email"))
-- )