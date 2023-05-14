import pandas as pd
import openpyxl
import datetime
import Common_Utilities as CU
import User_Prefs as up

class MondeVert_Create_Requests():
    def __init__(self,Request_Source = 'Email*',Request_File = up.Sample_Request_File, Request_File_Name = 'SHAINE Request' ):
        self.Request_Source = r'A:\MondeVert Productions\SHAINE - MondeVert AI Assistant\SHAINE - MondeVert AI Assistant.xlsx'
        self.SavePath = up.SHAINE_Requests
        #Have a way of monitoring emails for now I can feed in an excel file
        #if it comes from an email, I will make an ID for it and then a folder for it respectively and then I will read the respective excel or whatever json file I get from the requestor
        #Requests = pd.ExcelFile(self.Request_Source)
        self.Request_File_Name = Request_File_Name

        #get_ID (use date with seconds etc and then persons email for now, eventually have customerID or something

        self.ID = MondeVert_Create_Requests.getID(self)
        self.Customer_Folder = 'SHAINE - Request Testing'
        self.Request_Folder = self.ID



        CU.Check_Folder_Exists(self.SavePath)

        self.SavePathMain = self.SavePath + '\\' + self.Customer_Folder
        CU.Check_Folder_Exists(self.SavePathMain)
        self.SavePathRequest = self.SavePathMain + '\\' + self.Request_Folder
        CU.Check_Folder_Exists(self.SavePathRequest)

        IgnoreSheets = ['Drop Down for User Experience','Digital Run']

        # your starting wb with 2 Sheets: Sheet1 and Sheet2
        Requests = openpyxl.load_workbook(self.Request_Source)

        sheets = Requests.sheetnames  # ['Sheet1', 'Sheet2']

        for s in sheets:
            for x in IgnoreSheets:
                if s == x:
                    sheet_name = Requests.get_sheet_by_name(s)
                    Requests.remove_sheet(sheet_name)


      #  NumRequests = len(Requests.sheet_names)

        self.Request_File_Name = self.Request_File_Name + self.Customer_Folder + self.ID
        self.SavePathFinal = self.SavePathRequest+'\\' + self.Request_File_Name + '.xlsx'


        # your final wb with just Sheet1
        Requests.save(self.SavePathFinal)

    #This is commented out for now, eventually I will make one folder I think per Tab not ewual to what I showed #
        # del Requests
        # for s in range(0,NumRequests):
        #     Request = pd.read_excel(self.Request_Source, sheet_name=s, header= 1, usecols=(0,3))
        #     #if





    def getID(self):
        #get_customer_ID for now ignore but eventually have a running list or DB with this info
        #Customer_ID = 'SHAINE Testing'

        current_time1 = datetime.datetime.now()
        xx = current_time1.strftime('Y%d%m%H%M%S')
        ID = xx



        return ID

class MondeVert_Request():
    def __init__(self, Request_File,ID, Date_Request_Received,Receipt_Method,Response_Method,Request_Type,Request_Sub_Type, Title, Bio, Audience, Goal_User, AI_Task, AI_Roles, Task, Key_Information, Outline_Task, Outline_Format, Special_Notes, Additional_Notes,AI_Rules,Scrum_Mode,Ignore_Parameters,Wizard_Modes):
        self.Request_File = Request_File
        self.ID = ID
        self.Date_Request_Received = Date_Request_Received
        self.Receipt_Method= Receipt_Method
        self.Response_Method=Response_Method
        self.Request_Type = Request_Type
        self.Request_Sub_Type = Request_Sub_Type
        self.Title = Title
        self.Bio = Bio
        self.Audience = Audience
        self.Goal_User = Goal_User
        self.AI_Task = AI_Task
        self.AI_Roles = Goal_User
        self.Task = Task
        self.Key_Information= Key_Information
        self.Outline_Task= Outline_Task
        self.Outline_Format= Outline_Format
        self.Special_Notes= Special_Notes
        self.Additional_Notes= Additional_Notes
        self.AI_Rules= AI_Rules
        self.Scrum_Mode= Scrum_Mode
        self.Ignore_Parameters= Ignore_Parameters
        self.Wizard_Modes = Wizard_Modes


#     def Read_Request(self):
#         print('test')
#
#     def Set_Request_Type(self):
#         print('test')
#
#     def Set_Key_Information(self):
#
# #move the multi threading to here, have a new place to run SHAINE make everything modular and less code per file
#     def Run_Tool(self,Requests, Key_Information,Outline,Goal, AI_Tasks ):
#         print('test')
#
#     def Send_Response(self):
#         print('test')
#




if __name__ == '__main__':
    MondeVert_Create_Requests()