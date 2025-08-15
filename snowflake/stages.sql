SELECT CURRENT_USER();

USE DATABASE DEV_SOME_DB;

CREATE SCHEMA BMT;

-- create an internal stage to load input files for specific BMT
USE SCHEMA BMT;

CREATE FILE FORMAT IF NOT EXISTS ff_pipe_separated
    TYPE = CSV
    FIELD_DELIMITER = '|'
    EMPTY_FIELD_AS_NULL = TRUE
    PARSE_HEADER = TRUE
    COMMENT = 'Generic pipe separated files';

CREATE STAGE IF NOT EXISTS DEV_SOME_DB.BMT.stage_account_roster
    ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
    FILE_FORMAT = ff_pipe_separated
    COMMENT = 'stage for account roster converted input files';