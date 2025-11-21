from regression_abhisheks_e2etests_databricks_automationjobs_project_airflow_db_composer_automation.utils import *

def Slack_1():
    from airflow.providers.slack.operators.slack import SlackAPIPostOperator
    from datetime import timedelta

    return SlackAPIPostOperator(
        task_id = "Slack_1",
        text = "Test Automation Airflow",
        channel = "abhyslackpub",
        slack_conn_id = "slack_default",
    )
