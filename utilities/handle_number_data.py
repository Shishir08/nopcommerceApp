from numbers_parser import Document

doc=Document("/Users/shishirjoshi/PycharmProjects/PythonProject/nopcommerceApp/TestData/shishir.numbers")
sheet=doc.sheets[1]
table=sheet.tables[0]


count=0

def is_row_empty(row):
    for cell in row:
        cell_value=cell.formatted_value in [None,""]
        return cell_value

    return None

def get_row_count():

    for row in table.rows():
        global count
        if is_row_empty(row):
            continue
        count+=1
        # for cell in row:
        #     # print(cell.formatted_value,end="    ")

    return count



def get_cell_value(row_no):
    username = table.rows()[row_no][0].formatted_value
    password = table.rows()[row_no][1].formatted_value
    exp=table.rows()[row_no][2].formatted_value
    return username, password,exp

# def get_compare(row_no,key_number_sheet):
#     print(table.rows()[row_no][5].formatted_value)
#     print(key_number_sheet)
#     if float(table.rows()[row_no][5].formatted_value)== key_number_sheet:
#         return 'Pass'
#     else:
#         return 'fail'








