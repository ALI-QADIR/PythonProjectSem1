import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# Major functions of file manager

# open a file box window 
# when we want to select a file
def open_window():
    read = easygui.fileopenbox()
    return read

# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

# copy file function
def copy_file():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('confirmation', "Process Completed !")


# function to make a new folder
def make_folder(path):
    newFolder = 'New'
    if path == '':
        mb.showerror('Error!', 'Permission Error\nCannot make a folder here!!')
    else:
        path = os.path.join(path, newFolder)
        os.mkdir(path)
        mb.showinfo('confirmation', "Process Completed !")


'''def list_files():
    folderList = filedialog.askdirectory()
    sortList=sorted(os.listdir(folderList))       
    i=0
    print("Files in ", folderList, "folder are:")
    while(i<len(sortList)):
        print(sortList[i]+'\n')
        i+=1'''
