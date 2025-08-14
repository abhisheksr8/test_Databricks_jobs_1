{% snapshot test_modelAnother_final_Automation_Databricks_jobs_model %}
{{
  config({    
    "alias": "test_Automation_Databricks_jobs_model_1755166275464",
    "invalidate_hard_deletes": true,
    "strategy": "timestamp",
    "target_schema": "qa_upload_schema",
    "unique_key": "id",
    "updated_at": "updated_at"
  })
}}

WITH test_Automation_Databricks_jobs_model AS (

  SELECT *
  
  FROM {{ ref('test_Automation_Databricks_jobs_model')}}

)

SELECT *

FROM test_Automation_Databricks_jobs_model

{% endsnapshot %}
