import paramiko
import os
import requests
deployment_url = os.environ["airflow_url"]
dag_id = "supply-automation_Testtest"
response = requests.post(
    url=f"{deployment_url}/api/v1/dags/{dag_id}/dagRuns",
    auth=(os.environ['airflow_username'], os.environ['airflow_password']),
    verify=False,
    json={
        "conf": {},
    }
)
print(response)