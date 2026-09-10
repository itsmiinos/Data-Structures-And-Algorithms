# Write your MySQL query statement below
with last_day_temp as (
    select id , recordDate , temperature , lag(temperature) over(order by recordDate) as last_temp , lag(recordDate) over(order by recordDate) as last_date from weather
)
select id from last_day_temp where last_temp is not null and last_temp < temperature and datediff(recordDate , last_date) = 1;

-- window = Window.orderBy(col("recordDate"))
-- result = (weather.withColumn("last_day_temp" , lag(col("temperature")).over(window))
--             .filter(col("last_day_temp") < col("temperature"))
--             .select(col("id"))
-- )