WITH s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

),

SQLStatement_1 AS (

  {{
    DatabricksSqlBasics.FindDuplicates(
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

FROM SQLStatement_1
