{{
  config({    
    "materialized": "ephemeral",
    "database": "avpreet_random_prophecy_io_team",
    "schema": "main"
  })
}}

WITH support_tickets AS (

  SELECT * 
  
  FROM {{ source('avpreet_random_prophecy_io_team.dummy', 'support_tickets') }}

),

total_tickets_per_customer AS (

  SELECT 
    customer_id,
    COUNT(DISTINCT ticket_id) AS TOTAL_TICKETS
  
  FROM support_tickets
  
  GROUP BY customer_id

)

SELECT *

FROM total_tickets_per_customer
