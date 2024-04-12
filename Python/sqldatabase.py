import pyodbc


server = 'tcp:rmsserver2.database.windows.net'
database = 'RMSDB'
username = 'nithya'
password = 'Akhil387*'
driver= '{ODBC Driver 17 for SQL Server}'


conn  = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
cursor.execute("SELECT TOP (1000) * FROM [dbo].[studentresults]")
print(cursor.fetchall())
conn.close()



