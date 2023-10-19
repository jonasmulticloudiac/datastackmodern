from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = { 
    'depends_on_past' : False, 
    'start_date':datetime(2023,10,17),
    'email':['teste@teste.com.br'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)

}


dag = DAG('defaults_dag', description="My default DAG",
      default_args = default_args,
      schedule_interval='@hourly',start_date=datetime(2023,10,17), 
      catchup=False, default_view='graph', tags=['processo','tag','pipeline'])


taks1 = BashOperator(task_id="tsk1",bash_command="sleep 5",dag=dag, retries=3 )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 5",dag=dag )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 5",dag=dag )        


taks1 >> taks2 >> taks3
