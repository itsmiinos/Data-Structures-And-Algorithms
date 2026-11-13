# Write your MySQL query statement below
with ranking_per_department as (
select d.name as Department , e.name as Employee , e.salary as Salary , dense_rank() over (partition by d.id order by e.salary desc) as dr from department as d inner join employee as e on d.id = e.departmentid )

select Department , Employee , Salary from ranking_per_department where dr = 1;