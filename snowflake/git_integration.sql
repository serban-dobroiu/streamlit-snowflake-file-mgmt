-- Create an API integration https://docs.snowflake.com/en/sql-reference/sql/create-api-integration#for-git-repository
USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE API INTEGRATION github_api_integration
    API_PROVIDER = git_https_api
    API_ALLOWED_PREFIXES = ('https://github.com/serban-dobroiu')
    ENABLED = TRUE
    COMMENT = 'Test githib integration for entire github account';

USE DATABASE DEV_SOME_DB;

CREATE OR REPLACE GIT REPOSITORY streamlit_snowflake_file_mgmt
    API_INTEGRATION = github_api_integration
    ORIGIN = 'https://github.com/serban-dobroiu/streamlit-snowflake-file-mgmt.git';
