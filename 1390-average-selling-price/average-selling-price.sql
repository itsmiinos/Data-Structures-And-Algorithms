# Write your MySQL query statement below
SELECT
    p.product_id,
    COALESCE(
        ROUND(SUM(p.price * u.units) / SUM(u.units), 2),
        0
    ) AS average_price
FROM prices AS p
LEFT JOIN unitssold AS u
    ON p.product_id = u.product_id
    AND u.purchase_date >= p.start_date
    AND u.purchase_date <= p.end_date
GROUP BY p.product_id;

-- result = (prices.join(unitssold , prices["product_id"] == unitssold["product_id"] & prices["start_date"] <= unitssold["purchase_date"] & prices["end_date"] >= unitssold["purchase_date"] , how = "left")
--             .groupBy(prices["product_id"])
--             .agg(
--                 coalesce(round(avg(sum(prices["price"] * unitssold["units"])
--         / sum(unitssold["units"]),2),0).alias("average_price")
--             )
--             .select(
--                 prices["product_id"],
--                 col("average_price")
--             )
-- )