# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:45:56 2019

@author: admin
"""

#!/usr/bin/python
import cx_Oracle
connstr='hr/hr@XE'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs
#curs.arraysize=50
curs.execute('SELECT CUSTNAME, city from customers order by CUSTNAME desc')
print("\nCUSTNAME\t city\n")
for column_1, column_2 in curs.fetchall():
        print(column_1, "\t", "\t", column_2)
curs.close()
conn.close()

#############################3

#import pyodbc 
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=LENOVO_PC;'
#                      'Database=AdventureWorks2014;'
#                      'Trusted_Connection=yes;')
#
#cursor = conn.cursor()
#cursor.execute('SELECT * FROM dbo.Table')
#
#for row in cursor:
#    print(row)