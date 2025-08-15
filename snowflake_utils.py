from snowflake.snowpark import Session
import snowflake.snowpark.exceptions as sf_exceptions
from snowflake.snowpark.dataframe import DataFrame

def get_table_columns(snowflake_session: Session, table_name: str) -> list[str]:
    session = snowflake_session
    table_name=table_name
    columns: list[str] = list()
    try:
        # df = session.sql(f"""SELECT * FROM {table_name} WHERE 1 = 0""").collect()
        columns = session.table(f"{table_name}").columns#.collect()
        
    except sf_exceptions as e:
        pass
    finally:
        return columns