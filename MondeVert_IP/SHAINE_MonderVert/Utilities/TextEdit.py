import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
import threading
from tkinter import filedialog, messagebox
import time
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
def TextEdit2():
    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete("1.0", tk.END)
        with open(filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")


    window = tk.Tk()
    window.title("Simple Text Editor")

    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
    btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    frm_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()


class TextEdit():
    def __init__(self, Text= '', UserConfirm = False,Mode = 'Story'):
        d = 100
        self.UserResponseProvided = False
        self.UserConfirm = UserConfirm
        self.Text = Text




    def MakeWindow(self,Text= "",UserConfirm = False, WindowName = "SHAINE"):
        self.UserConfirm = UserConfirm
        self.Text = Text
        self.current_file = None
        self.window = tk.Tk()
        self.window.title(WindowName)
        self.text_widget = tk.Text(self.window)
        self.window.rowconfigure(0, minsize=1000, weight=1)
        self.window.columnconfigure(1, minsize=1000, weight=1)

        # window.rowconfigure(1, minsize=800, weight=1)


        #txt_edit2 = tk.Text(self.window)
        frm_buttons = tk.Frame(self.window, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(frm_buttons, text="Open", command=self.open_file)
        btn_save = tk.Button(frm_buttons, text="Save As...", command=self.save_file)
        btn_new = tk.Button(frm_buttons, text="New Window...", command=self.openNewWindow)
        btn_KeepRunning = tk.Button(frm_buttons, text="Keep Running", command=self.KeepRunning_Button)

        btn_open.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=1, column=1, sticky="ew", padx=5)
        btn_new.grid(row=2, column=1, sticky="ew", padx=5)
        btn_KeepRunning.grid(row=3, column=1, sticky="ew", padx=5)

        if self.UserConfirm == True:
            self.window.columnconfigure(2, minsize=1000, weight=1)
            btn_Continue = tk.Button(frm_buttons, text="Continue", command=self.Continue_Button)
            btn_SmallEdit = tk.Button(frm_buttons, text="Small Edit/Guidance", command=self.SmallEdit)
            btn_ReWriteWithEdit = tk.Button(frm_buttons, text="ReWrite with Edit", command=self.ReWriteWithEdit)
            btn_ReWrite = tk.Button(frm_buttons, text="ReWrite",command=self.ReWrite)
            btn_UseUserText = tk.Button(frm_buttons, text="Use Text provided", command=self.UseUserText)
            btn_NoMoreUserInputs_RuntoEnd = tk.Button(frm_buttons, text="No More User Inputs Run to End", command=self.EndUserInput)
            btn_Speak = tk.Button(frm_buttons, text="Speak Text", command=self.Speak)
            btn_Continue.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
            btn_SmallEdit.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
            btn_ReWriteWithEdit.grid(row=2, column=1, sticky="ew", padx=5)
            btn_ReWrite.grid(row=3, column=1, sticky="ew", padx=5)
            btn_UseUserText.grid(row=4, column=1, sticky="ew", padx=5)
            btn_NoMoreUserInputs_RuntoEnd.grid(row=5, column=1, sticky="ew", padx=5)
            btn_Speak.grid(row=6, column=1, sticky="ew", padx=5)
            self.UserInput = tk.Entry(self.window)
            self.UserInput.pack()
            self.UserInput.grid(row=0, column=2, sticky="nsew")

        frm_buttons.grid(row=0, column=1, sticky="ns")
        #self.text_widget.grid(row=1, column=2, sticky="nsew")


        #txt_edit.grid(row=0, column=1, sticky="nsew")
        self.Printtxt = tk.Text(self.window)
        self.Printtxt.insert(tk.END, self.Text)
        self.Printtxt.grid(column=0, row=0,sticky="nsew")

        menu_bar = tk.Menu(self.window)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menu_bar.add_cascade(label="File", menu=file_menu)




        # Edit menu
        # Add more options to the menu as needed
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
         # Help menu
        # Add more options to the menu as needed

        self.window.config(menu=menu_bar)
        self.text_widget = tk.Text(self.window)



        while self.UserResponseProvided ==False:
            self.window.mainloop()
            #time.sleep(1)


        return self.UserEdits


    def GetUserText(self):
        self.UserEdits = self.UserInput.get()
        return self.UserEdits

    def GetUserResponseMode(self):
        return self.UserResponseMode

    def GetUserResponseMain(self):
        self.UserConfirm = True
        TextEdit.MakeWindow(self)
        x = self.UserInput.get()
        try:
            self.window.destroy()
        except:
            print('Error With Window, continue, maybe look into later')
        return x

    def Continue_Button(self, Mode = 0):
        TextEdit.UserResponse(self,Mode)
        self.UserEdits = "0"
        return "0"

    def EndUserInput(self, Mode = 5):
        TextEdit.UserResponse(self,Mode)
        self.UserEdits = "5"
        return "5"

    def Speak(self, Mode = 6):
        try:
            Text = self.Text
            t = threading.Thread(target= cu.speak, args=(Text,)).start()
            #threads.append(t)
        except:
            print("Error While trying to read outloud")

        self.UserEdits = "6"
        return "6"




    def SmallEdit(self, Mode = 1):

        self.UserEdits = TextEdit.GetUserText(self)
        TextEdit.UserResponse(self,Mode)
        return "1"


    def ReWriteWithEdit(self, Mode = 2):

        self.UserEdits = TextEdit.GetUserText(self)
        TextEdit.UserResponse(self,Mode)
        return "2"

    def ReWrite(self, Mode = 3):
        TextEdit.UserResponse(self,Mode)
        self.UserEdits = "3"
        return "3"

    def UseUserText(self, Mode = 4):
        TextEdit.UserResponse(self,Mode)
        self.UserEdits = "4"
        return "4"




    def UserResponse(self, Mode):
        self.UserResponseMode = Mode
        # print(Mode)
        if Mode == 0:
            # print("Pass")
            c = 1
        self.UserResponseProvided = True
        try:
            self.window.destroy()
        except:
            print("Error Trying to close window")
        return Mode

    def GetUserResponse(self):
        return self.UserResponseMode


    def UpdateUI(self):

        d = 1


    def new_file(self):


        self.text_widget.delete("1.0", tk.END)
        self.current_file = None

    def openNewWindow(self):

        # Toplevel object which will
        # be treated as a new window

        self.txt_edit3 = tk.Text(self.window)
        self.txt_edit3.grid(row=0, column=2, sticky="nsew")

        newWindow = tk.Toplevel( self.window)

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        tk.Label(newWindow,
              text="This is a new window").pack()

    def KeepRunning_Button(self):
        sys.exit()
    def open_file(self):


        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, file.read())
        self.current_file = file_path

    def save_file(self):


        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
        else:
            self.save_file_as

    def save_file_as(self):


        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
        self.current_file = file_path

    def exit_editor(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            try:
                self.window.destroy()
            except:
                print("Error Trying to close window")

    def cut_text(self):
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text_widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.window.clipboard_clear()
        self.window.clipboard_append(selected_text)

    def copy_text(self):
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.window.clipboard_clear()
        self.window.clipboard_append(selected_text)

    def paste_text(self):
        text_to_paste = self.window.clipboard_get()
        self.text_widget.insert(tk.INSERT, text_to_paste)



