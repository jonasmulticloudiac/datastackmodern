from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('trigger_dag_encadeada', description="trigger DAG",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)


taks1 = BashOperator(task_id="tsk1",bash_command="sleep 5",dag=dag  )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 5",dag=dag  )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 5",dag=dag )   
taks4 = BashOperator(task_id="tsk4",bash_command="sleep 5",dag=dag  )      
taks5 = BashOperator(task_id="tsk5",bash_command="sleep 5",dag=dag  )    
taks6 = BashOperator(task_id="tsk6",bash_command="sleep 5",dag=dag )        
taks7 = BashOperator(task_id="tsk7",bash_command="sleep 5",dag=dag  )    
taks8 = BashOperator(task_id="tsk8",bash_command="sleep 5",dag=dag )        
taks9 = BashOperator(task_id="tsk9",bash_command="sleep 5",dag=dag, 
                     trigger_rule='one_failed' )    


taks1 >> taks2
taks3 >> taks4
[taks2, taks4] >> taks5 >> taks6
taks6 >> [taks7, taks8, taks9] 