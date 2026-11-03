# Write your MySQL query statement below
with customers_with_products as (
select distinct c.customer_id , c.product_key from customer as c inner join product as p on c.product_key = p.product_key )
select customer_id from customers_with_products group by customer_id having count(product_key) = (select count(*) from product);