from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session
from other_utils import create_excel_template
from utils import return_element_after_stage_validation

import streamlit as st

# session = get_active_session()

session = Session.builder.config("connection_name", "IGUTYDJ-NJ39709_serban1").create()

# session.use_database('DEV_SOME_DB')
# session.use_schema('BMT')

st.title(body="An app to manage dreaded BMTs")

st.sidebar.text("Things to do")

data=[{"Make": "International Harvester" 
       , "Model": "Scout"
       , "Year": 1979
       , "First Registration": '1979-06-15'
       , "Purchase Date": '2025-01-01'
       , "Known for": "First SUV in history"}]

bmt_options = ["Account Roster", "CSV BMT"]

ss = st.session_state

selected_bmt = st.segmented_control(label="Which BMT would you like to manage?", options=bmt_options, selection_mode="single", width=1000, key="selected_bmt")

if selected_bmt:

    # st.text(validate_stage_exists(session=session, stage_name='DEV_SOME_DB.BMT.STAGE_ACCOUNT_ROSTER1'))
    return_element_after_stage_validation(snowflake_session=session, stage_name='DEV_SOME_DB.BMT.STAGE_ACCOUNT_ROSTER')

    if ss.stage_info['stage_valid']:
        # st.balloons()

        tab1, tab2, tab3, tab4 = st.tabs(["Upload", "Download a template", "View existing data", "View Stage Contents"])
        # st.write(selected_bmt)
        # print(f"Selected BMT from session state is : {ss.selected_bmt}")

        if ss.selected_bmt == "CSV BMT":
            container = st.container(border=True)

            with container:
                with tab1:
                    separator_container = st.container(border=True)
                    default_separator_value: str = ","
                    separator_value: str = default_separator_value
                    with separator_container:
                        custom_separator_toggle = st.toggle(label="I am using a custom **single char** separator", help="It is assumed that the separator in a comma. Toggle this to enter a different one.")
                        if custom_separator_toggle:
                            custom_separator_value = st.text_input(label="Custom separator", max_chars=1, placeholder="enter separator", width=200)
                            if len(custom_separator_value) == 1:
                                print(f"after toggle custom separator is: {custom_separator_value}")
                                separator_value = custom_separator_value
                                print(f"separator is: {separator_value}")
                                
                        file_types = ["csv", "xlsx"] # remove CSV 
                        uploaded_file = st.file_uploader(label="Choose file", type=file_types, accept_multiple_files=False, width=400)
                        # if uploaded_file_meta not in st.session_state:
                        #     st.session_state.uploaded_file_meta = 
                        if uploaded_file:
                            print(f"Uploaded file id id: {uploaded_file.file_id}")
                            print(f"File type is: {uploaded_file.type}")

        if ss.selected_bmt == "Account Roster":
            container = st.container(border=True)

            with container:
                with tab1:                                
                        file_types = ["xlsx"] # remove CSV 
                        uploaded_file = st.file_uploader(label="Choose file", type=file_types, accept_multiple_files=False, width=400)
                        # if uploaded_file_meta not in st.session_state:
                        #     st.session_state.uploaded_file_meta = 
                        if uploaded_file:
                            print(f"Uploaded file id id: {uploaded_file.file_id}")
                            print(f"File type is: {uploaded_file.type}")

                with tab2:
                    template_file = create_excel_template(snowflake_session=session, table_name="DEV_SOME_DB.BMT.STG_ACCOUNT_ROSTER", worksheet_title="Account_Roster")
                    st.download_button(label="Download a template", data=template_file, file_name="Account Roster.xlsx", on_click='ignore', type="secondary", icon=":material/download:")

                with tab3:
                    st.dataframe(data=data)


# st.write(ss.selected_bmt)