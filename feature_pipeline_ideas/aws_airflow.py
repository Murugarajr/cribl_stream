from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.lambda_function import LambdaHook
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from datetime import datetime

default_args = {
        'owner': 'Raj',
        'depends_on_past': False,
        'start_date': datetime(2022, 10, 13),
        'email': ['rmurugaraj@outlook.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
}


def lambda_aws(ds, **kwargs):
    hook = LambdaHook('criblTask', region_name='', log_type='None', qualifier='$LATEST',
                      invocation_type='RequestResponse', config=None, aws_conn_id='my_lambda')
    response_aws = hook.invoke_lambda(payload='null')
    print(f"Response:{response_aws}")


with DAG('invocation_hook_lambda', default_args=default_args,
         description='invoke a lambda in dev aws instance') as dag:
    start = EmptyOperator(task_id='Begin_execution')

    run_lambda = PythonOperator(
        task_id="invoke_lambda_fn",
        python_callable=lambda_aws,
        provide_context=True
    )

    transfer_s3_to_redshift = S3ToRedshiftOperator(
        task_id='transfer_s3_to_redshift',
        redshift_conn_id='conn_id_name',
        s3_bucket='bucket_name',
        s3_key='S3_KEY_2',
        schema='PUBLIC',
        table='REDSHIFT_TABLE',
    )

    end = EmptyOperator(task_id='stop_execution')

start >> run_lambda >> transfer_s3_to_redshift >> end
