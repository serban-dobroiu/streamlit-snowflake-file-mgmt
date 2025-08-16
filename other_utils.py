from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
from io import BytesIO

from snowflake_utils import get_table_columns

def create_excel_template(snowflake_session, table_name, worksheet_title: str):
    """
    Need to document this fully
    """
    wb = Workbook()

    ws = wb.active

    ws.title = worksheet_title
    headers = get_table_columns(snowflake_session=snowflake_session, table_name = table_name)
    dummy_data = [''] * len(headers)

    data = [headers, dummy_data]

    for row in data:
        ws.append(row)

    table = Table(displayName = "Account_Roster", ref="A1:" + get_column_letter(ws.max_column) + str(ws.max_row))

    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                        showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    table.tableStyleInfo = style

    ws.add_table(table)

    for cell in ws[1]:
        if cell.value == "DEPLOYMENT_DATE":
            comment = Comment(text="The accepted format is YYYY-MM-DD.\nIf not deployed use 9999-12-31.", author='')
            cell.comment = comment

    io = BytesIO()
    wb.save(io)

    return io

# wb = Workbook()

# ws = wb.active

# ws.title = "worksheet_title"

# test_list = [['A', 'B', 'C'], [1, 2, 3]]

# for row in test_list:
#     ws.append(row)

# table = Table(displayName = "Account_Roster", ref="A1:" + get_column_letter(ws.max_column) + str(ws.max_row))

# style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
#                        showLastColumn=False, showRowStripes=True, showColumnStripes=False)
# table.tableStyleInfo = style

# ws.add_table(table)

# wb.save('test.xlsx')