# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyodbc
import glob
import pandas
import re


class c_bulk_insert:
    def __init__(self, csv_file_nm, sql_server_nm, db_nm, db_table_nm):
    # Connect to the database, perform the insert, and update the log table.
        conn = self.connect_db(sql_server_nm, db_nm)
        self.insert_data(conn, csv_file_nm, db_table_nm)
        conn.close

#{ODBC Driver 17 for SQL Server}

    def connect_db(self, sql_server_nm, db_nm):
        # Connect to the server and database with Windows authentication.
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + sql_server_nm + ';DATABASE=' + db_nm + ';Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        return conn


    def insert_data(self, conn, csv_file_nm, db_table_nm):
    # Insert the data from the CSV file into the database table.
    # Assemble the BULK INSERT query.
        columns = pandas.DataFrame()
        ColumnList = ''

    # Execute the query
        cursor = conn.cursor()
        ColumnList1 = pandas.read_csv(csv_file_nm, sep = '|',nrows = 1 )

        for col in ColumnList1.columns:
            colfix1 = str(col.replace(' ', '_'))
            colfix2 = str(colfix1.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+-", ""))
            colfix2 = re.sub('[^a-zA-Z0-9 \n\.]', '', colfix2)
            if len(colfix2) > 128:
                colfix2[0:115]

            #Put if statement here to make the object numeric if the data is numeric
            ColumnList = ColumnList +  "[" + colfix2+"]" +   ' varchar(MAX),'

        qry1b = "CREATE TABLE " + db_table_nm + " (" + ColumnList[0:len(ColumnList) - 1] + ")"
        qry1 = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm + "') BEGIN DROP TABLE " + db_table_nm + " "+ qry1b  + " END ELSE BEGIN " + qry1b + " END"
        print(qry1)
        qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH ( DATAFILETYPE = 'char', FIRSTROW = 2 ,FIELDTERMINATOR = '|',ROWTERMINATOR = '\n' )"

        try:
            cursor.execute(qry1)
            success = cursor.execute(qry)
            conn.commit()
            cursor.close

        except:
            print(colfix2, )






#After this is done running maybe it should move the file it loaded to a loaded folder so its obvious and data does not have to rerun
#Also we can make it so it does not quit out of the connection until its done looping
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #from c_bulk_insert import c_bulk_insert


    #Make there be a parameter that allows you to delete the table that already exist or not
    dir_path = r'A:\RE Data\MA 2022-2023 Data\**\*.*'
    Server_Name = 'DESKTOP-9MVETUM'
    DB_Name = 'MondeVert'



    #dir_path = r'C:\Users\sdono\Downloads\Real Estate Data\Load to SQL Server'
    for file in glob.glob(dir_path, recursive=True):
        TableName = file[(len(dir_path)- 6):(len(file)-4)]
        File_Name = file[(len(dir_path)- 6):len(file)]
        TableName1 =  str(TableName.replace(' ', '_'))
        TableName1 = str(TableName1.replace('%', ''))
        TableName1 = str(TableName1.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+-", ""))
        TableName1 = re.sub('[^a-zA-Z0-9 \n\.]', '', TableName1)



        if file.find(".txt")==(len(file)-4):
            bulk_insert = c_bulk_insert( file,Server_Name ,DB_Name , TableName1)
        else:
            print("Did not Load a non-.txt file - " + File_Name)
            #Do Nothing

