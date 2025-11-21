from regression_abhisheks_e2etests_databricks_automationjobs_project_airflow_db_composer_automation.utils import *

def S3FileSensor_1():
    from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
    from datetime import timedelta

    return S3KeySensor(
        task_id = "S3FileSensor_1",
        bucket_key = [s.strip() for s in "test/validation_data/test_source.json".split(",") if s.strip()],
        bucket_name = "qa-prophecy",
        check_fn = None,
        aws_conn_id = "aws_s3_default",
        wildcard_match = False,
        verify = False,
        timeout = 600,
    )
