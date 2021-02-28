from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_query="",
                 mode="append-only",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_query = sql_query
        self.mode = mode

    def execute(self, context):
		self.log.info("Connect to Redshift")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.mode == "delete-load":
			self.log.info("Start deleting data on Redshift")
            redshift.run("TRUNCATE {}".format(self.table))
		self.log.info("Run INSERT query to load data from S3 to Redshift")
        redshift.run("INSERT INTO {} {}".format(self.table, self.sql_query))
