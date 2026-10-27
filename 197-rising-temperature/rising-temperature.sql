# Write your MySQL query statement below
with last_date_and_temperature as (
    select id , recordDate , temperature , lag(temperature) over(order by recordDate) as last_day_temperature , lag(recordDate) over(order by recordDate) as last_day_date from weather
)
select id from last_date_and_temperature where datediff(recordDate , last_day_date) = 1 and last_day_temperature < temperature;




-- window = Window.orderBy(col("recordDate"))
-- result = (weather.withColumn("previous_day_temp" , lag(col("temperature")).over(window))
--                 .withColumn("previous_day_date" , lag(col("recordDate")).over(window))
--                 .filter(
--                     (col("previous_day_temp") < col("temperature")) & 
--                     (datediff(col("recordDate") , col("previous_day_date")) == 1)
--                 )
--                 .select(
--                     col("id")
--                 )
-- )