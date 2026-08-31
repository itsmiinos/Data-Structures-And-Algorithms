# Write your MySQL query statement below
select name as Customers from customers where id not in (select distinct customerId from orders);

-- # Pyspark : 
-- result = customers.join(orders , customers["id"] == orders["customerId"] , how="left_anti")
--             .select(customers["name"]).distinct()