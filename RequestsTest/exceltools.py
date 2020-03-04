"""
    python读写excel
"""
import xlrd


def read_excel(excel_path, sheet_name, skip_first=True):
    """
        名字：读取excel方法
        参数：
            - excel_path：excel的绝对路径
            - sheet_name：表格的名字
            - skip_first: 是否跳过首页：默认为是/False跳过
    """
    result = []
    datas = xlrd.open_workbook(excel_path) # 打开工作bu
    table = datas.sheet_by_name("Sheet1") # 打开工作bu的表格
    if skip_first == True:    # 判断是否跳过首页
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行数据
    for row in range(start_row, table.nrows):
        result.append(table.row_values(row))

    return result


# p = "C:\\Users\\SNake\\Desktop\\测试用例.xlsx"
# s = "Sheet1"
# res = read_excel(p, s)
# for r in res:
#     print(r)