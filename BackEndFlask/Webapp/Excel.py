import xlrd
from Webapp.models import Patients
from flask_login import current_user
from Webapp import db
class Excelentry:
    WorkBook = xlrd.open_workbook('.\\Excel\\Excel.xlsx')
    Sheet = WorkBook.sheet_by_index(0)
    limitRows = Sheet.nrows
    resultRecord = Patients()
    def addRecord(self, ExcelPath):
        for i in range(1, self.limitRows):
            self.resultRecord.name = self.Sheet.cell_value(i, 0)
            self.resultRecord.age = self.Sheet.cell_value(i, 1)
            self.resultRecord.nationalID = self.Sheet.cell_value(i, 2)
            self.resultRecord.date_entered = self.Sheet.cell_value(i, 3)
            self.resultRecord.diabetes = self.Sheet.cell_value(i, 4)
            self.resultRecord.blood_presure = self.Sheet.cell_value(i, 5)
            self.resultRecord.covid_19 = self.Sheet.cell_value(i, 6)
            #-----------------------------------------------------
            db.add(self.resultRecord)
            db.commit()
        