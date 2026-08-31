# Write your MySQL query statement below
with activity_with_lag as (
select machine_id , process_id , activity_type , timestamp , lag(timestamp) over(partition by machine_id , process_id order by timestamp) as start_row from activity
)

select machine_id , round(avg(case when activity_type = 'end' then (timestamp - start_row) end) , 3) as processing_time from activity_with_lag group by machine_id;