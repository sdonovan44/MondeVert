# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import pyodbc
import glob
import pandas as pd
import re
import datetime
import time
#from selenium import WebDriverWait
from time import sleep
from MondeVert_IP.SHAINE_MonderVert.Utilities import DoNotCommit as pw
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options


class MLSBot:
    def __init__(self, current_time2  = datetime.datetime.now()):
        self.current_time2 =current_time2
        self.current_time_START2 = self.current_time2.strftime('%Y-%m-%d_%H.%M.%S')
        self.current_time_START2 = self.current_time2.strftime('%Y-%m-%d_%H.%M.%S')
        self.SavePath1 = up.REData
        self.SavePath2 = self.SavePath1 + '\\' + self.current_time_START2
        MLSBot.SetUpFolders(self)

        options = Options()
        options.add_experimental_option("detach", True)
        prefs = {
            "download.default_directory": self.SavePath2 ,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        }

        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=options)


    def SignOutMLS(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        #self.driver.get(up.MLSURL2)
        #print ("Opened MLS")
        sleep(3)

        wait = ui.WebDriverWait(  self.driver, 10)
        try:
            # cookieConsentBootstrapModal
            wait.until(lambda driver:   self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/a'))
            #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.id, "cookieConsentBootstrapModal"))).click()
            login_box =   self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/a')
            login_box.click()
            self.driver.close()
        except:
            print('Not Signed in')
            self.driver.close()

        sleep(3)


    def SignINMLS(self):
        usr = pw.MLSUSer
        pwd=pw.MLSPW
        self.driver.get(up.MLSURL)
        sleep(3)
        wait = ui.WebDriverWait(self.driver, 15)
        try:
            # cookieConsentBootstrapModal
            wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="cookieConsentBootstrapModal"]/div/div/div[3]/button'))
            #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.id, "cookieConsentBootstrapModal"))).click()
            login_box = self.driver.find_element_by_xpath('//*[@id="cookieConsentBootstrapModal"]/div/div/div[3]/button')
            login_box.click()
        except:
            print('No Cookie Window')
        sleep(3)
        username_box = self.driver.find_element_by_name('user_name')
        username_box.send_keys(usr)
        #print ("Email Id entered")
        sleep(1)
        password_box = self.driver.find_element_by_name('pass')
        password_box.send_keys(pwd)
        #print ("Password entered")
        login_box = self.driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[7]/td/button')
        login_box.click()
        try:
            wait.until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/a'))

        except:
            login_box = self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td/center/button')
            login_box.click()
            print('Warning Message bypassed')


        time.sleep(10)
        #self.driver.execute_script("window.open('');")
        # Switch to the new window and open new URL
        #self.driver.switch_to.window(self.driver.window_handles[1])
        #self.driver.get(up.MLSURL2)
        #time.sleep(10)


    def DownloadFiles(self,RETypes = up.REType , Mode = 'All'):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.execute_script("window.open('');")
        # Switch to the new window and open new URL
        self.driver.switch_to.window(self.driver.window_handles[1])


        for x in RETypes :

            if (Mode == 'All' or 'SLD' not in x) and 'OH' not in x and 'VT' not in x:
                #webbrowser.open_new(up.REDATAURL + x)
                self.driver.get(up.REDATAURL + x)
            elif 'SLD' in x:
                #webbrowser.open_new(up.REDATAURL + x[0:1] + up.REURL_ADD)
                print(x[0:2] )
                self.driver.get(up.REDATAURL + x[0:2] +  up.REURL_ADD)
            else:
                doNothing = []


            time.sleep(10)
            if x == 'OH' or x == 'VT':
                #xnothing = []
                self.driver.get(up.REDATAURL2 + x)
            elif Mode == 'All':
                #webbrowser.open_new(up.REDATAURL + x + up.REURL_ADD)
                self.driver.get(up.REDATAURL + x +  up.REURL_ADD)
                time.sleep(10)
            else:
                doNothing = []

        #self.driver.close()

    #
    # def StoreFiles(self):
    #
    #     DailyFileCheck = 0
    #     Success_File_Tracker =[]
    #
    #     SavePath1 = up.REData
    #     SavePath2 = SavePath1 + '\\' + current_time_START2
    #     isExist = os.path.exists(SavePath1)
    #     if not isExist:
    #         # Create a new directory because it does not exist
    #         os.makedirs(SavePath1)
    #
    #     isExist = os.path.exists(SavePath2)
    #     if not isExist:
    #         # Create a new directory because it does not exist
    #         os.makedirs(SavePath2)
    #
    #
    #     ExpectedFileCount = len(up.RE_File_Names)
    #     #ExpectedFileCount = 2
    #
    #     while DailyFileCheck < ExpectedFileCount:
    #
    #
    #         path_of_the_directory = up.DownloadFolder
    #         paths = Path(path_of_the_directory).glob('**/*.txt')
    #         for file in paths:
    #             print(file)
    #
    #         #for file in glob.glob(up.DownloadFolder, recursive=True):
    #             File_Time1 = os.path.getctime(file)
    #             File_Time =time.ctime(File_Time1)
    #             #print ( File_Time)
    #
    #             x1 = int(re.sub('[^0-9]', '', str(current_time_START2))[0:12])
    #             dt = parse(File_Time)
    #             x22 =  dt.strftime('%Y-%m-%d_%H.%M.%S')
    #             x2 =  int(re.sub('[^0-9]', '', str(x22))[0:12])
    #                 #pd.to_datetime(File_Time) #.strftime('%m-%d-%Y_%H.%M.%S')
    #
    #
    #             print(dt)
    #             print (x1)
    #             print( x2 )
    #             ycheck = (x1 <= x2)
    #             #print('x1 <= x2: ' +  ycheck )
    #
    #             if x1 <= x2 :
    #                 original = file
    #                 File_Name = os.path.basename(file).split('/')[-1]
    #
    #                 #for fn in up.RE_File_Names:
    #                  #   if File_Name == fn:
    #                 if File_Name in up.RE_File_Names:
    #                     target = SavePath2 + '\\' + File_Name
    #                     shutil.move(original, target)
    #                     Success_File_Tracker.append(File_Name)
    #                     print(File_Name)
    #                     DailyFileCheck += 1
    #
    #                 else:
    #                     doNothing = []
    #             else:
    #                 doNothing = []
    #
    #         time.sleep(25)
    #         MLSBot.CheckForMissingFiles(Success_File_Tracker)
    #
    #     return DailyFileCheck
    #

    def SetUpFolders(self ):

        isExist = os.path.exists(self.SavePath1 )
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(self.SavePath1 )

        isExist = os.path.exists(self.SavePath2)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(self.SavePath2)



    def CheckForMissingFiles(self):
        DailyFileCheck = 0
        ExpectedFileCount = len(up.RE_File_Names)
        path_of_the_directory =  self.SavePath2


        while DailyFileCheck < ExpectedFileCount:
            paths = Path(path_of_the_directory).glob('**/*.txt')
            Success_File_Tracker = []
            DailyFileCheck = 0


            for file in paths:
                print(file)
                File_Name = os.path.basename(file).split('/')[-1]
                Success_File_Tracker.append(File_Name)
                DailyFileCheck +=1

            print('File List: ' + str(up.RE_File_Names))
            print('Current List of Files: ' +  str(Success_File_Tracker))
            MissingFiles = list(set(up.RE_File_Names).difference(Success_File_Tracker))
            MissingFiles1 = MissingFiles
            MissingFiles2 = []
            for f in MissingFiles:
                f = f[4:len(f)-4].upper()
                MissingFiles2.append(f)
                #print (f)
            print(MissingFiles2)
            if len(MissingFiles) > 0:
                print('Missing Files Identified, Redownloading the following: ' + str(MissingFiles1))
                MLSBot.DownloadFiles(self,MissingFiles2, Mode = 'Fix')
                time.sleep(240)
            else:
                print('confirmed All Files Downloaded')





    def MultiThread(self,Functions ,Args1 = ''):

        thread_list = []
        print("Start")
        Args = up.RE_File_Names
        for x in Args:
            t = threading.Thread(target=Functions, args = (self,x,))
            thread_list.append(t)



        Count1 = 0
        # Starts threads
        for thread in thread_list:

            time.sleep(3)
            thread.start()
            Count1 = Count1+1
            print(Count1)
            print("New Thread Started")

        # This blocks the calling thread until the thread whose join() method is called is terminated.
        # From http://docs.python.org/2/library/threading.html#thread-objects
        for thread in thread_list:
            thread.join()

    # Demonstrates that the main process waited for threads to complete
        print ( "Done")




    def getMLSData(self):
        #MLSBot.SignINMLS(self)
        print("Signed into MLS")
        #MLSBot.DownloadFiles(self,RETypes = ['SF'])
        Functions = [MLSBot.DownloadFiles]
        for x in Functions:
            MLSBot.MultiThread(self,x)
        #MLSBot.DownloadFiles(self)
        #MLSBot.DownloadFiles(self)
        time.sleep(280)
        MLSBot.CheckForMissingFiles(self)
        print("Files Downloaded")
        MLSBot.SignOutMLS(self)
        print("Signed out of MLS")




class c_bulk_insert:
    def __init__(self, csv_file_nm, sql_server_nm, db_nm, db_table_nm, WipeTable = False, As_of_Date = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')):
    # Connect to the database, perform the insert, and update the log table.
        conn = self.connect_db(sql_server_nm, db_nm)


        self.As_of_Date = As_of_Date


        self.newT = WipeTable
        self.groupby = ""
        self.errorc = []
        self.csv_file_nm = csv_file_nm
        print(csv_file_nm)
        self.AddNewData(conn, db_table_nm)
        print('6). New Data Loaded into Temp Table')
        self.Combine_Old_New(conn)
        print('11). Old and New Data Combined')
        if str(self.errorc) == []:
            print('No Errors File Loaded Successfully')
        else:
            print('Error(s): ' + str(self.errorc))
        conn.close


    def ReturnErrors(self):
        doNothing = []
        return self.errorc

    # Do the same thing for listing type so you can eventually combine all


#{ODBC Driver 17 for SQL Server}







    def connect_db(self, sql_server_nm, db_nm):
        # Connect to the server and database with Windows authentication.
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + sql_server_nm + ';DATABASE=' + db_nm + ';Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        return conn


    #def ResetTables(self):

    def Combine_Old_New(self, conn):

        # Make a min Date for listing start date (calculate age of listing)
        # calculate date sold
        # create a table for just active items
        # table for sold items with details
        # table for all unique updates
        # Eventually use a uniqueness for all raw values and then come up with row number for the min date to determine the update date
        cursor = conn.cursor()
        db_table_nm = self.db_table_nm
        db_table_nm_Load = self.db_table_nm + '_Load'
        db_table_nm_FullUniverse = self.db_table_nm + '_Full_Universe'
        db_table_nm_BackUp1 = self.db_table_nm + '_BackUp1'
        db_table_nm_BackUp2 = self.db_table_nm + '_BackUp2'
        Derivations = ', rank() over (partition by ' + self.groupby + ' order by As_of_date) as Original_Filter,  max(As_of_date) over (partition by ' + self.groupby + ' ) as Last_Active_Date, min(As_of_date) over (partition by ' + self.groupby + ' ) as Last_Update_Date, min(As_of_date) over (partition by ListNO ) as Listing_Date '
        Active_Case = 'Case when concat(' +  self.groupby + ') in (select distinct concat('+  self.groupby + ") as Check1 from " +  db_table_nm_Load +")  then 'Y' else 'N' end as Active_Record "
        FullUniverse_qry = 'select *   into ' + db_table_nm_FullUniverse + '_temp from ( select * '+ Derivations+  '  from (Select Distinct   t.LONG, m.*  from (Select Distinct ' + self.Combine_GroupBy + ' ,' + Active_Case + " from " + db_table_nm_FullUniverse + " union Select Distinct *, 'Y' as Active_Record  from " + db_table_nm_Load + ")  m left join [towns] t on m.TOWNNUM = t.TOWNNUM)d ) d where Original_Filter =1"
        #print("Update This: " + FullUniverse_qry)
        Check_NewTable = 'Select Distinct top 1 * from ' + db_table_nm
        worker_qry_NewFile  = "select *   into " + db_table_nm_FullUniverse + '_temp from ( select * '+ Derivations+  "  from ( Select Distinct   t.LONG, m.*, 'Y' as  Active_Record from ( Select Distinct *  from " + db_table_nm_Load + ')  m left join [towns] t on m.TOWNNUM = t.TOWNNUM)d )d where Original_Filter =1'
        CombineOldNew = 'select Distinct * into ' + db_table_nm + '  from (Select Distinct * from ' + db_table_nm_FullUniverse + ') combo'
        OnlyActive =  'select Distinct * into ' + db_table_nm + ' from (Select Distinct * from ' + db_table_nm_FullUniverse + ") combo where Active_Record = 'Y'"



        if self.db_table_nm[-3:] == 'sld':
            Main_Query = CombineOldNew
        else:
            Main_Query = OnlyActive


        if self.newT ==True:
            FullUniverse_qry = worker_qry_NewFile

        else:
            try:
                cursor.execute(Check_NewTable)
            except:
                print('Main Table Does not Exist')
                FullUniverse_qry = worker_qry_NewFile



        FullUniverseFix = 'Select * into '+db_table_nm_FullUniverse +' from ' + db_table_nm_FullUniverse + "_temp  "
        print("Update/Review This: " + FullUniverse_qry)
        WipeWorker = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm_FullUniverse + "_temp') BEGIN DROP TABLE " + db_table_nm_FullUniverse + "_temp   " + FullUniverse_qry + "  END ELSE BEGIN " + FullUniverse_qry + " END             IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm_FullUniverse + "') BEGIN DROP TABLE " + db_table_nm_FullUniverse + " " + FullUniverseFix + " END ELSE BEGIN " + FullUniverseFix + " END"
        WipeMain = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm + "') BEGIN DROP TABLE " + db_table_nm + " " + Main_Query + " END ELSE BEGIN " + Main_Query + " END"
        Backup1 = 'select Distinct * into ' + db_table_nm_BackUp1 + '  from (Select Distinct * from ' + db_table_nm_FullUniverse+ ') combo'
        Backup2 = 'select Distinct * into ' + db_table_nm_BackUp2 + '  from (Select Distinct * from ' + db_table_nm_BackUp1+ ') combo'
        BackUpMain2 = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm_BackUp2 + "') BEGIN DROP TABLE " + db_table_nm_BackUp2 + " " + Backup2 + " END ELSE BEGIN " + Backup2 + " END"
        BackUpMain1 = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm_BackUp1 + "') BEGIN DROP TABLE " + db_table_nm_BackUp1 + " "+ Backup1  + " END ELSE BEGIN " + Backup1 + " END"
        try:
            cursor.execute(BackUpMain2)
            print('7). Success - Wipe BackUp2 & ReAdd')
            conn.commit()
        except:
            print('error saving backup2')
            self.errorc.append('Error saving backup2')
        try:
            try:
                cursor.execute(BackUpMain1)
                conn.commit()
                print('8). Success - Wipe BackUp1 & ReAdd')
            except:
                print('error saving backup1')
                self.errorc.append('Error saving backup1')

            print(WipeWorker)
            cursor.execute(WipeWorker)
            conn.commit()
            print('9a). Success - Wipe Worker & reAdd')
            print(WipeMain)
            FixQuotes = cursor.execute(WipeMain)
            print('10). Success - Wipe Main & ReAdd')
            conn.commit()
            cursor.close

        except:
            print('Error - Review ' + self.csv_file_nm + ' not Fully loaded')
            self.errorc.append('Error - Review ' + self.csv_file_nm + ' not Fully loaded')
    def CheckFileWillLoad(self):
        new_lines = []
        RedoFile = False
        with open(self.csv_file_nm, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]


        while   '|' not in last_line:
            if '|' in last_line:
                doNothing = []
            else:
                lines = lines[0:-1]
                last_line = lines[-1]
                RedoFile = True

        if RedoFile == True:
            with open(self.csv_file_nm, 'w') as file2:
                file2.writelines(new_lines)




#For Sold we can have full list and dedupe, for active just latest file

    def AddNewData(self, conn,  db_table_nm):

        columns = pd.DataFrame()
        cursor = conn.cursor()
        ColumnList1 = pd.read_csv(self.csv_file_nm, sep = '|',nrows = 1 )
        ColumnList = ''
        colList = []
        db_table_nm = str(db_table_nm.replace(' ', '_'))
        db_table_nm = str(db_table_nm.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+-", ""))
        db_table_nm = re.sub('[^a-zA-Z0-9 \n\.]', '', db_table_nm)
        self.db_table_nm = db_table_nm
        db_table_nm = self.db_table_nm + '_Load'
        for col in ColumnList1.columns:
            colfix1 = str(col.replace(' ', '_'))
            colfix2 = str(colfix1.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+-", ""))
            colfix2 = re.sub('[^a-zA-Z0-9 \n\.]', '', colfix2)
            if len(colfix2) > 128:
                colfix2[0:115]

            #Put if statement here to make the object numeric if the data is numeric
            colList.append(colfix2)
            ColumnList = ColumnList +  "[" + colfix2+"]" +   ' varchar(MAX),'
            self.groupby =  self.groupby + '[' + colfix2 + "],"



        if self.db_table_nm[-3:] == 'sld':
            Status = 'Sold'
        else:
            Status = 'Active Listing'





        qry1b = "CREATE TABLE " + db_table_nm + " (" + ColumnList[0:len(ColumnList) - 1] + ")"
        qry1 = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm + "') BEGIN DROP TABLE " + db_table_nm + "  "+ qry1b  + " END ELSE BEGIN " + qry1b + " END"
        #DO NOT USE for now
       # qry11 = "IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME  = N'" + db_table_nm1 + "') BEGIN DROP TABLE " + db_table_nm1 + " END"
        #print(qry1)
        qry = "BULK INSERT " + db_table_nm + " FROM '" + self.csv_file_nm + """' WITH ( DATAFILETYPE = 'char', FIRSTROW = 2 ,FIELDTERMINATOR = '|',ROWTERMINATOR = '0x0A' )"""
        qry_ec = "BULK INSERT " + db_table_nm + " FROM '" + self.csv_file_nm + """' WITH ( DATAFILETYPE = 'char', FIRSTROW = 2 ,FIELDTERMINATOR = '|',ROWTERMINATOR = '\\n' )"""
        qry11= 'ALTER TABLE ' + db_table_nm + ' ADD  Load_Date  varchar(MAX);'
        qry12 = 'ALTER TABLE ' + db_table_nm +  ' ADD  As_of_Date  varchar(MAX); '
        qry13 ='ALTER TABLE ' + db_table_nm + ' ADD  [STATUS1] nvarchar(60);'
        qry2 = 'UPDATE ' + db_table_nm + " SET [Load_Date] = '" +  self.As_of_Date +"'  UPDATE " + db_table_nm + " SET [As_of_Date]= '"  + self.As_of_Date  +"'  UPDATE " + db_table_nm + " SET [STATUS1]= '"  + Status + "'"
        #qry2 = 'UPDATE ' + db_table_nm + " SET [Load_Date] = '" + self.As_of_Date + "'  UPDATE " + db_table_nm + " SET [As_of_Date]= '2023-02-09'  UPDATE " + db_table_nm + " SET [STATUS1]= '" + Status + "'"

        self.Combine_GroupBy = self.groupby + 'Load_Date, As_of_Date, Status1'
        self.groupby = self.groupby[0:-1]

        try:
            cursor.execute(qry1)
            conn.commit()
            print('1). Columns Added to table ' + db_table_nm)
            #print(qry1)

            try:
                #print(qry)
                success = cursor.execute(qry)
                conn.commit()
            except:
                print('Error - Review ' + self.csv_file_nm + ' not Fully loaded')
                self.errorc.append('Error - Review ' + self.csv_file_nm + ' not Fully loaded')
                c_bulk_insert.CheckFileWillLoad(self)
                #c_bulk_insert.AddNewData(self, conn, self.db_table_nm)
                success = cursor.execute(qry)
                conn.commit()

            print('2). Data Added to table')

            #print(qry11)

            #print(qry12)

            #print(qry13)

            cursor.execute(qry11)
            conn.commit()
            #print('3a). Added User Columns (Custom1) ' + db_table_nm1)
            cursor.execute(qry12)
            conn.commit()
            #print('3b). Added User Columns (Custom2) ' + db_table_nm1)
            cursor.execute(qry13)
            conn.commit()
            print('3). Added User Columns (Custom) ' + self.db_table_nm)
            print(qry2)
            success2 = cursor.execute(qry2)
            print('4). Load Info Added to table')
            conn.commit()

            for col1 in colList:
                fixQ = "update " +db_table_nm + "  set [" + col1 + '] = REPLACE([' + col1 + """],'"','');"""
                #print(fixQ)
                FixQuotes = cursor.execute(fixQ)
                #print('Quotes Fixed in Text Columns')
            print('5). Quotes Fixed in Text Columns')
            conn.commit()

            cursor.close

        except:
            print('Error - Review ' + self.csv_file_nm + ' not loaded')
            self.errorc.append('Error - Review ' + self.csv_file_nm + ' not loaded')
            c_bulk_insert.CheckFileWillLoad(self)
            c_bulk_insert.AddNewData(self,conn, self.db_table_nm)



#After this is done running maybe it should move the file it loaded to a loaded folder so its obvious and data does not have to rerun
#Also we can make it so it does not quit out of the connection until its done looping
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ErrorMessage = []
    #from c_bulk_insert import c_bulk_insert
    current_time_START = datetime.datetime.now()
    current_time_START2 = current_time_START.strftime('%Y-%m-%d_%H.%M.%S')


    xx = 1

    if xx == 1:
        x = MLSBot(current_time_START)
        x.getMLSData()




######Undo Comment out below
    #Make there be a parameter that allows you to delete the table that already exist or not
    #Data Pull #1
    #dir_path = up.REData + '\\' +current_time_START2 + '\**\*.*'
    # Data Pull #2
    #dir_path = up.REData + r'\2-9-2023\**\*.*'
    #dir_path = up.REData + r'\3-4-2023\**\*.*'
    dir_path = up.REData + r'\3-7-2023\**\*.*'
    #dir_path = up.REData + r'\2023-03-08\**\*.*'
    #dir_path = up.REData + r'\2023-03-11\**\*.*'
    #dir_path = up.REData + r'\2023-04-03\**\*.*'

    current_time_START2 = '2023-03-07'
    Server_Name = 'DESKTOP-9MVETUM'
    DB_Name = 'MondeVert_IP'



    #dir_path = r'C:\Users\sdono\Downloads\Real Estate Data\Load to SQL Server'
    for file in glob.glob(dir_path, recursive=True):
        TableName = file[(len(dir_path)- 6):(len(file)-4)]
        File_Name = file[(len(dir_path)- 6):len(file)]
        TableName1 =  str(TableName.replace(' ', '_'))
        TableName1 = str(TableName1.replace('%', ''))
        TableName1 = str(TableName1.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+-", ""))
        TableName1 = re.sub('[^a-zA-Z0-9 \n\.]', '', TableName1)


        if xx == 2:
        #if file == r'A:\RE Data\MA 2022-2023 Data\3-4-2023\idx_sf_sld.txt':
            if file.find(".txt")==(len(file)-4):
                x =  c_bulk_insert( file,Server_Name ,DB_Name , TableName1, WipeTable = False, As_of_Date= current_time_START2)
                ErrorMessage .append(x.ReturnErrors())
            else:
                print("Did not Load a non-.txt file - " + File_Name)
                #Do Nothing



    print(ErrorMessage)



#First take all of the
#
# with open(outfilename, 'wb') as outfile:
#     for filename in glob.glob('*.txt'):
#         if filename == outfilename:
#             # don't want to copy the output into the output
#             continue
#         with open(filename, 'rb') as readfile:
#             shutil.copyfileobj(readfile, outfile)