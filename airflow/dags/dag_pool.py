from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('dag_pool', description="Pool",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)

taks1 = BashOperator(task_id="tsk1",bash_command="sleep 5",dag=dag, pool="NewPool" )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 5",dag=dag, pool="NewPool",priority_weight=5 )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 5",dag=dag, pool="NewPool" )   
taks4 = BashOperator(task_id="tsk4",bash_command="sleep 5",dag=dag, pool="NewPool",priority_weight=10 )      
  



