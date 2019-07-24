# teste de conexao com DB

import pyodbc
server = 'ip'
database = 'master'
username =''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL SERVER}; SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
#sample select query
cursor.execute('SELECT @@version;')
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()



"""https://sqlchoice.azurewebsites.net/en-us/sql-server/developer-get-started/python/windows/step/2.html"""
"""https://riptutorial.com/pandas/example/7128/read-sql-server-to-dataframe"""
"""https://sql.programmingpedia.net/en/tutorial/184/getting-started-with-sql"""
"""https://developer.salesforce.com/forums/?id=9060G000000MPlLQAW"""