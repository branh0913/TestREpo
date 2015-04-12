__author__ = 'branh0913'

import pyexcel
import pyexcel_xls


myvar = pyexcel.load("Report_PatientAccountLedger-148786.xls")

myrows = myvar.rows()

for i in myrows:
    print(i)