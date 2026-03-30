{% snapshot test_modelAnother_final_Automationchetan_Databricks_jobs_model %}
{{
  config({    
    "alias": "test_Automationchetan_Databricks_jobs_model_1774862670471",
    "invalidate_hard_deletes": true,
    "strategy": "timestamp",
    "target_schema": "qa_upload_schema",
    "unique_key": "id",
    "updated_at": "updated_at"
  })
}}

WITH test_Automationchetan_Databricks_jobs_model AS (

  SELECT *
  
  FROM {{ ref('test_Automationchetan_Databricks_jobs_model')}}

)

{#Duplicates data from an existing automation model for further testing or analysis.#}
SELECT *

FROM test_Automationchetan_Databricks_jobs_model

{% endsnapshot %}
