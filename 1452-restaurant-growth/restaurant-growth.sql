# Write your MySQL query statement below
with daily as (
    select visited_on , sum(amount) as daily_amount from customer group by visited_on
),
rolling as (
    select visited_on , sum(daily_amount) over (order by visited_on rows between 6 preceding and current row) as amount from daily
)
select visited_on , amount , round(amount / 7 , 2) as average_amount from rolling where visited_on >= date_add((select min(visited_on) from customer) , interval 6 day) order by visited_on;