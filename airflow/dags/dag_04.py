from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with  DAG('four_dag', description="My four DAG",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False) as dag:


    taks1 = BashOperator(task_id="tsk1",bash_command="sleep 5" )      
    taks2 = BashOperator(task_id="tsk2",bash_command="sleep 5" )    
    taks3 = BashOperator(task_id="tsk3",bash_command="sleep 5" )        

    taks1.set_upstream(taks2)
    taks2.set_upstream(taks3)   