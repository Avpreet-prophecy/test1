WITH customers AS (

  SELECT * 
  
  FROM {{ source('qa_team.avpreettables', 'customers') }}

),

s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

),

duplicate_finder AS (

  {{
    prophecy_basics.FindDuplicates(
      's1', 
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

FROM customers
