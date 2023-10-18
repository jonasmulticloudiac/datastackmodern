from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('trigger_dag_3', description="trigger DAG",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)


taks1 = BashOperator(task_id="tsk1",bash_command="exit 1",dag=dag )      
taks2 = BashOperator(task_id="tsk2",bash_command="exit 1",dag=dag )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 5",dag=dag, 
                    trigger_rule='all_failed' )        


[taks1, taks2] >> taks3