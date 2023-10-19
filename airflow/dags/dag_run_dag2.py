from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

dag = DAG('dagrundag2', description="trigger DAG",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)


taks1 = BashOperator(task_id="tsk1",bash_command="sleep 5",dag=dag  )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 5",dag=dag  )    


taks1 >> taks2
