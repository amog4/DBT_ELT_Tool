from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
import logging



args = {
    'owner': 's',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 17),
    'retries': 1,
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retry_delay': timedelta(minutes=3)
}

dag = DAG(dag_id='docu_contact_trans_dag1',default_args=args,schedule_interval='@daily',dagrun_timeout=timedelta(minutes=10))

dummy_start = DummyOperator(task_id='start',dag=dag)
dummy_end = DummyOperator(task_id='end',dag=dag)


#default_args = {dbt_dir = "/usr/local/airflow/dags/projects/DBT_ELT_Tool"}


dbt_run = DbtRunOperator(
    task_id='dbt_run',dir="/home/amogh/PycharmProjects/DBT_ELT_Tool/dbt_tool_practice/",dag=dag
)
#command_ = "/usr/local/airflow/dags/projects/DBT_ELT_Tool && dbt run --help"
#bashoperator_task = BashOperator(task_id='docu_transform',dag=dag,bash_command=command_)

dummy_start >> dbt_run >> dummy_end
