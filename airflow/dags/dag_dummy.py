from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime



dag = DAG('dag_dummy', description="Dummy",
      schedule_interval=None,start_date=datetime(2023,10,17), 
      catchup=False)




taks1 = BashOperator(task_id="tsk1",bash_command="sleep 1",dag=dag  )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 1",dag=dag  )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 1",dag=dag )   
taks4 = BashOperator(task_id="tsk4",bash_command="sleep 1",dag=dag  )      
taks5 = BashOperator(task_id="tsk5",bash_command="sleep 1",dag=dag  )  
taksdummy = DummyOperator(task_id="tskdummy",dag=dag  )  




[taks1, taks2, taks3]  >> taksdummy >>  [taks4, taks5]
