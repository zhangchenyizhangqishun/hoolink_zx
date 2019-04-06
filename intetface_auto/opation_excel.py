# -*- coding:utf-8 -*-


import xlrd
from excel_data import ExcelData


class OpationExcel:
    def __init__(self):
        self.read_exc = self.readExcel()
        self.excel_data = ExcelData()

    '''
    读取Excel的数据
    '''
    def readExcel(self):
        file_path = '/Users/zhangxiao/hoolink_python/hoolink_zx/intetface_auto/auto_data.xls'
        tables = xlrd.open_workbook(file_path)
        exc_data = tables.sheet_by_index(0)
        return exc_data

    '''
    获取总行数
    '''
    def get_row(self):
        row_count = self.read_exc.row_values
        print row_count

    '''
    获取到Excel中case_id的值
    '''
    def get_exc_case_id(self,row):
        col = int(self.excel_data.exc_case_id())
        case_id_value = self.read_exc.cell_value(row,col)
        return case_id_value

    '''
    获取到Excel中case_name的值
    '''
    def get_exc_case_name(self, row):
        col = int(self.excel_data.exc_case_name())
        print col
        case_name_value = self.read_exc.cell_value(row, col)
        print case_name_value
        return case_name_value



if __name__ == '__main__':
    oe = OpationExcel()
    oe.get_exc_case_name(1)