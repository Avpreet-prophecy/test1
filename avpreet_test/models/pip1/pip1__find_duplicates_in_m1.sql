{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH numeric_values_unknown_format AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

),

find_duplicates_in_m1 AS (

  {{
    DatabricksSqlBasics.FindDuplicates(
      'numeric_values_unknown_format', 
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
