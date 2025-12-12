from snowflake.snowpark import Session
from snowflake.snowpark.exceptions import SnowparkSQLException
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

st_ss = st.session_state

def validate_stage_exists(session: Session, stage_name: str) -> dict:
    """
    """
    stage_valid: bool = False
    stage_exists: str = 'Stage does not exist or is inaccessible'
    error_msg: str = str()
    stage_info = {'stage_valid': stage_valid, 'stage_status': stage_exists, 'error_msg': error_msg}
    try:
        stage_desc = session.sql(f"DESCRIBE STAGE {stage_name}").collect()
        stage_info['stage_valid'] = True
        stage_info['stage_status'] = 'Stage exists and is accessible'
    except SnowparkSQLException as e:
        stage_info['error_msg'] = e.message
    finally:
        st_ss.stage_info = stage_info
        print(stage_info)
        return stage_info
    
def return_element_after_stage_validation(snowflake_session: Session, stage_name: str):
    """
    """
    session = snowflake_session
    stage_name = stage_name
    stage_info = validate_stage_exists(session=session, stage_name=stage_name)
    if stage_info['stage_valid']:
        valid_stage_container = st.container(key="valid_stage_container")
        with valid_stage_container:
            st.badge(stage_info['stage_status'], icon=":material/check:", color="green")
        return valid_stage_container
    else:
        invalid_stage_container = st.container(key="invalid_stage_container")
        with invalid_stage_container:
            st.badge(f"{stage_info['stage_status']}", icon=":material/error:", color="red")
            st.text(f"Complete error message: {stage_info['error_msg']}")