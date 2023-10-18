from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

dag = DAG('trigger_dag_taskgroup', description="trigger DAG",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)


taks1 = BashOperator(task_id="tsk1",bash_command="sleep 5",dag=dag  )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 5",dag=dag  )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 5",dag=dag )   
taks4 = BashOperator(task_id="tsk4",bash_command="sleep 5",dag=dag  )      
taks5 = BashOperator(task_id="tsk5",bash_command="sleep 5",dag=dag  )    
taks6 = BashOperator(task_id="tsk6",bash_command="sleep 5",dag=dag )    
tsk_group = TaskGroup("tsk_group", dag=dag)
taks7 = BashOperator(task_id="tsk7",bash_command="sleep 5",dag=dag,task_group=tsk_group )    
taks8 = BashOperator(task_id="tsk8",bash_command="sleep 5",dag=dag,task_group=tsk_group)        
taks9 = BashOperator(task_id="tsk9",bash_command="sleep 5",dag=dag, 
                     trigger_rule='one_failed',task_group=tsk_group )    


taks1 >> taks2
taks3 >> taks4
[taks2, taks4] >> taks5 >> taks6
taks6 >> tsk_group