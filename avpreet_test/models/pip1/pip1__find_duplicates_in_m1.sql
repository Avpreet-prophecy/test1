{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH dummy AS (

  SELECT * 
  
  FROM {{ ref('dummy')}}

),

find_duplicates_in_m1 AS (

  {{
    DatabricksSqlBasics.FindDuplicates(
      'dummy', 
      [], 
      '', 
      'unique', 
      '', 
      '', 
      '', 
      'allCols', 
      ['a', 'b', 'c'], 
      []
    )
  }}

)

SELECT *

FROM find_duplicates_in_m1
