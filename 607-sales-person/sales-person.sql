# Write your MySQL query statement below
with sales_id_with_red_company as (
    select sales_id from orders where com_id in (select com_id from company where name = 'RED')
)
select name as name from salesperson where sales_id not in (select sales_id from sales_id_with_red_company);


-- red_company = company.filter(col("com_name") == 'RED').select(col("com_id"))
-- sales_id_with_red_company = orders.join(red_company , orders["com_id"] == red_company["com_id"] , how = "inner").select(col("sales_id"))
-- result = salesperson.join(sales_id_with_red_company , on="sales_id" , how ="left anti").select(col("name"))