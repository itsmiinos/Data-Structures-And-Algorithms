# Write your MySQL query statement below
select v.customer_id , count(v.visit_id) as count_no_trans from visits as v left join transactions as t on v.visit_id = t.visit_id where t.transaction_id is null group by v.customer_id;


-- result = (visits.join(transactions , visits["visit_id"] == transactions["visit_id"] , how="left-anti")
--             .groupBy(visits["customer_id"])
--             .agg(
--                 count(visits["visits_id"]).alias("count_no_trans")
--             )
--             .select(
--                 visits["customer_id"],
--                 col("count_no_trans")
--             )
-- )