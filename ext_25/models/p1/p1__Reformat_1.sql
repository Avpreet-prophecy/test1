{{
  config({    
    "materialized": "ephemeral",
    "database": "avpreet_random_prophecy_io_team",
    "schema": "main"
  })
}}

WITH all_type_databricks_0 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('p1', 'all_type_databricks_0') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM all_type_databricks_0 AS in0

)

SELECT *

FROM Reformat_1
