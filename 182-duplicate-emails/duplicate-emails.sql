# Write your MySQL query statement below
select email from person group by email having count(email) > 1 ;

-- result = (person.groupBy(col("email"))
--             .agg(
--                 count(col("email")).alias("countEmail")
--             )
--             .filter(col("countEmail") > 1)
--             .select(col("email")) 
-- )