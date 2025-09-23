{{
  config({    
    "materialized": "ephemeral",
    "database": "avpreet_random_prophecy_io_team",
    "schema": "schema"
  })
}}

WITH crocs AS (

  SELECT * 
  
  FROM {{ source('avpreet_random_prophecy_io_team.dummy', 'crocs') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM crocs AS in0

)

SELECT *

FROM Reformat_1
