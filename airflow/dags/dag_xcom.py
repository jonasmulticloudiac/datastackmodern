from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

dag = DAG('dag_xcom', description="Xcom",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)


def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valorxcom1',value=10200)

taks1 = PythonOperator(task_id="tsk1",python_callable=task_write,dag=dag )     

def task_read(**kwarg): 
     valor = kwarg['ti'].xcom_pull(key='valorxcom1')
     print(f"Valor Recuperado : {valor}")

taks2 = PythonOperator(task_id="tsk2",python_callable=task_read,dag=dag )  


taks1 >> taks2
