from regression_abhisheks_e2etests_databricks_automationchetanjobs_project_airflow_db_composer_automationchetan.utils import *

def HTTPSensor_1():
    from airflow.providers.http.sensors.http import HttpSensor
    from datetime import timedelta

    # Execution timeout is airflow task level execution timeout
    # Sensor timeout will be different. Should be handled separately
    return HttpSensor(
        task_id = "HTTPSensor_1",
        endpoint = "/webhp",
        request_params = None,
        headers = None,
        response_check = None,
        http_conn_id = "http_default",
        poke_interval = 60,
        timeout = 600,
    )
