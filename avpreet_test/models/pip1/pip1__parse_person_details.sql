{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH random_person_details AS (

  SELECT
    id,
    user_id,
    order_date,
    status,
    to_json(
      named_struct(
        'root', named_struct(
          'person', named_struct(
            'id',       id,
            'name',
              element_at(
                array(
                  named_struct('first','John','last','Doe'),
                  named_struct('first','Jane','last','Smith'),
                  named_struct('first','Alice','last','Johnson'),
                  named_struct('first','Bob','last','Brown'),
                  named_struct('first','Eva','last','Williams')
                ),
                cast(floor(rand() * 5) + 1 as int)
              ),
            'address',
              element_at(
                array(
                  named_struct('street','Main St','city','Springfield','zip',12345),
                  named_struct('street','Elm St','city','Rivertown','zip',54321),
                  named_struct('street','Oak St','city','Mapleton','zip',67890),
                  named_struct('street','Pine St','city','Laketown','zip',13579),
                  named_struct('street','Maple Ave','city','Hillview','zip',24680)
                ),
                cast(floor(rand() * 5) + 1 as int)
              )
          )
        )
      )
    ) AS person_details
  FROM (VALUES
    (1,  1,  '2018-01-01','returned'),
    (2,  3,  '2018-01-02','completed'),
    (3,  94, '2018-01-04','completed'),
    (4,  50, '2018-01-05','completed'),
    (5,  64, '2018-01-05','completed'),
    (6,  54, '2018-01-07','completed'),
    (7,  88, '2018-01-09','completed'),
    (8,  2,  '2018-01-11','returned'),
    (9,  53, '2018-01-12','completed'),
    (10, 7,  '2018-01-14','completed'),
    (11, 99, '2018-01-14','completed')
  ) AS t(id, user_id, order_date, status)

),

parse_person_details AS (

  {{
    DatabricksSqlBasics.JSONParse(
      'random_person_details', 
      'person_details', 
      'parseFromSampleRecord', 
      '{
        "root": {
          "person": {
            "id": 1,
            "name": {
              "first": "John",
              "last": "Doe"
            },
            "address": {
              "street": "Main St",
              "city": "Springfield",
              "zip": 12345
            }
          }
        }
      }', 
      ''
    )
  }}

)

SELECT *

FROM parse_person_details
