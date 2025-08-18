from datetime import date, datetime
import decimal
from enum import Enum
from pydantic import BaseModel, Field, field_validator, ValidationInfo

class VettingOutcome(Enum):
    vetted_in = "Include"
    vetted_out = "Exclude"

class Removed(Enum):
    yes = "Yes"
    no = "No"

class RosterEntryUpload(BaseModel):
    """
    Validates a record submitted for upload
    """
    # TODO: if vetted = vetted_out deployment_date needs to be '9999-12-31'
    # TODO: consider if DEPLOYMENT_DATE should be date or string
    # ACCOUNT_ID: str = Field(min_length=10, max_length=10, pattern=r'^([\s\d]+)$')
    ACCOUNT_ID: str = Field(min_length=10, max_length=10, strict=False)
    PROGRAM_ID: str = Field(min_length=18, max_length=18)
    POTENTIAL: decimal.Decimal = Field(gt=0) 
    VETTED: VettingOutcome
    REMOVED: Removed
    DEPLOYMENT_DATE: date

    @field_validator("ACCOUNT_ID", mode="before")
    @classmethod
    def convert_to_str_and_check_digits_only(cls, v, info: ValidationInfo) -> str:
        """
        The ACCOUNT_ID should only contain digits
        """
        #TODO: this can probably be done in a smarter way, openpyxl reads this as int
        v_str = str()
        if not isinstance(v, str):
            v_str = str(v)
        else:
            v_str = v
        is_digits_only = v_str.isdigit()
        assert is_digits_only, f"{info.field_name} must contain digits only"
        return v_str

    # @field_validator("ACCOUNT_ID", mode="before")
    # @classmethod
    # def check_is_digits_only(cls, v: str, info: ValidationInfo) -> str:
    #     """
    #     The ACCOUNT_ID should only contain digits
    #     """
    #     if isinstance(str(v), str):
    #         is_digits_only = v.isdigit()
    #         assert is_digits_only, f"{info.field_name} must contain digits only"
    #     return v
    
    @field_validator("DEPLOYMENT_DATE", mode="before")
    @classmethod
    def deployment_date_must_make_sense(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_date = datetime.strptime(v, "%Y-%m-%d").date()
            assert is_date, f"{info.field_name} must be a valid ISO date format"
        return v
    
# data = {"ACCOUNT_ID": "1234567890"
#         , "PROGRAM_ID": "abcdefghi123456789"
#         , "POTENTIAL": 50
#         , "VETTED": "Include"
#         , "REMOVED": "Yes"
#         , "DEPLOYMENT_DATE": "2025-08-20"}

# input = RosterEntryUpload(**data)

# print(input)