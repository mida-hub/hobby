from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
import pendulum

with DAG(
    'bq',
    default_args={'retries': 2},
    description='ETL DAG tutorial',
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=['example'],
) as dag:
    bq_op_1 = BigQueryExecuteQueryOperator(
        task_id='bq_op_1',
        gcp_conn_id='google_cloud_default',
        sql='select 1 as id',
        destination_dataset_table='lake.test',
        write_disposition='WRITE_TRUNCATE',
        allow_large_results=True,
        use_legacy_sql=False
    )
