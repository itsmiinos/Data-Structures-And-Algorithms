with lag_values as (

SELECT
    id,
    num,
    LAG(num, 1) OVER (ORDER BY id) AS prev_1,
    LAG(num, 2) OVER (ORDER BY id) AS prev_2
FROM Logs )

select distinct num as ConsecutiveNums from lag_values where num = prev_1 and num = prev_2;