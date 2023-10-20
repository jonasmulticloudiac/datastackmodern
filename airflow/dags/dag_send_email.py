from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta


default_args = { 
    'depends_on_past' : False, 
    'start_date':datetime(2023,10,17),
    'email':['jonas.isaias@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)

}


dag = DAG('email_dag', description="Email DAG",
      default_args = default_args,
      schedule_interval=None, 
      catchup=False, default_view='graph', tags=['email','envio de emails'])


taks1 = BashOperator(task_id="tsk1",bash_command="sleep 1",dag=dag  )      
taks2 = BashOperator(task_id="tsk2",bash_command="sleep 1",dag=dag  )    
taks3 = BashOperator(task_id="tsk3",bash_command="sleep 1",dag=dag  )   
taks4 = BashOperator(task_id="tsk4",bash_command="exit  1",dag=dag  )      
taks5 = BashOperator(task_id="tsk5",bash_command="sleep 1",dag=dag, trigger_rule='none_failed' )    
taks6 = BashOperator(task_id="tsk6",bash_command="sleep 1",dag=dag, trigger_rule='none_failed' )    
     

send_email = EmailOperator(task_id="send_email", 
              to="jonasmulticloudiac@gmail.com",
              subject="Airflow Error",
              html_content="""
                              <h3> Erro na Dag</h3>
                              <p> Dag: send_email >/p>
                            """, 
              dag=dag, trigger_rule="one_failed" )


[taks1,taks2] >> taks3 >> taks4 
taks4 >> [taks5,taks6,send_email]
