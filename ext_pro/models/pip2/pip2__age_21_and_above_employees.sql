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

),

employee_annual_salary AS (

  SELECT 
    ID,
    NAME,
    AGE,
    SALARY,
    CATEGORY,
    SALARY * 12 AS ANNUALSALARY
  
  FROM selected_employee_columns

),

age_21_and_above_employees AS (

  SELECT * 
  
  FROM employee_annual_salary
  
  WHERE AGE >= 21

)

SELECT *

FROM age_21_and_above_employees
