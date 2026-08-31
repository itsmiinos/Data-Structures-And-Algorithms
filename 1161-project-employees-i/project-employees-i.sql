# Write your MySQL query statement below
select p.project_id , round(avg(e.experience_years), 2) as average_years from project as p inner join employee as e on p.employee_id = e.employee_id group by p.project_id;

-- # Pyspark :
-- result = (
--         project.join(employee , project["employee_id"]==employee["employee_id"] , how="inner")
--             .groupBy(project["project_id"])
--             .agg(
--                 round(avg(employee["experience_years"]),2).alias("average_years")
--             )
--             .select(
--                 project["project_id"],
--                 col("average_years")
--             )
-- )