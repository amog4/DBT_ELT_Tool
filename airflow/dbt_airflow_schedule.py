from airflow import DAG, macros

from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
from airflow.operators.dummy_operator import DummyOperator

import yaml
from airflow.utils.dates import days_ago
from datetime import timedelta
import json



args = {
    'owner': 's',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'retries': 1,
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retry_delay': timedelta(minutes=3)
}
	

with open('config_esop_dbt.yml','rb') as f:
    doc = yaml.load(f,Loader=yaml.FullLoader)

for ke , v in doc.items():
    k = ke
    val = v
    


json_manifest_file = 'manifest.json'



def model_flow(ancestor_value):
    if ancestor_value.split('.')[0] == 'model':
        return ancestor_value.split('.')[-1]

def get_structure():
    with open(json_manifest_file, 'r') as json_data:
        data = json.load(json_data)
        ancestors_data = data['parent_map']
        tree = {}
        for node in ancestors_data:
            ancestor =  list(set(ancestors_data[node]))
            anestor_2 = [ model_flow(ancestor_value = ancestor_value )  for ancestor_value in ancestor ]
            clean_node_name = model_flow(ancestor_value = node)
            if clean_node_name is not None:
                tree[clean_node_name ] =  anestor_2

        return tree





dag = DAG(dag_id='practice_contact_trans_dag_scheduler',default_args=args,schedule_interval='@daily',dagrun_timeout=timedelta(minutes=10))


dummy_start = DummyOperator(task_id='start',dag=dag)
dummy_end = DummyOperator(task_id='end',dag=dag)




nodes = get_structure()

operator = {}
for node in nodes:

    dbt_run = DbtRunOperator( task_id='dbt_run_{}'.format(node),dir=val['dir'],dag=dag,profiles_dir=val['profiles_dir'],target=val['target'],models= '{}'.format(node) )

    operator[node] = dbt_run



for node in nodes:
    for parent in nodes[node]:
        if parent != None:
            dummy_start >> operator[parent] >> operator[node] >> dummy_end
        else:
            dummy_start >> operator[node] >> dummy_end


