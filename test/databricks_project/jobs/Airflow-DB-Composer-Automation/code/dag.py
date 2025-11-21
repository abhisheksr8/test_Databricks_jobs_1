import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from regression_abhisheks_e2etests_databricks_automationjobs_project_airflow_db_composer_automation.tasks import (
    Email_1,
    HTTPSensor_1,
    Model_0,
    Model_1,
    S3FileSensor_1,
    Slack_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "regression_abhisheks_e2etests_Databricks_AutomationJobs_Project_Airflow_DB_Composer_Automation", 
    schedule_interval = "0 0 17 2 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_0_op = Model_0()
    HTTPSensor_1_op = HTTPSensor_1()
    S3FileSensor_1_op = S3FileSensor_1()
    Email_1_op = Email_1()
    Slack_1_op = Slack_1()
    Model_1_op = Model_1()
    Model_0_op >> [Email_1_op, HTTPSensor_1_op, Model_1_op, S3FileSensor_1_op, Slack_1_op]
