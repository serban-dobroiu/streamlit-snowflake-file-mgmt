from io import BytesIO
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
    

def load_to_stage(session: Session, stage_name: str, file: BytesIO):
    msg = "Could not load file to stage."
    try:
        session.file.put_stream(file, f"{stage_name}/{file.name}", auto_compress=True, overwrite=False)
        msg = f"File was successfully loaded to stage {stage_name}/{file.name}"
    except sf_exceptions as e:
        str(e)
        msg += str(e)
    finally:
        return msg