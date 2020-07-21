import pyodbc as pdb
drivers = [item for item in pdb.drivers()]
driver = drivers[-1]
print("driver:{}".format(driver))
server = 'localhost'
database = 'testdb'
uid = 'sa'
pwd = '3141592654Pi'
con_string = f'DRIVER={driver}; SERVER={server}; DATABASE={database}; UID={uid}; PWD={pwd}'
print(con_string)
