{{
  config({    
    "materialized": "ephemeral",
    "database": "avpreet_random_prophecy_io_team",
    "schema": "schema"
  })
}}

WITH xlxs_file AS (

  SELECT * 
  
  FROM {{ source('avpreet_random_prophecy_io_team.dummy', 'xlxs_file') }}

),

selected_employee_columns AS (

  SELECT 
    ID,
    Name AS NAME,
    Age AS AGE,
    Salary AS SALARY,
    Category AS CATEGORY
  
  FROM xlxs_file

)

SELECT *

FROM selected_employee_columns
