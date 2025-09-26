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

)

SELECT *

FROM rides_aggregation_ordered
