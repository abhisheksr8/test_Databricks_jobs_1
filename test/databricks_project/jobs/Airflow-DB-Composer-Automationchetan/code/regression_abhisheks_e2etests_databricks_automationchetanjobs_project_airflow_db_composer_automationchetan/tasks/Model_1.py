from regression_abhisheks_e2etests_databricks_automationchetanjobs_project_airflow_db_composer_automationchetan.utils import *

def Model_1():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_1",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": True,
          "run_seeds": True,
          "run_parents": True,
          "run_children": True,
          "run_tests": True,
          "run_mode": "model",
          "entity_kind": "snapshot",
          "entity_name": "test_modelAnother_final_Automationchetan_Databricks_jobs_model",
          "project_id": "55124",
          "git_entity": "branch",
          "git_entity_value": "testBranchDatabricksJobs",
          "git_ssh_url": "https://github.com/abhisheksr8/test_Databricks_jobs_1.git",
          "git_sub_path": "test/databricks_project",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile",
          "envs": {
            "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
            "DBT_PROFILES_DIR": "/home/airflow/gcs/data", 
            "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
            "DBT_FULL_REFRESH": "true"
          },
          "project_config": None
        },
        retries = 1, 
        max_retry_delay = timedelta(minutes = 1.0)
    )
