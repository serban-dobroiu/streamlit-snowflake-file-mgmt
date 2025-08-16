CREATE TABLE IF NOT EXISTS DEV_SOME_DB.BMT.STG_ACCOUNT_ROSTER (
    ACCOUNT_ID VARCHAR(10) NOT NULL COMMENT 'account identifier' 
    , PROGRAM_ID VARCHAR(18) NOT NULL COMMENT 'program identifier'
    , POTENTIAL NUMBER(9,2) COMMENT 'dollar potential'
    , VETTED VARCHAR(20) NOT NULL COMMENT 'account and program vetting status'
    , REMOVED BOOLEAN NOT NULL COMMENT 'logical delete'
    , DEPLOYMENT_DATE TIMESTAMP_NTZ(3) NOT NULL /*DEFAULT '999-12-31 23:59:59.999'::timestamp_ntz(3)*/ COMMENT 'date of account and program deployment'
    , LOAD_TS TIMESTAMP_NTZ(3) DEFAULT SYSDATE()::TIMESTAMP_NTZ(3) COMMENT 'load timestamp'
);

CREATE TABLE IF NOT EXISTS DEV_SOME_DB.BMT.ACCOUNT_ROSTER (
    ACCOUNT_ID VARCHAR(10) NOT NULL COMMENT 'account identifier' 
    , PROGRAM_ID VARCHAR(18) NOT NULL COMMENT 'program identifier'
    , POTENTIAL NUMBER(9,2) COMMENT 'dollar potential'
    , VETTED VARCHAR(20) NOT NULL COMMENT 'account and program vetting status'
    , REMOVED BOOLEAN COMMENT 'logical delete'
    , DEPLOYMENT_DATE TIMESTAMP_NTZ(3) NOT NULL /*DEFAULT '999-12-31 23:59:59.999'::timestamp_ntz(3)*/ COMMENT 'date of account and program deployment'
    , VALID_FROM TIMESTAMP_NTZ(3) COMMENT 'record validity start'
    , VALID_TO TIMESTAMP_NTZ(3) COMMENT 'record validity end'
    , STAGING_LOAD_TS TIMESTAMP_NTZ(3) COMMENT 'record staging timestamp'
    , LOAD_TS TIMESTAMP_NTZ(3) DEFAULT SYSDATE()::TIMESTAMP_NTZ(3) COMMENT 'load timestamp'
);

