import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
import threading
from tkinter import filedialog, messagebox, Scrollbar
from tkinter import *
import time
import matplotlib
matplotlib.use('Qt5Agg')
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
from idlelib.tooltip import Hovertip
import os
import re
import random
from functools import partial
from multiprocessing import Process
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
import threading
from tkinter import filedialog, messagebox, Scrollbar
from tkinter import *
import time
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
from idlelib.tooltip import Hovertip
import os

LOGO =r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png"

#import ScrolledText






from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QTextEdit, QCheckBox, QStatusBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import threading
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStatusBar, QTextEdit, QCheckBox,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


#
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
#
#
#
# class CustomWindow11(QMainWindow):
#     def __init__(self, window_title, window_type, window_size, main_buttons,main_checkboxes,internal_frames):
#         self.main_buttons = main_buttons
#         self.main_checkboxes = main_checkboxes
#         self.internal_frame = internal_frames
#         self.window_title = window_title
#         self.window_type = window_type
#         self.window_size = window_size
#         self.FrameText = {}
#         self.FrameCount = 0
#
#         try:
#             super().__init__()
#             self.WINDOWNAME = str(self.WindowName + " - " + self.window_type)
#         except:
#             print('error super')
#             self.WINDOWNAME = 'SHAINE'
#
#
#         #window_size = self.WindowSize
#
#         #self.setWindowTitle(window_title + " - " + window_type)
#
#
#         try:
#             self.setWindowTitle(self.WINDOWNAME)
#             self.setGeometry(100, 100, *self.get_window_size(window_size))
#         except:
#             print("error")
#             try:
#                 self.setGeometry(100, 100,500,500)
#             except:
#                 print("error")
#         #
#         self.setup_ui(internal_frames)
#         self.SHAINELOG = "SHAINE Actions Taken: "
#         self.SHAINELOGCounter = 0
#         self.UserResponseProvided = False
# #        self.UserResponseProvided2 = False
#
#     def get_window_size(self, window_size):
#         try:
#             if window_size == "small":
#                 return 300, 200
#             elif window_size == "medium":
#                 return 500, 300
#             elif window_size == "large":
#                 return 800, 500
#             elif window_size == "XL":
#                 screen = QApplication.primaryScreen()
#                 screen_geometry = screen.availableGeometry()
#                 return screen_geometry.width(), screen_geometry.height()
#             elif window_size == "full_screen":
#                 return QApplication.desktop().screenGeometry().width(), QApplication.desktop().screenGeometry().height()
#             else:
#                 return 600, 400
#         except:
#             return 800, 500
#
#     def setup_ui(self, internal_frames):
#         # Create the main layout
#         layout = QGridLayout()
#
#         # Create the dropdown menu
#         menu_bar = self.menuBar()
#         file_menu = menu_bar.addMenu('File')
#         edit_menu = menu_bar.addMenu('Edit')
#         shaine_menu = menu_bar.addMenu('SHAINE')
#         help_menu = menu_bar.addMenu('Help')
#
#         # Create the buttons on the main screen
#         main_buttons_layout = QHBoxLayout()
#
#         # Create the checkboxes
#         checkbox_layout = QVBoxLayout()
#         checkbox_group = QButtonGroup()
#
#
#
#         # Create the functions for each button
#         # button_functions = {
#         #     'Last': self.last_function,
#         #     'Next': self.next_function,
#         #     'Original': self.original_function,
#         #     'Save': self.save_function,
#         #     'Use User Text': self.use_user_text_function,
#         #     'Rewrite With Edits': self.rewrite_with_edits_function,
#         #     'Generate': self.generate_function,
#         #     'User Edits': self.user_edits_function,
#         #     'Rewrite': self.rewrite_function,
#         #     'Speak': self.speak_function,
#         #     'Speak Input': self.speak_input_function,
#         #     'Continue': self.continue_function,
#         #     'Review Prompt': self.review_prompt_function,
#         #     'Review Outlines': self.review_outlines_function,
#         #     'Review Story(s)': self.review_stories_function,
#         #     'See Full Prompt': self.see_full_prompt_function,
#         #     'Prompt History': self.prompt_history_function
#         # }
#
#         # Create the checkboxes
#         checkbox_layout = QHBoxLayout()
#         for checkbox_text in self.main_checkboxes:
#             checkbox = QCheckBox(checkbox_text)
#             checkbox_layout.addWidget(checkbox)
#             checkbox_group.buttonClicked.connect(self.checkbox_function)
#
#         for button_text in self.main_buttons:
#             button = QPushButton(button_text)
#             #button.clicked.connect(lambda checked, btn=button_text, Frame = "Main": self.update_status_bar(btn, Frame))
#             #button.clicked.connect(lambda checked, btn=button_text: self.update_status_bar(btn))
#             button.clicked.connect(partial(self.update_status_bar, button_text, "Main", "Test Window"))
#
#             main_buttons_layout.addWidget(button)
#
#         # Set the checkbox functionality
#
#
#     # Define the functions for each button
#
#
#
#         #Not ready for this option yet, it is buggy and causes it to crash
#         # internet_button = QPushButton("Internet")
#         # internet_button.clicked.connect(self.open_web_browser)
#         # main_buttons_layout.addWidget(internet_button)
#         #layout.addLayout(checkbox_layout)
#         #layout.addLayout(main_buttons_layout)
#         #layout.addLayout(checkbox_layout, 0, 0, 2, 2)
#         layout.addLayout(main_buttons_layout, 0, 0, 1, 2)  # Add main buttons layout to grid layout
#
#         # Create the internal frames
#         self.frames = []
#         num_columns = 2 if len(internal_frames) > 1 else 1
#         for i, frame in enumerate(internal_frames):
#             frame_widget = self.create_internal_frame(frame)
#             layout.addWidget(frame_widget, i // num_columns + 1, i % num_columns)  # Add frame widget to grid layout
#             self.frames.append(frame_widget)
#
#         # Create the total word count label
#         self.total_word_count_label = QLabel("Total Word Count: 0")
#         layout.addWidget(self.total_word_count_label, len(internal_frames) // num_columns + 1, 0, 1,
#                          num_columns)  # Add total word count label to grid layout
#
#         # Create a status bar
#         self.statusBar = QStatusBar()
#         self.setStatusBar(self.statusBar)
#
#         # Create a central widget and set the layout
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(layout)
#         self.setCentralWidget(self.central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon(LOGO))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#
#         self.show()


