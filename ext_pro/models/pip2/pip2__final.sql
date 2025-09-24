{{
  config({    
    "materialized": "ephemeral",
    "database": "avpreet_random_prophecy_io_team",
    "schema": "schema"
  })
}}

WITH uber_raw_data AS (

  SELECT * 
  
  FROM {{ source('avpreet_random_prophecy_io_team.dummy', 'uber_data') }}

),

uber_data AS (

  SELECT 
    "Date",
    "Time",
    "Booking ID",
    "Booking Status",
    "Customer ID",
    "Vehicle Type",
    "Pickup Location",
    "Drop Location",
    "Avg VTAT",
    "Avg CTAT",
    "Cancelled Rides by Customer",
    "Reason for cancelling by Customer",
    "Cancelled Rides by Driver",
    "Driver Cancellation Reason",
    "Incomplete Rides",
    "Incomplete Rides Reason",
    "Booking Value",
    "Ride Distance",
    "Driver Ratings",
    "Customer Rating",
    "Payment Method"
  
  FROM uber_raw_data

),

valid_uber_bookings AS (

  SELECT * 
  
  FROM uber_data
  
  WHERE NOT "Booking ID" IS NULL

),

uber_data_clean AS (

  SELECT 
    "Date",
    "Time",
    "Booking ID",
    "Booking Status",
    "Customer ID",
    "Vehicle Type",
    "Pickup Location",
    "Drop Location",
    "Avg VTAT",
    "Avg CTAT",
    "Cancelled Rides by Customer",
    "Reason for cancelling by Customer",
    "Cancelled Rides by Driver",
    "Driver Cancellation Reason",
    "Incomplete Rides",
    "Incomplete Rides Reason",
    "Booking Value",
    "Ride Distance",
    "Driver Ratings",
    "Customer Rating",
    "Payment Method"
  
  FROM valid_uber_bookings

),

vehicle_type_agg AS (

  SELECT 
    "Vehicle Type" AS vehicle_type,
    COUNT(*) AS total_bookings,
    SUM(CASE
      WHEN "Booking Status" = 'Completed'
        THEN 1
      ELSE 0
    END) AS completed_rides,
    SUM(CASE
      WHEN "Booking Status" = 'Cancelled by Customer'
        THEN 1
      ELSE 0
    END) AS cancelled_by_customer,
    SUM(CASE
      WHEN "Booking Status" = 'Cancelled by Driver'
        THEN 1
      ELSE 0
    END) AS cancelled_by_driver,
    SUM(CASE
      WHEN "Booking Status" = 'Incomplete'
        THEN 1
      ELSE 0
    END) AS incomplete_rides
  
  FROM uber_data_clean
  
  GROUP BY "Vehicle Type"

),

vehicle_type_completion AS (

  SELECT 
    vehicle_type,
    total_bookings,
    completed_rides,
    cancelled_by_customer,
    cancelled_by_driver,
    incomplete_rides,
    CAST(completed_rides AS DOUBLE) / NULLIF(total_bookings, 0) AS completion_rate
  
  FROM vehicle_type_agg

),

completion_rate_ranking AS (

  SELECT * 
  
  FROM vehicle_type_completion
  
  ORDER BY completion_rate ASC

),

final AS (

  SELECT 
    vehicle_type,
    total_bookings,
    completed_rides,
    cancelled_by_customer,
    cancelled_by_driver,
    incomplete_rides,
    completion_rate
  
  FROM completion_rate_ranking

)

SELECT *

FROM final
