# Write your MySQL query statement below
with rolling_sum as (
    select person_name , weight , sum(weight) over(order by turn rows between unbounded preceding and current row) as rolling_weight from queue
)
select person_name from rolling_sum where rolling_weight <= 1000 order by rolling_weight desc limit 1;