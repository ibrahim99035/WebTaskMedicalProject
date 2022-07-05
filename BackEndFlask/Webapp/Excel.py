import xlrd
from Webapp.models import Patients
from flask_login import current_user
from Webapp import db
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed
class Excelentry(FlaskForm):
    TheFile = FileField('Upload Excel File', validators=[FileAllowed(['xlsx', 'xls'])])
    submit = SubmitField('Upload')
    
    def addRecord(self, ExcelPath):
        WorkBook = xlrd.open_workbook(ExcelPath)
        Sheet = WorkBook.sheet_by_index(0)
        limitRows = Sheet.nrows
        #-------------------------------------------------
        #add default values to the dtabase
        name = 'default'
        age = 0
        nationalID = 'default'
        diabetes = 'default'
        blood_presure = 'default'
        covid_19 = 'default'
        #-------------------------------------------------
        for i in range(1, limitRows):
            name = Sheet.cell_value(i, 0)
            age = Sheet.cell_value(i, 1)
            nationalID = Sheet.cell_value(i, 2)
            diabetes = Sheet.cell_value(i, 3)
            blood_presure = Sheet.cell_value(i, 4)
            covid_19 = Sheet.cell_value(i, 5)
        
        DataList = []
        if name != 'default':
            DataList.append(name)
        if age > 0:
            DataList.append(age)
        if nationalID != 'default':
            DataList.append(nationalID)
        if diabetes != 'default':
            DataList.append(diabetes)
        if blood_presure != 'default':
            DataList.append(blood_presure)
        if covid_19 != 'default':
            DataList.append(covid_19)
        
        #-----------------------------------------------------
        return DataList
        