from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import pyqtSignal, pyqtSlot
class CustomWindow11(QMainWindow):
    def __init__(self):
        # t = threading.Thread(target=self.TE.CreateWindow,args=())
        d = 1
          # Start the application
        self.SHAINELOGCounter = 0






        #CustomWindow11.CreateWindow(self)

    def CreateWindow(self ,window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames):
        self.TE_APP = QApplication([])
        self.UserResponseProvided = False
        self.CloseWindow = False
        text_changed = pyqtSignal(str)
        try:
            super().__init__()
            #print('super successful')
        except:
            print('error super')
        self.main_buttons = main_buttons
        self.main_checkboxes = main_checkboxes
        self.internal_frame = internal_frames
        self.window_title = window_title
        self.window_type = window_type
        self.window_size = window_size
        self.FrameText = {}
        self.FrameCount = 0


        try:

            self.WINDOWNAME = str(self.WindowName + " - " + self.window_type)
        except:
            #print('error WindowName')
            self.WINDOWNAME = 'SHAINE'

        try:
            if window_size == "full_screen" or  window_size == "large":
                self.showFullScreen()
            else:
                self.setFixedSize(*self.get_window_size(window_size))
                self.center_window()

            self.setWindowTitle(self.WINDOWNAME)
            self.setGeometry(100, 100, *self.get_window_size(window_size))
        except:
            print("error")
            try:
                self.setGeometry(100, 100, 500, 500)
            except:
                print("error")


        self.SHAINELOG = "SHAINE Actions Taken: "
        self.setup_ui(self.internal_frame )
        if self.CloseWindow == True:
            self.close()
        #     self.central_widget.close()
        #     self.TE_APP.quit()



# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.checkbox import CheckBox
#
# class CustomWindow11(App):
#     def __init__(self):
#         self.SHAINELOGCounter = 0
#         self.window_layouts = {}  # Dictionary to store window layouts
#
#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         label = Label(text='Hello, Kivy!')
#         text_input = TextInput()
#         button = Button(text='Create Window')
#         button.bind(on_press=self.create_window)  # Bind the button press to the create_window method
#         layout.add_widget(label)
#         layout.add_widget(text_input)
#         layout.add_widget(button)
#         return layout
#
#     def CreateWindow(self, window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames):
#
#
#         # Create the main window layout
#         main_layout = GridLayout(cols=1)
#         main_label = Label(text=window_title)
#         main_layout.add_widget(main_label)
#
#         # Create the main buttons
#         main_buttons_layout = BoxLayout(orientation='horizontal')
#         for button_text in main_buttons:
#             button = Button(text=button_text)
#             main_buttons_layout.add_widget(button)
#         main_layout.add_widget(main_buttons_layout)
#
#         # Create the main checkboxes
#         main_checkboxes_layout = BoxLayout(orientation='horizontal')
#         try:
#             for checkbox_text in main_checkboxes:
#                 checkbox = CheckBox(active=False, label=checkbox_text)
#                 main_checkboxes_layout.add_widget(checkbox)
#             main_layout.add_widget(main_checkboxes_layout)
#         except:
#             print("No Checkboxes")
#
#         # Create the internal frames
#         for frame_info in internal_frames:
#             frame_layout = GridLayout(cols=1)
#             frame_title, frame_text, frame_buttons, frame_checkboxes, frame_color = frame_info
#
#             frame_label = Label(text=frame_title)
#             frame_layout.add_widget(frame_label)
#
#             frame_text_input = TextInput(text=frame_text)
#             frame_layout.add_widget(frame_text_input)
#
#             frame_buttons_layout = BoxLayout(orientation='horizontal')
#             for button_text in frame_buttons:
#                 button = Button(text=button_text)
#                 frame_buttons_layout.add_widget(button)
#             frame_layout.add_widget(frame_buttons_layout)
#
#             frame_checkboxes_layout = BoxLayout(orientation='horizontal')
#             for checkbox_text in frame_checkboxes:
#                 checkbox = CheckBox(active=False, label=checkbox_text)
#                 frame_checkboxes_layout.add_widget(checkbox)
#             frame_layout.add_widget(frame_checkboxes_layout)
#
#             frame_layout.background_color = frame_color
#             main_layout.add_widget(frame_layout)
#
#             # Store the window layout in the dictionary with the frame title as the key
#             self.window_layouts[frame_title] = frame_layout
#
#         # Create the 'Continue' button to close the window and quit the program
#         continue_button = Button(text='Continue')
#         continue_button.bind(on_press=self.close_window)
#         main_layout.add_widget(continue_button)
#
#         # Set the main window as the root widget
#         self.root = main_layout

    def close_window(self, instance):
        self.stop()  # Close the window and quit the program

    def update_frame_text(self, frame_title, new_text):
        if frame_title in self.window_layouts:
            for widget in self.window_layouts[frame_title].children:
                if isinstance(widget, TextInput):
                    widget.text = new_text
                    break  # Assuming there's only one TextInput in each frame

    def update_frame_buttons(self, frame_title, new_buttons):
        if frame_title in self.window_layouts:
            for widget in self.window_layouts[frame_title].children:
                if isinstance(widget, BoxLayout):
                    if widget.orientation == 'horizontal':
                        for button in widget.children:
                            widget.remove_widget(button)
                        for button_text in new_buttons:
                            new_button = Button(text=button_text)
                            widget.add_widget(new_button)
                    break  # Assuming there's only one BoxLayout in each frame



    def get_window_size(self, window_size):
        try:
            if window_size == "small":
                return 300, 200
            elif window_size == "medium":
                return 500, 300
            elif window_size == "large":
                return 800, 500
            elif window_size == "XL":
                screen = QApplication.primaryScreen()
                screen_geometry = screen.availableGeometry()
                return screen_geometry.width(), screen_geometry.height()
            elif window_size == "full_screen":
                return QApplication.desktop().screenGeometry().width(), QApplication.desktop().screenGeometry().height()
            else:
                return 600, 400
        except:
            return 800, 500

    def setup_ui(self, internal_frames):
        # Create the main layout
        layout = QGridLayout()

        # Create the dropdown menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        shaine_menu = menu_bar.addMenu('SHAINE')
        help_menu = menu_bar.addMenu('Help')

        # Create the buttons on the main screen
        main_buttons_layout = QHBoxLayout()

        # Create the checkboxes
        checkbox_layout = QVBoxLayout()
        checkbox_group = QButtonGroup()

        # Create the checkboxes
        try:
            checkbox_layout = QHBoxLayout()
            for checkbox_text in self.main_checkboxes:
                checkbox = QCheckBox(checkbox_text)
                checkbox_layout.addWidget(checkbox)
                checkbox_group.buttonClicked.connect(self.checkbox_function)
        except:
            dn = 100


        for button_text in self.main_buttons:
            button = QPushButton(button_text)
            button.clicked.connect(partial(self.update_status_bar, button_text, "Main", "Test Window"))
            main_buttons_layout.addWidget(button)

        layout.addLayout(main_buttons_layout, 0, 0, 1, 2)  # Add main buttons layout to grid layout

        # Create the internal frames
        self.frames = []
        num_columns = 2 if len(internal_frames) > 1 else 1
        for i, frame in enumerate(internal_frames):
            frame_widget = self.create_internal_frame(frame)
            layout.addWidget(frame_widget, i // num_columns + 1, i % num_columns)  # Add frame widget to grid layout
            self.frames.append(frame_widget)

        # Create the total word count label

        #word_count_label = QLabel(f"Word Count: {word_count}" + "  " + f"Character Count: {character_count}")
        self.total_word_count_label = QLabel("Total Word Count: 0")
        layout.addWidget(self.total_word_count_label, len(internal_frames) // num_columns + 1, 0, 1,
                         num_columns)  # Add total word count label to grid layout

        # Create a status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Create a central widget and set the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        # Set window icon
        self.setWindowIcon(QIcon(LOGO))

        # Set desktop thumbnail
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)



          # Run the application event loop


        self.show()

        #while(self.CloseWindow==False):
        self.TE_APP.exec_()



        # while True:
        #     QApplication.processEvents()
        #     # Continue with other code execution
        #
        #     # Check if you want to exit the loop and stop the GUI
        #     if self.CloseWindow==True:
        #         break








    def closeEvent(self, event):
        # Add your code here to handle the close event
        # For example, you can save any unsaved data or perform cleanup tasks
        event.accept()  # Accept the close event
    def WindowShow(self):
        #self.show()
        d = 100


    def checkbox_function(self, checkbox):
        checkbox_text = checkbox.text()
        checkbox_state = checkbox.isChecked()
        # Implement the desired functionality based on the checkbox state and text

    def create_internal_frame(self, frame_info):

        frame_widget = QWidget()
        frame_layout = QVBoxLayout()

        title, text_value, buttons, checkboxes, color = frame_info
        #print(frame_info)

        # Create the text widget
        text_edit = QTextEdit(text_value)
        text_edit.setObjectName(title)
        text_edit.setStyleSheet("background-color: white;")  # Set text field background color
        text_edit.textChanged.connect(lambda: self.update_word_count(text_edit))

        # Create the word count label
        word_count =len(text_value.split())
        character_count=  len(text_value)
        word_count_label = QLabel(f"Word Count: {word_count}" + "  " + f"Character Count: {character_count}")
        word_count_label.setStyleSheet("font-weight: bold;")  # Set label font weight
        word_count_label.setStyleSheet("background-color: #f0f0f0;")  # Set text field background color




        # Create the buttons
        button_layout = QHBoxLayout()
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("background-color: #f0f0f0;")  # Set button background color
            #button.clicked.connect(lambda checked, btn=button_text, Frame = title: self.update_status_bar( btn, Frame))
            button.clicked.connect(partial(self.update_status_bar, button_text, title, self.WINDOWNAME))
            button_layout.addWidget(button)


        # Create the checkboxes
        checkbox_layout = QHBoxLayout()
        for checkbox_text in checkboxes:
            checkbox = QCheckBox(checkbox_text)
            checkbox_layout.addWidget(checkbox)

        # Set the color scheme
        if color:
            frame_widget.setStyleSheet(
                f"background-color: {color}; border: 4px solid black;")  # Set frame background color and border

        TITLE = QLabel(title)
        TITLE.setStyleSheet("font-weight: bold; color: white;")  # Set label font weight and color
        TITLE.setStyleSheet("background-color: #f0f0f0;")  # Set text field background color



        # Add the title, text widget, word count label, character count label, buttons, and checkboxes to the frame layout
        frame_layout.addWidget(TITLE)
        frame_layout.addLayout(checkbox_layout)
        frame_layout.addLayout(button_layout)
        # print("text title:")
        # print(title)
        # print( "self.FrameText[title]")
        self.FrameText[title] = text_edit
        # print( self.FrameText[title])

        frame_layout.addWidget(text_edit)
        frame_layout.addWidget(word_count_label)
        #frame_layout.addWidget(character_count_label)


        # Set the frame layout to the frame widget
        frame_widget.setLayout(frame_layout)
        self.FrameCount += 1
        return frame_widget

    def update_word_count(self, text_edit):
        word_count = len(text_edit.toPlainText().split())
        character_count = len(text_edit.toPlainText())
        for label in text_edit.parent().findChildren(QLabel):
            # if label.text().startswith("Word Count:"):
            #     label.setText()
            if label.text().startswith("Word Count:"):
                label.setText(f"Word Count: {word_count}" + f"Character Count: {character_count}")

        total_word_count = sum([len(text_edit1.toPlainText().split()) for text_edit1 in self.findChildren(QTextEdit)])
        total_Char_count = sum([len(text_edit1.toPlainText()) for text_edit1 in self.findChildren(QTextEdit)])
        self.total_word_count_label.setText(f"Total Word Count: {total_word_count}" + "   "+ f"Total Char Count: {total_Char_count}")

    def update_text_edit(self, text_edit, button_text):
        self.SHAINELOGCounter +=1
        self.SHAINELOG += str(self.SHAINELOGCounter) + '). ' + button_text + up.LineBreak_1
        current_text = text_edit.toPlainText()
        if current_text:
            current_text += f" {button_text}"
        else:
            current_text = button_text
        text_edit.setText(current_text)

    def getClose(self):
        f = self.CloseWindow
        return f

    def update_status_bar(self, button_name, Frame, Window):

        #self.RestoreLastUserText

        #self.RestoreUserInput
        #self.EndUserInput
        #self.EndUserInputSmall
        #self.EndUserInputMain
        #self.MakeArt

        #status_message = f"SHAINE: {button_name} - {Frame}"

        #status_message = f"SHAINE: {button_name}"
        status_message = f"SHAINE: {button_name} - {Frame} - {Window}"
        print(status_message)
        #self.statusBar.showMessage(status_message)
        # Call the respective function based on the button name
        if self.UserResponseProvided == False:
            if button_name == "<":
                #self.last_function()

                if "GPT" in Frame.upper():
                    self.ReturnLast()
                elif "PROMPT" in Window.upper():
                    self.RestorePrompt()

            elif button_name == "OG":
                #self.original_function()
                if "GPT" in Frame.upper():
                    self.ReturnOrig()
                elif "PROMPT" in Window.upper():
                    self.RestorePrompt_original()


            elif button_name == "Use User Text":
                self.UseUserText()
                #self.use_user_text_function()
            elif button_name == "Rewrite with User Edits":
                self.ReWriteWithEdit()
                #self.rewrite_with_edits_function()

            elif button_name == "User Edits":
                #self.user_edits_function()
                self.SmallEdit()
            elif button_name == "ReWrite":
                #self.rewrite_function()
                self.ReWrite()
            elif button_name == "Speak":
                #self.speak_function()
                if "PROMPT" in Window.upper():
                    self.Speak2()
                else:
                    if 'GPT' in Frame.upper():
                        self.FINALGPTOUTPUT = self.FrameText["CHAT GPT"].toPlainText()
                        self.Speak(Text= self.FINALGPTOUTPUT)
                    else:
                        self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
                        self.Speak(Text=self.UserEdits)
                    #self.Speak()

            elif button_name == "Continue":
                #self.continue_function()
                if "PROMPT" in Window.upper():
                    self.Continue_Button2()
                else:
                    # print("Frame")
                    # print(Frame)
                    self.Continue_Button()

            elif button_name == "Review Prompts":
                self.ReviewPrompt()
                #self.review_prompt_function()


            elif button_name == "Next":
                self.next_function()
            elif button_name == ">":
                dn = 100
            # elif button_name == "<":
            #     dn = 100
            elif button_name == "Save":
                self.save_function()
            elif button_name == "Generate":
                self.generate_function()
            elif button_name == "Speak Input":
                self.speak_input_function()
            elif button_name == "Review Outlines":
                self.review_outlines_function()
            elif button_name == "Review Story(s)":
                self.review_stories_function()
            elif button_name == "See Full Prompt":
                self.see_full_prompt_function()
            elif button_name == "Prompt History":
                self.prompt_history_function()

            elif button_name == "IGNORE SMALL":
                self.EndUserInputSmall()

            # elif button_name == "MEDIUM":
            #     self.EndUserInputSmall()

            elif button_name == "IGNORE BIG":
                self.EndUserInputMain()
            elif button_name == "IGNORE ALL":
                self.EndUserInput()

            elif button_name == "RESTORE ALL":
                self.RestoreUserInput()




    def last_function(self):
        # Add your code here
        pass

    def next_function(self):
        # Add your code here
        pass

    def original_function(self):
        # Add your code here
        pass

    def save_function(self):
        # Add your code here
        pass

    # def use_user_text_function(self):
    #     # Add your code here
    #     pass

    # def rewrite_with_edits_function(self):
    #     # Add your code here
    #     pass

    def generate_function(self):
        # Add your code here
        pass

    # def user_edits_function(self):
    #     # Add your code here
    #     CustomWindow11.UseUserText(self)
    #     pass

    # def rewrite_function(self):
    #     # Add your code here
    #     pass

    # def speak_function(self):
    #     # Add your code here
    #     pass

    def speak_input_function(self):
        # Add your code here
        pass

    def continue_function(self):
        # Add your code here
        print('Exit')
        self.CloseWindow = True

        pass

    # def review_prompt_function(self):
    #     # Add your code here
    #     self.ReviewPrompt()
    #     pass

    def review_outlines_function(self):
        # Add your code here
        pass

    def review_stories_function(self):
        # Add your code here
        pass

    #def see_full_prompt_function(self):
        # Add your code here
        #self.ReviewPrompt()

    def prompt_history_function(self):
        # Add your code here
        pass


    def handle_all_checkbox(self, state):
        if state == 0:
            self.big_checkbox.setChecked(False)
            self.medium_checkbox.setChecked(False)
            self.small_checkbox.setChecked(False)
            self.RestoreUserInput = False
            #self.EndUserInput()

        else:
            self.big_checkbox.setChecked(True)
            self.medium_checkbox.setChecked(True)
            self.small_checkbox.setChecked(True)
            #self.RestoreUserInput()


    def handle_other_checkbox(self, state):
        if state == 0:
            self.all_checkbox.setChecked(False)
        else:
           # if state ==1:

            if self.big_checkbox.isChecked() and self.medium_checkbox.isChecked() and self.small_checkbox.isChecked():
                self.all_checkbox.setChecked(True)



        #self.RestoreUserInput
        #self.EndUserInput
        #self.EndUserInputSmall
        #self.EndUserInputMain


    # def open_web_browser(self):
    #     web_browser_thread = threading.Thread(target=create_web_browser_window)
    #     web_browser_thread.start()




    # def update_status_bar(self, button_text):
    #     status_message = f"SHAINE: {button_text}"
    #     self.statusBar.showMessage(status_message)

    def RestoreLastUserText(self):

        USERLASTEDIT = self.USERLASTEDIT
        CustomWindow11.GetUserText(self)
        CustomWindow11.UpdateUserText(self, self.USERLASTEDIT)
        self.USERLASTEDIT = self.UserEdits
        return self.USERLASTEDIT

    def GetUserText(self):

        self.UserEdits = self.FrameText["USER EDITS"].toPlainText()



        print("self.UserEdits")
        print(self.UserEdits)
        return self.UserEdits

    def GetUserResponseMode(self):
        return self.UserResponseMode

    def GetUserResponseMain(self):
        self.UserConfirm = True
        CustomWindow11.MakeWindow(self)
        self.x =  self.FrameText["USER EDITS"].toPlainText()

        # I May not want to do this, I may be closing windows I do not want to

        # try:
        #     if self.WindowClose == True:
        #         self.window.destroy()
        #     if self.WindowClose2 == True:
        #         self.window2.destroy()
        # except:
        #     print('Error With Window, continue, maybe look into later')
        return self.x

    def Continue_Button2(self, Mode=0):

        try:

            self.WindowClose2 = True
            self.WindowClose = True
            self.CloseWindow = True
        except:
            dn = 1
        CustomWindow11.UserResponse(self, Mode, UIversion=2)

        # self.UserEdits = "0"
        return "0"

    def Continue_Button(self, Mode=0):

        try:
            self.FINALGPTOUTPUT= self.FrameText["CHAT GPT"].toPlainText()
            #self.FINALGPTOUTPUT = self.FrameText["CHAT GPT"].toPlainText()
            self.WindowClose = True
            self.CloseWindow = True



        except:
            dn = 1
        CustomWindow11.UserResponse(self, Mode, UIversion=1)

        # self.UserEdits = "0"
        return "0"

    def EndUserInput(self, Mode=5):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "5"
        return "5"

    def RestoreUserInput(self, Mode=50):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "5"
        return "50"

    def EndUserInputSmall(self, Mode=6):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "6"
        return "6"

    def EndUserInputMain(self, Mode=7):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "7"
        return "7"

    def MakeArt(self, Mode=8):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "8"
        return "8"

    def ReviewPrompt(self, Mode=10):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "8"
        return "10"

    def ReturnLast(self, Mode=12):
        CustomWindow11.UserResponse(self, Mode, UIversion=1)
        closeWindow = True
        # self.UserEdits = "8"
        return "12"

    def ReturnOrig(self, Mode=11):
        CustomWindow11.UserResponse(self, Mode, UIversion=1, closeWindow=True)

        # self.UserEdits = "8"
        return "11"

    def UpdateGPTResponse(self, Text):
        # Get the new data from some source
        new_data = "New data"
        title = "CHAT GPT"
        # Delete existing content in the Text widget
        #self.Printtxt.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.Printtxt.insert(tk.END, Text)
        # print("self.FrameText[title]:")
        # print(self.FrameText[title])

        #self.TE_APP.text_changed.emit(Text, title)
        self.FrameText[title].setText(Text)




    def UpdateUserText(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        #self.UserInput.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput.insert(tk.END, Text)

        self.FrameText["USER EDITS"].setText(Text)


    # def UpdateWordCountField(self, Text):
    #     # Get the new data from some source
    #     new_data = "New data"
    #     # Delete existing content in the Text widget
    #     self.WordCountField.delete("1.0", tk.END)
    #     # Add the new data to the Text widget
    #     self.WordCountField.insert(tk.END, Text)
    #
    # def UpdateWordCountField2(self, Text):
    #     # Get the new data from some source
    #     new_data = "New data"
    #     # Delete existing content in the Text widget
    #     self.WordCountField2.delete("1.0", tk.END)
    #     # Add the new data to the Text widget
    #     self.WordCountField2.insert(tk.END, Text)

    def UpdateUserInput_fld_System(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        #self.UserInput_fld_SYSTEM.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput_fld_SYSTEM.insert(tk.END, Text)
        self.FrameText["System"].setText(Text)

    def UpdateUserInput_fld_Role(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        #self.UserInput_fld_ROLE.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput_fld_ROLE.insert(tk.END, Text)
        self.FrameText["Role"].setText(Text)

    def UpdateUserInput_fld_FORMAT(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        #self.UserInput_fld_FORMAT.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput_fld_FORMAT.insert(tk.END, Text)
        self.FrameText["Format"].setText(Text)

    def UpdateUserInput_fld_TASK(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        # self.UserInput_fld_TASK.delete("1.0", tk.END)
        # # Add the new data to the Text widget
        # self.UserInput_fld_TASK.insert(tk.END, Text)
        self.FrameText["Task"].setText(Text)


    def UpdateUserInput_fld_Background(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        # self.UserInput_fld_Background.delete("1.0", tk.END)
        # # Add the new data to the Text widget
        # self.UserInput_fld_Background.insert(tk.END, Text)
        self.FrameText["Background"].setText(Text)

    def UpdateUserInput_fld_Background2(self, Text):
        # Delete existing content in the Text widget
        # self.UserInput_fld_Background2.delete("1.0", tk.END)
        # # Add the new data to the Text widget
        # self.UserInput_fld_Background2.insert(tk.END, Text)
        self.FrameText["Background2"].setText(Text)

    def UpdateUserInput_fld_Background3(self, Text):
        # self.UserInput_fld_Background3.delete("1.0", tk.END)
        # self.UserInput_fld_Background3.insert(tk.END, Text)
        self.FrameText["Background3"].setText(Text)

    def UpdateUserInput_fld_Version(self, Text):
        # self.UserInput_fld_version.delete("1.0", tk.END)
        # self.UserInput_fld_version.insert(tk.END, Text)
        self.FrameText["Version"].setText(Text)


    def UpdateUserInput_fld_Crazy(self, Text):
        #self.UserInput_fld_Crazy.delete("1.0", tk.END)
        self.FrameText["Crazy"].setText(Text)

    def UpdateGPTResponseWindow(self, NewGPTResponse, NewCurrentPrompt, NEWUSERLASTEDIT):
        self.UserResponseProvided = False
        CustomWindow11.UpdateGPTResponse(self, NewGPTResponse)
        self.Current_PROMTS_ALL = NewCurrentPrompt
        self.USERLASTEDIT = NEWUSERLASTEDIT
        # self.Window.title(NEWWINDOWNAME)

    def UpdatePromptWindow(self, NewSystem, NewRole, NewFormat, NewTask, NewBackground, NewBackground2, NewBackground3,
                           NewCrazy, NewVersion, NewModel):
        self.UserResponseProvided = False
        CustomWindow11.UpdateUserInput_fld_System(self, NewSystem)
        CustomWindow11.UpdateUserInput_fld_Role(self, NewRole)
        CustomWindow11.UpdateUserInput_fld_FORMAT(self, NewFormat)
        CustomWindow11.UpdateUserInput_fld_TASK(self, NewTask)
        CustomWindow11.UpdateUserInput_fld_Background(self, NewBackground)
        CustomWindow11.UpdateUserInput_fld_Background2(self, NewBackground2)
        CustomWindow11.UpdateUserInput_fld_Background3(self, NewBackground3)
        CustomWindow11.UpdateUserInput_fld_Crazy(self, NewCrazy)
        # TextEdit.UpdateUserInput_fld_Version(self,NewVersion)

    def UpdateWindow(self, Text1='', Text2='', Text3=''):
        if Text != '':
            x = 1

    def GetSpeakText(self):
        return self.Speak_Text

    def Speak(self, Mode=9, Text = ""):

        try:
            try:
                self.Speak_Text = Text
                CustomWindow11.UserResponse(self, Mode, UIversion=1, closeWindow=False)
                # threads.append(t)
            except:
                print("Error While trying to read outloud")
        except:
            print("Error While trying to read outloud #2")

        #self.UserEdits = "9"
        return "9"

    def SmallEdit(self, Mode=1):

        #self.UserEdits = self.UserInput.get(1.0, END)
        self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
        CustomWindow11.UserResponse(self, Mode, UIversion=1, closeWindow=False)

        return "1"

    def ReWriteWithEdit(self, Mode=2):

        #self.UserEdits = self.UserInput.get(1.0, END)
        self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
        CustomWindow11.UserResponse(self, Mode, UIversion=1, closeWindow=False)

        return "2"

    def ReWrite(self, Mode=3):
        CustomWindow11.UserResponse(self, Mode, UIversion=1, closeWindow=False)

        # self.UserEdits = "3"
        return "3"

    def UseUserText(self, Mode=4):
        self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
        #might want to change this eventually
        #self.CloseWindow = True
        CustomWindow11.UserResponse(self, Mode, UIversion=1, closeWindow=True)

        # self.UserEdits = "4"
        return "4"

        # Decide which numbers not to close window on, for instance, Speak, Review Responses, use prior response,

    def UserResponse(self, Mode, UIversion, closeWindow=True):
        self.UserResponseMode = Mode

        if UIversion == 2 and self.UserResponseProvided == False:
            try:
                CustomWindow11.GetPrompts(self)  # print(Mode)
                self.UserResponseProvided = True

                try:
                    if self.CloseWindow == True:
                        #self.window2.destroy()
                        #CustomWindow11.closeWindow(self)
                        #self.TE_APP.quit()
                        dn = 100

                        #self.TE_APP.close()
                        #os._exit(1)
                        # self.central_widget.close()
                        #sys.exit()
                except:

                    print("Error Trying to close window")

            except:
                print("Error while trying to pull User Values from Prompt")


        elif UIversion == 1 and self.UserResponseProvided == False:
            try:

                self.UserResponseProvided = True
                try:
                    self.FINALGPTOUTPUT = self.FrameText["CHAT GPT"].toPlainText()
                    self.UserEdits = CustomWindow11.GetUserText(self)
                except:
                    dn = 100
                try:
                    if self.CloseWindow == True:
                        #self.window.destroy()
                        #CustomWindow11.closeWindow(self)
                        #self.central_widget.close()

                        #self.TE_APP.quit()
                        dn = 100

                        #self.TE_APP.close()
                        #os._exit(1)
                        #sys.exit()

                except:
                    print("Error Trying to close window")

            except:
                print("Error while trying to pull User Values from Prompt")


        self.CloseWindow = True
        self.TE_APP.quit()
        # if self.CloseWindow == True:
        #     self.close()

        self.UserResponseProvided = True
        if Mode == 0:
            # print("Pass")
            c = 1

        return Mode

    def GetUserResponseProvided(self):
        #print(self.UserResponseProvided)
        return self.UserResponseProvided


    def GetWindowClose(self):
        return self.WindowClose

    def GetWindowClose2(self):
        return self.WindowClose2

    def GetCloseWindow(self):
        return self.CloseWindow


    def GetUserResponseProvided2(self):
        return self.UserResponseProvided2

    def GetUserResponse(self):
        return self.UserResponseMode

    def GetFinalGPTOutput(self):
        return self.FINALGPTOUTPUT

    def Get_System(self):
        return self.UserPromptSystem

    def Get_Role(self):
        return self.UserPromptRole

    def Get_Format(self):
        return self.UserPromptFormat

    def Get_Task(self):
        return self.UserPromptTask

    def Get_Background(self):
        return self.UserPromptBackground

    def Get_Background2(self):
        return self.UserPromptBackground2

    def Get_Background3(self):
        return self.UserPromptBackground3

    def Get_version(self):
        # TextEdit.GetPrompts(self)
        return self.UserPromptversion

    def Get_Crazy(self):
        return self.UserPromptCrazy

    def GetPrompts(self):
        x = 1

        self.UserPromptSystem = ''
        self.UserPromptRole = ''
        self.UserPromptFormat = ''
        self.UserPromptTask = ''
        self.UserPromptBackground = ''
        self.UserPromptBackground2 = ''
        self.UserPromptBackground3 = ''
        self.UserPromptCrazy = ''
        self.UserPromptversion = ''
        self.UserPromptSystem1 = ''
        self.UserPromptRole1 = ''
        self.UserPromptFormat1 = ''
        self.UserPromptTask1 = ''
        self.UserPromptBackground1 = ''
        self.UserPromptBackground21 = ''
        self.UserPromptBackground31 = ''
        self.UserPromptCrazy1 = ''
        self.UserPromptversion1 = ''

        try:
            self.UserPromptSystem = self.FrameText["System"].toPlainText()
            self.UserPromptSystem1 = "System: " + self.UserPromptSystem
        except:
            print('Error Getting User prompt System')

        try:
            #self.UserPromptRole = self.UserInput_fld_ROLE.get(1.0, END)
            self.UserPromptRole = self.FrameText["Role"].toPlainText()
            self.UserPromptRole1 = "Role: " + self.UserPromptRole
        except:
            print('Error Getting User prompt Role')

        try:
            #self.UserPromptFormat = self.UserInput_fld_FORMAT.get(1.0, END)
            self.UserPromptFormat = self.FrameText["Format"].toPlainText()
            self.UserPromptFormat1 = "Format: " + self.UserPromptFormat
        except:
            print('Error Getting User prompt Format')

        try:
            #self.UserPromptTask = self.UserInput_fld_TASK.get(1.0, END)
            self.UserPromptTask = self.FrameText["Task"].toPlainText()
            self.UserPromptTask1 = "Task: " + self.UserPromptTask
        except:
            print('Error Getting User prompt Task')

        try:
            #self.UserPromptBackground = self.UserInput_fld_Background.get(1.0, END)
            self.UserPromptBackground = self.FrameText["Background"].toPlainText()
            self.UserPromptBackground1 = "Background : " + self.UserPromptBackground
        except:
            print('Error Getting User prompt Background')

        try:
            # self.UserPromptBackground2 = self.UserInput_fld_Background2.get(1.0, END)
            self.UserPromptBackground2 = self.FrameText["Background2"].toPlainText()
            self.UserPromptBackground21 = "Background 2: " + self.UserPromptBackground2
        except:
            print('Error Getting User prompt Background2')

        try:
            #self.UserPromptBackground3 = self.UserInput_fld_Background3.get(1.0, END)
            self.UserPromptBackground3 = self.FrameText["Background3"].toPlainText()
            self.UserPromptBackground31 = "Background 3: " + self.UserPromptBackground3
        except:
            print('Error Getting User prompt Background3')

        try:
            # self.UserPromptCrazy = self.UserInput_fld_Crazy.get(1.0, END)
            self.UserPromptCrazy = self.FrameText["Crazy"].toPlainText()
            self.UserPromptCrazy1 = "Crazy: " + self.UserPromptCrazy

        except:
            print('Error Getting User prompt Crazy')



        self.Full_User_Prompt2 = self.UserPromptSystem + self.UserPromptRole + self.UserPromptFormat + self.UserPromptTask + self.UserPromptBackground + self.UserPromptBackground2 + self.UserPromptBackground3

        self.Full_User_Prompt = self.UserPromptSystem1 + self.UserPromptRole1 + self.UserPromptFormat1 + self.UserPromptTask1 + self.UserPromptBackground1 + self.UserPromptBackground21 + self.UserPromptBackground31

        self.CountCharacters = len(self.Full_User_Prompt2)
        self.CountWords = cu.WordCount(self.Full_User_Prompt2)

    def UpdatePrompts1(self, Mode=44):
        d = 1
        # TextEdit.GetPrompts(self)
        self.WindowClose2 = True
        CustomWindow11.UserResponse(self, Mode, UIversion=2)
        # self.UserEdits = "8"
        return "44"

    def RestorePrompt_original(self, Mode=14):

        CustomWindow11.UserResponse(self, Mode, UIversion=2)

        return "14"

    def RestorePrompt(self, Mode=13):

        CustomWindow11.UserResponse(self, Mode, UIversion=2)

        return "13"

    def OPTIMIZEPROMPT(self, Mode=2002):

        CustomWindow11.UserResponse(self, Mode, UIversion=2)

        return "2002"

    def ChangeVersion(self, Mode=2000):

        CustomWindow11.UserResponse(self, Mode, UIversion=2)
        # self.version

        return 2000

    def Speak2(self, Mode=9, Text= ''):
        try:
            try:
                try:
                    CustomWindow11.GetPrompts(self)
                    self.Speak_Text = self.Full_User_Prompt
                    CustomWindow11.UserResponse(self, Mode, UIversion=2)
                    #t = threading.Thread(target=cu.speak, args=(Text,)).start()
                    # threads.append(t)
                except:
                    print("Error While trying to read outloud")
            except:
                print("Error While trying to read outloud #2")
        except:
            print("Error While trying to read outloud #3")

        self.UserEdits = "9"
        return "9"

    def UpdateUI(self):

        d = 1
    def closeWindow(self):
        # Add your custom logic here, if needed
        # For example, save any unsaved data or perform cleanup tasks
        # Then close the window
        self.close()

    def KeepRunning_Button(self):
        # self.window.quit
        self.WindowClose = True
        self.WindowClose2 = True
        self.UserResponseProvided = True
        self.UserResponseProvided2 = True



    def WindowSetUp(self,Type= "GPT", GPTResponse = '', UserEdits = '', System = '', Role= '', Task= '', Format= '', Background= '', Background2= '', Background3= '', Crazy= .5):

        #self.GPTResponse = "Default text 1"
        self.main_buttons1 = ["Continue", "Cancel", "ReGenerate", "ReGenerate with Edit", "ReWrite Edit" , "Review Prompts",	"SPEAK","ALL", "BIG", "MEDIUM", "SMALL"]
        self.main_buttons2 = ["Continue", "Cancel", "<", ">", "SAVE ALL", "OG","SPEAK"]


        self.FrameButtons_User = ["<", ">", "OG", "Save", "Generate", "Regenerate", "Speak", "Speak Input"]
        self.FrameButtons_GPT = ["<", ">", "OG", "Save", "Generate", "Regenerate with Edit", "Rewrite with User Edits", "Use User Text", "Speak", "Speak Input"]
        self.FrameButtons2 = ["<", ">", "OG", "Save", "Speak", "Generate"]
        self.FrameButtons2.append("Optimize Prompt")
        CurrentTest = "Prompt Test1"

        self.WindowInfo1 = "Test1"
        self.WindowInfo2 = "Test2"


        if Type== "GPT":
            self.WindowName = "SHAINE"
            self.WindowSize = "large"
            self.internal_frame = [("GPT Response", GPTResponse, self.FrameButtons_GPT, [], "black"),("USER EDITS", UserEdits, self.FrameButtons_User, [], "lightgreen")]
            self.window_type = self.WindowInfo1
            self.main_buttons = self.main_buttons1
            self.window_info = [
            (self.WindowName,self.window_type , self.WindowSize,self.main_buttons,["ALL", "BIG", "MEDIUM", "SMALL"], self.internal_frame)]

        else:
            self.WindowName = "PROMPTS REVIEW"
            self.WindowSize = "large"
            self.window_type = self.WindowInfo1
            self.main_buttons = self.main_buttons2
            self.internal_frame =[("System", System, self.FrameButtons2, [], "lightyellow"),
                ("Role", Role, self.FrameButtons2, [], "lightpink"),
                ("Format", Format,  self.FrameButtons2, [], "green"),
                ("Task", Task, self.FrameButtons2, [], "lightgreen"),
                ("Background", Background, self.FrameButtons2, [], "lightblue"),
                ("Background2", Background2, self.FrameButtons2, [], "blue"),
                ("Background3", Background3, self.FrameButtons2, [], "purple"),("Crazy", Crazy, self.FrameButtons2, [], "yellow")]
            self.window_info = [(self.WindowName, self.window_type,self.WindowSize ,self.main_buttons,self.internal_frame)]

        # Create a separate thread to run the GUI
        #x = create_windows6(window_info=window_info)
        #gui_thread = threading.Thread(target=create_windows6, args=(window_info,))
        #gui_thread.start()

        return self.window_info




def create_windows6(window_info):
    app = QApplication([])
    windows = []

    for info in window_info:
        window = CustomWindow11(*info)
        windows.append(window)




    app.exec_()
    f = FALSE
    while(f ==False):
        d = 100
        f = window.getClose()





#
# import sys
# import threading
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel, QHBoxLayout, QStatusBar, QMenuBar, QMenu, QAction, QLineEdit
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# class WebBrowserWindow(CustomWindow11):
#     def __init__(self, window_title, window_type, window_size, internal_frames):
#         super().__init__(window_title, window_type, window_size, internal_frames)
#         self.web_view = None  # Add this line to initialize the web_view attribute
#
#     def setup_ui(self, internal_frames):
#         super().setup_ui(internal_frames)
#
#         # Create the URL bar
#         self.url_bar = QLineEdit()
#         self.url_bar.setPlaceholderText("Enter URL")
#         self.url_bar.returnPressed.connect(self.load_url)
#         self.statusBar.addPermanentWidget(self.url_bar)
#
#         # Create the web view frame
#         self.web_view = QWebEngineView()
#         self.web_view.load(QUrl("https://www.you.com"))
#         self.setCentralWidget(self.web_view)
#
#
#         # Create the back button
#         back_button = QPushButton("Back")
#         back_button.clicked.connect(self.web_view.back)
#         self.statusBar.addPermanentWidget(back_button)
#
#         # Create the forward button
#         forward_button = QPushButton("Forward")
#         forward_button.clicked.connect(self.web_view.forward)
#         self.statusBar.addPermanentWidget(forward_button)
#
#         # Create the refresh button
#         refresh_button = QPushButton("Refresh")
#         refresh_button.clicked.connect(self.web_view.reload)
#         self.statusBar.addPermanentWidget(refresh_button)
#
#
#
#     def load_url(self):
#         url = self.url_bar.text()
#         if not url.startswith("http://") and not url.startswith("https://"):
#             url = "http://" + url
#         self.web_view.load(QUrl(url))
#
# # Function to create the web browser window
# def create_web_browser_window():
#     app = QApplication([])
#     app.setAttribute(Qt.AA_ShareOpenGLContexts, True)
#     web_browser_window = WebBrowserWindow("Web Browser", "Web Browser", "large", [])
#     web_browser_window.show()
#     app.exec_()

# Create a separate thread to run the web browser window





#I need to be able to call the class specifically so this needs to be in the code, and I need to be able to pull values from the respective text fields.



import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame

class DynamicGUI(QMainWindow):
    def __init__(self, window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setWindowFlags(window_type | Qt.WindowTitleHint)
        self.setStyleSheet("background-color: lightgray;")
        self.resize(window_size[0], window_size[1])

        self.internal_frame_widgets = {}
        self.frame_data = {}

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(QLabel("Main Buttons: " + ", ".join(main_buttons)))
        main_layout.addWidget(QLabel("Main Checkboxes: " + ", ".join(main_checkboxes)))

        # Add logo image
        logo_label = QLabel()
        logo_pixmap = QPixmap(r"A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Extracted images\2024-02-15\Shane Show\Best\1111.png")
        logo_label.setPixmap(logo_pixmap)
        main_layout.addWidget(logo_label)

        for frame_config in internal_frames:
            frame_widget = self.create_frame(frame_config)
            main_layout.addWidget(frame_widget)

        continue_button = QPushButton("Continue")
        continue_button.clicked.connect(self.close_window)
        main_layout.addWidget(continue_button)

        self.setCentralWidget(main_widget)

    def create_frame(self, frame_config):
        frame_title, frame_text, frame_buttons, frame_checkboxes, frame_color = frame_config

        frame_widget = QFrame()
        frame_widget.setStyleSheet(f"background-color: {frame_color};")

        frame_layout = QVBoxLayout(frame_widget)
        frame_layout.addWidget(QLabel(frame_title))

        if frame_text:
            frame_layout.addWidget(QLabel(frame_text))

        for button_text in frame_buttons:
            button = QPushButton(button_text)
            button.clicked.connect(lambda _, btn_text=button_text: self.update_status_bar(btn_text))
            frame_layout.addWidget(button)

        for checkbox in frame_checkboxes:
            frame_layout.addWidget(QLabel(checkbox))

        self.internal_frame_widgets[frame_title] = frame_widget
        self.frame_data[frame_title] = {"frame_title": frame_title,
                                        "frame_text": frame_text,
                                        "frame_buttons": frame_buttons,
                                        "frame_checkboxes": frame_checkboxes,
                                        "frame_color": frame_color}

        return frame_widget

    def update_frame_data(self, frame_title, frame_title_new=None, frame_text=None, frame_buttons=None, frame_checkboxes=None, frame_color=None):
        frame_data = self.frame_data.get(frame_title, {})
        if frame_data:
            if frame_title_new is not None:
                frame_data["frame_title"] = frame_title_new

            if frame_text is not None:
                frame_data["frame_text"] = frame_text

            if frame_buttons is not None:
                frame_data["frame_buttons"] = frame_buttons

            if frame_checkboxes is not None:
                frame_data["frame_checkboxes"] = frame_checkboxes

            if frame_color is not None:
                frame_data["frame_color"] = frame_color

            self.frame_data[frame_title] = frame_data

    def get_frame_data(self, frame_title):
        return self.frame_data.get(frame_title, {})

    def update_status_bar(self, button_text):
        status_bar = QLabel(f"Button '{button_text}' Pressed")
        self.statusBar().addWidget(status_bar)

    def close_window(self):
        self.close()


class Worker(QThread):
    def __init__(self, window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames):
        super().__init__()
        self.window_title = window_title
        self.window_type = window_type
        self.window_size = window_size
        self.main_buttons = main_buttons
        self.main_checkboxes = main_checkboxes
        self.internal_frames = internal_frames
        self.dynamic_gui = None

    def run(self):
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(r"A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Extracted images\2024-02-15\Shane Show\Best\re should only be one person in your picture incorporate a train in your drawing.png"))
        self.dynamic_gui = DynamicGUI(self.window_title, self.window_type, self.window_size, self.main_buttons, self.main_checkboxes, self.internal_frames)
        self.dynamic_gui.show()
        sys.exit(app.exec_())

    def update_frame_data(self, frame_title, frame_title_new=None, frame_text=None, frame_buttons=None, frame_checkboxes=None, frame_color=None):
        if self.dynamic_gui:
            self.dynamic_gui.update_frame_data(frame_title, frame_title_new, frame_text, frame_buttons, frame_checkboxes, frame_color)

    def get_frame_data(self, frame_title):
        if self.dynamic_gui:
            return self.dynamic_gui.get_frame_data(frame_title)

    def close_window(self):
        if self.dynamic_gui:
            self.dynamic_gui.close()


if __name__ == "__main__":
    window_title = "Dynamic GUI"
    window_type = Qt.Window
    window_size = (600, 400)
    main_buttons = ["Button 1", "Button 2", "Continue"]
    main_checkboxes = ["Checkbox 1", "Checkbox 2"]
    internal_frames = [
        ("Internal Frame 1", "Some text for Frame 1", ["Frame 1 Button 1", "Frame 1 Button 2"], ["Frame 1 Checkbox 1", "Frame 1 Checkbox 2"], "lightblue"),
        ("Internal Frame 2", "Some text for Frame 2", ["Frame 2 Button 1", "Frame 2 Button 2"], ["Frame 2 Checkbox 1", "Frame 2 Checkbox 2"], "lightgreen")
    ]

    worker = Worker(window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames)
    worker.start()
