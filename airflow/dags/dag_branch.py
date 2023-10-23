from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime
import random 

dag = DAG('dag_branch', description="Banch Test",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)

def gera_numero_aleatorio():
    return random.randint(1,100)

gera_numero_aleatorio_task = PythonOperator(
    task_id='gera_numero_aleatorio_task', 
    python_callable = gera_numero_aleatorio, dag=dag)


def avalia_numero_aleatorio(**context):
    number = context['task_instance'].xcom_pull(task_ids='gera_numero_aleatorio_task')
    if number % 2 == 0:
        return 'par_task'
    else: 
        return 'impar_task'


branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=avalia_numero_aleatorio,
    provide_context=True,
    dag=dag
)




par_task = BashOperator(task_id="par_task",bash_command='echo "numero PAR"',dag=dag )      
impar_task = BashOperator(task_id="impar_task",bash_command='echo "numero IMPARAR"',dag=dag )    

gera_numero_aleatorio_task >> branch_task
branch_task >> par_task
branch_task >> impar_task


  



