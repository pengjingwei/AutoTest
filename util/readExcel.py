import xlrd


class ReadExcel:
    def __init__(self):
        self.lt = []

    def read_execl(self, path='', sheetname='0'):
        wb = xlrd.open_workbook(filename=path, encoding_override=True)

        if sheetname.isdigit():
            sheet = wb.sheet_by_index(int(sheetname))
        else:
            sheet = wb.sheet_by_name(sheetname)

        rows = sheet.nrows
        for i in range(1, rows):
            self.lt.append(sheet.row_values(i))

        return self.lt


if __name__ == '__main__':
    data = ReadExcel().read_execl(path=r'C:\Users\gamer\Desktop\testDate.xlsx')
    print(*data)
