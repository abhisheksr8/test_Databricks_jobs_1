{{
  config({    
    "materialized": "table",
    "full_refresh": true
  })
}}

WITH qa_test_seed_job_Databricks AS (

  SELECT * 
  
  FROM {{ ref('qa_test_seed_job_Databricks')}}

)

SELECT *

FROM qa_test_seed_job_Databricks
