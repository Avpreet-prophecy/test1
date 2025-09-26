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

)

SELECT *

FROM rides_with_fare
