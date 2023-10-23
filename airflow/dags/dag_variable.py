from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime

dag = DAG('dag_variaveis', description="Variaveis",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)

def print_variable(**context): 
    VAR_ID= Variable.get('GLOBAL_VAR_ID')
    print(f'----> O valor da variavel GLOBAL_VAR_ID :--->  {VAR_ID} ')

taks1 = PythonOperator(task_id="tsk1",python_callable=print_variable,dag=dag )     


taks1 
