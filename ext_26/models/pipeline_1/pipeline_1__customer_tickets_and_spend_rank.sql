{{
  config({    
    "materialized": "ephemeral",
    "database": "avpreet_random_prophecy_io_team",
    "schema": "main"
  })
}}

WITH rides AS (

  SELECT * 
  
  FROM {{ source('avpreet_random_prophecy_io_team.dummy', 'rides') }}

),

rides_with_fare AS (

  SELECT * 
  
  FROM rides
  
  WHERE NOT fare_amount IS NULL

),

support_tickets AS (

  SELECT * 
  
  FROM {{ source('avpreet_random_prophecy_io_team.dummy', 'support_tickets') }}

),

total_tickets_per_customer AS (

  SELECT 
    customer_id,
    COUNT(DISTINCT ticket_id) AS TOTAL_TICKETS
  
  FROM support_tickets
  
  GROUP BY customer_id

),

rides_daily_aggregation AS (

  SELECT 
    ride_date,
    COUNT(DISTINCT ride_id) AS TOTAL_RIDES,
    SUM(fare_amount) AS TOTAL_REVENUE,
    AVG(fare_amount) AS AVG_FARE,
    any_value(customer_id) AS customer_id
  
  FROM rides_with_fare
  
  GROUP BY ride_date

),

rides_aggregation_ordered AS (

  SELECT * 
  
  FROM rides_daily_aggregation
  
  ORDER BY ride_date ASC

),

customer_total_revenue AS (

  SELECT 
    customer_id,
    SUM(TOTAL_REVENUE) AS TOTAL_REVENUE
  
  FROM rides_aggregation_ordered
  
  GROUP BY customer_id

),

customer_spend_rank AS (

  SELECT 
    customer_id AS CUSTOMER_ID,
    TOTAL_REVENUE,
    RANK() OVER (ORDER BY TOTAL_REVENUE DESC) AS SPEND_RANK
  
  FROM customer_total_revenue

),

customer_tickets_and_spend_rank AS (

  SELECT 
    customer_spend_rank.CUSTOMER_ID,
    customer_spend_rank.TOTAL_REVENUE,
    customer_spend_rank.SPEND_RANK,
    total_tickets_per_customer.TOTAL_TICKETS
  
  FROM customer_spend_rank
  INNER JOIN total_tickets_per_customer
     ON customer_spend_rank.CUSTOMER_ID = total_tickets_per_customer.customer_id

)

SELECT *

FROM customer_tickets_and_spend_rank
