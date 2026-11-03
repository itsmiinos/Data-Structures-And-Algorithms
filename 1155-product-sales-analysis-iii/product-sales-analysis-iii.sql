# Write your MySQL query statement below
with product_and_first_year as (
select product_id , min(year) as fr from sales group by product_id )
select p.product_id , p.fr as first_year , s.quantity , s.price from product_and_first_year as p inner join sales as s on p.product_id = s.product_id and p.fr = s.year;