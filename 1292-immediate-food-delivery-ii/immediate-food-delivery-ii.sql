# Write your MySQL query statement below
with orders as (
select delivery_id , customer_id , order_date , customer_pref_delivery_date , row_number() over(partition by customer_id order by order_date) as order_rank from delivery)

select round(sum(case when order_rank = 1 and order_date = customer_pref_delivery_date then 1 else 0 end) * 100.00 / sum(case when order_rank = 1 then 1 else 0 end) , 2) as immediate_percentage from orders;