from regression_abhisheks_e2etests_databricks_automationjobs_project_airflow_db_composer_automation.utils import *

def Email_1():
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_1",
        to = "abhisheks@prophecy.io",
        subject = "Test Subject",
        html_content = "Test Content",
        cc = "navneet@prophecy.io",
        bcc = "sony@prophecy.io",
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "email_default",
    )
