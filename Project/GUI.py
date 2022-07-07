from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb

from functools import partial

# project contributions
import EZMGRP  # Parv's Contribution
import EZMGRV  # Vaibhav's Contribution
# Tejasvee's Contribution is imported in EZMGRP

import easygui
import os

import win32con
from win32api import GetLogicalDriveStrings
from win32file import GetDriveType


def get_drives_list(drive_types=(win32con.DRIVE_REMOVABLE,)):
    drives_str = GetLogicalDriveStrings()
    _drives = [item for item in drives_str.split("\x00") if item]
    return [item[:2] for item in _drives if drive_types is None or GetDriveType(item) in drive_types]


def srt(path):
    method = sortVar.get()
    lst = EZMGRP.sort_alpha(path, method)
    if lst:
        return create_button(lst)
    else:
        return button_click(goBack)


def filedel():
    read = easygui.fileopenbox()
    return EZMGRP.deleet(read)


def folderdel():
    read = filedialog.askdirectory()
    return EZMGRP.deleet(read)


def filemove():
    read = easygui.fileopenbox()
    dest = filedialog.askdirectory()
    return EZMGRP.move(read, dest)


def foldermove():
    read = filedialog.askdirectory()
    dest = filedialog.askdirectory()
    return EZMGRP.move(read, dest)


def doreed(selection):
    read = easygui.fileopenbox()
    return EZMGRP.Reed(read, selection)


def dohide(selection):
    read = easygui.fileopenbox()
    return EZMGRP.Sus(read, selection)


def open_window_rename(name):
    read = easygui.fileopenbox()
    EZMGRP.Renem(read, name)
    return button_click(currDir)


def rename():
    top = Toplevel(height=200, width=350, bg='#2b2b2b')
    lbl = Label(top, text='Enter New Name', bg='#2b2b2b')
    lbl.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.8, relheight=0.15)
    e = Entry(top)
    e.place(anchor=N, relx=0.5, rely=0.4, relwidth=0.8)
    lbl2 = Label(top, text='Click OK to proceed to File Selection for Renaming', bg='#2b2b2b')
    lbl2.place(anchor=N, relx=0.5, rely=0.6, relwidth=0.9, relheight=0.15)
    btn = Button(top, text='OK', command=lambda: open_window_rename(e.get()), bg='grey')
    btn.place(anchor=N, relx=0.75, rely=0.8, relwidth=0.4)


def deleet():
    top = Toplevel(height=200, width=300, bg='#2b2b2b')
    btn1 = Button(top, text='Select a File to Delete', command=filedel, bg='grey')
    btn1.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2)
    btn2 = Button(top, text='Select a Folder to Delete', command=folderdel, bg='grey')
    btn2.place(anchor=N, relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2)


def move():
    top = Toplevel(height=200, width=300, bg='#2b2b2b')
    btn1 = Button(top, text='Select a File to Move', command=filemove, bg='grey')
    btn1.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2)
    btn2 = Button(top, text='Select a Folder to Move', command=foldermove, bg='grey')
    btn2.place(anchor=N, relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2)


def hide():
    top = Toplevel(height=200, width=300, bg='#2b2b2b')
    btn1 = Button(top, text='Select a File to Move', command=lambda: dohide(1), bg='grey')
    btn1.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2)
    btn2 = Button(top, text='Select a Folder to Move', command=lambda: dohide(2), bg='grey')
    btn2.place(anchor=N, relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2)


def reed():
    top = Toplevel(height=200, width=300, bg='#2b2b2b')
    btn1 = Button(top, text='Set a file to Read only', command=lambda: doreed(1), bg='grey')
    btn1.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2)
    btn2 = Button(top, text='Set a file to open', command=lambda: doreed(2), bg='grey')
    btn2.place(anchor=N, relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2)


def srt_ext():
    global currDir
    EZMGRP.sort_ext_(currDir)
    return button_click(currDir)


def clear():
    if fileFrame is not None:
        for widget in fileFrame.winfo_children():
            widget.destroy()
    return


def build(lst=None):
    global fileFrame, canvas, myScrollbar
    if fileFrame is not None and canvas is not None and myScrollbar is not None:
        fileFrame.destroy()
        myScrollbar.destroy()
        canvas.destroy()

    canvas = Canvas(fileFrameMain, bg='#2b2b2b', highlightthickness=0)
    canvas.place(anchor=W, relx=0.0, rely=0.5, relwidth=0.97, relheight=1.0)

    myScrollbar = ttk.Scrollbar(fileFrameMain, orient="vertical", command=canvas.yview)
    myScrollbar.place(anchor=W, relx=0.97, rely=0.5, relwidth=0.03, relheight=1.0)

    canvas.config(yscrollcommand=myScrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    if lst is not None:
        h = 30 * len(lst) + 10
    else:
        h = 380

    fileFrame = LabelFrame(canvas, bg='#2b2b2b', height=h)
    canvas.create_window((0, 0), window=fileFrame, anchor='nw')
    return


def update_main(lst):
    for ii in lst:
        ii.pack(padx=2, pady=1, fill='x')
    return


def create_button(lst):
    build(lst)
    buttonList = list()
    if lst:
        for ii in lst:
            temp = Button(fileFrame, text=ii, font=('Helvetica', 10), bg='grey')
            tempFunc = partial(button_click, ii)
            temp.config(command=tempFunc)
            buttonList.append(temp)
    else:
        t = '''\n\nNothing here\n*Cricket Noises\n\n'''
        buttonList.append(Label(fileFrame, text=t, font=('Courier New', 44), bg='grey'))
    return update_main(buttonList)


def button_click_frame(a):
    global goBack, currDir
    goBack, currDir = '', ''
    currDir = a
    try:
        os.listdir(a)
    except NotADirectoryError:
        return
    except PermissionError:
        mb.showinfo('Error', "The device is not ready: 'E:/''")
    else:
        lst = sorted(os.listdir(a))
        g = partial(EZMGRV.make_folder, currDir)
        newFolderButton.config(command=g)
        f = partial(srt, currDir)
        sortButton.config(command=f)
        h = partial(srt_ext)
        filterButton.config(command=h)
        print(lst)
        return create_button(lst)


def button_click(a):
    global goBack, currDir
    if currDir != a:
        goBack = currDir
        if currDir != '':
            if currDir[-1] == '/':
                currDir = currDir + a
            else:
                currDir = currDir + '/' + a
        else:
            currDir = a
    else:
        pass
    try:
        os.listdir(currDir)
    except NotADirectoryError:
        os.startfile(currDir)
        currDir = goBack
    except PermissionError:
        mb.showinfo('Error', "The device is not ready: 'E:/''")
    else:
        lst = sorted(os.listdir(currDir))
        g = partial(EZMGRV.make_folder, currDir)
        newFolderButton.config(command=g)
        f = partial(srt, currDir)
        sortButton.config(command=f)
        h = partial(srt_ext)
        filterButton.config(command=h)
        print(lst)
        return create_button(lst)


def drives():
    fixed = get_drives_list(drive_types=(win32con.DRIVE_FIXED,))
    cdrom = get_drives_list(drive_types=(win32con.DRIVE_CDROM,))
    removable = get_drives_list(drive_types=(win32con.DRIVE_REMOVABLE,))
    fixedDriveButtonList = dict()
    cdromDriveButtonList = list()
    removableDriveButtonList = list()
    for fix in fixed:
        fixedDriveButtonList[fix] = Button(panelFrameL, text=fix, font=('Helvetica', 14), bg='grey')
        tempFunc = partial(button_click_frame, fix + '/')
        fixedDriveButtonList[fix].config(command=tempFunc)
    for cd in cdrom:
        temp = Button(panelFrameL, text=cd, font=('Helvetica', 14), bg='grey')
        tempFunc1 = partial(button_click_frame, cd)
        temp.config(command=tempFunc1)
        cdromDriveButtonList.append(temp)
    for rem in removable:
        temp = Button(panelFrameL, text=rem, font=('Helvetica', 14), bg='grey')
        tempFunc2 = partial(button_click_frame, rem)
        temp.config(command=tempFunc2)
        removableDriveButtonList.append(temp)
    fixedDrive = Label(panelFrameL, text='Fixed Drives:', bg='#2b2b2b', font=('Courier New', 14))
    fixedDrive.pack(padx=4, pady=(4, 0))
    for key, value in fixedDriveButtonList.items():
        value.pack(padx=4, pady=(4, 4), fill='x')
    return [0, cdromDriveButtonList, removableDriveButtonList]


def main():
    clear()
    build()
    fixed = get_drives_list(drive_types=(win32con.DRIVE_FIXED,))
    cdrom = get_drives_list(drive_types=(win32con.DRIVE_CDROM,))
    removable = get_drives_list(drive_types=(win32con.DRIVE_REMOVABLE,))
    fixedDriveButtonList = dict()
    cdromDriveButtonList = list()
    removableDriveButtonList = list()
    for fix in fixed:
        fixedDriveButtonList[fix] = Button(fileFrame, text=fix, font=('Helvetica', 14), bg='grey')
    for cd in cdrom:
        temp = Button(fileFrame, text=cd, font=('Helvetica', 14), bg='grey')
        tempFunc1 = partial(button_click, cd)
        temp.config(command=tempFunc1)
        cdromDriveButtonList.append(temp)
    for rem in removable:
        temp = Button(fileFrame, text=rem, font=('Helvetica', 14), bg='grey')
        tempFunc2 = partial(button_click, rem)
        temp.config(command=tempFunc2)
        removableDriveButtonList.append(temp)
    fixed_Drive = Label(fileFrame, text='Fixed Drives:', bg='#2b2b2b', font=('Helvetica', 14))
    fixed_Drive.pack(padx=4, pady=4)
    for key, value in fixedDriveButtonList.items():
        value.pack(padx=4, pady=(4, 4), fill='x')
        tempFunc0 = partial(button_click, key + '/')
        value.config(command=tempFunc0)
    cd_Drive = Label(fileFrame, text='CD ROM:', bg='#2b2b2b', font=('Helvetica', 14))
    cd_Drive.pack(padx=4, pady=8, expand=1, fill='x')
    for ii in cdromDriveButtonList:
        ii.pack(padx=4, pady=4, expand=1, fill='x')
    removable_Drive = Label(fileFrame, text='Removable Drives:', bg='#2b2b2b', font=('Helvetica', 14))
    removable_Drive.pack(padx=4, pady=8)
    if not removableDriveButtonList:
        no_Removables = Label(fileFrame, text='No Removables', bg='grey', font=('Courier New', 14))
        no_Removables.pack(padx=4, pady=(4, 0), fill='x', expand=1)
    else:
        for ii in removableDriveButtonList:
            ii.pack(padx=4, pady=4, expand=1, fill='x')


if __name__ == '__main__':
    goBack = ''
    currDir = ''
    root = Tk()
    root.title('EZ Manager by OverwatchdedgameXD')
    root.geometry('900x450')
    root.resizable(False, False)

    mainFrame = LabelFrame(root, bg='#444444')
    mainFrame.pack(fill=BOTH, expand=1)
    topFrame = LabelFrame(mainFrame, bg='grey')
    topFrame.place(relheight=0.1, relwidth=1.0, anchor=N, relx=0.5, rely=0.0)
    text = Label(topFrame, text='EZ Manager by OverwatchdedgameXD', font=('Courier New', 18), fg='black', bg='grey')
    text.pack(padx=4, pady=4)

    # responsive designing
    bottomFrame = LabelFrame(mainFrame, bg='#2b2b2b')
    bottomFrame.place(relheight=0.9, relwidth=1.0, anchor=S, relx=0.5, rely=1.0)
    mainPanel = PanedWindow(bottomFrame, orient=HORIZONTAL, bd=2, bg='black')
    mainPanel.place(anchor=W, relx=0.0, rely=0.5, relheight=1.0, relwidth=1.0)

    # left frame in panel
    panelFrameL = LabelFrame(mainPanel, bg='#2b2b2b')
    mainPanel.add(panelFrameL)
    driveList = drives()
    cdDrive = Label(panelFrameL, text='CD ROM:', bg='#2b2b2b', font=('Courier New', 14))
    cdDrive.pack(padx=4, pady=8)
    for i in driveList[1]:
        i.pack(padx=4, pady=(4, 4), fill='x')
    removableDrive = Label(panelFrameL, text='Removable Drives:', bg='#2b2b2b', font=('Courier New', 14))
    removableDrive.pack(padx=4, pady=(8, 8))
    if not driveList[2]:
        noRemovables = Label(panelFrameL, text='No Removables', bg='grey', font=('Courier New', 14))
        noRemovables.pack(padx=4, pady=(4, 4), fill='x')
    else:
        for i in driveList[2]:
            i.pack(padx=4, pady=(4, 4), fill='x')

    # right frame in panel
    panelFrameR = Frame(mainPanel, bg='#2b2b2b')
    mainPanel.add(panelFrameR)

    # menu frame in right panel
    menuFrame = LabelFrame(panelFrameR, bd=2, bg='#2b2b2b')
    menuFrame.place(anchor=N, relwidth=1.0, relheight=0.1, relx=0.5, rely=0.0)

    newFolderButton = Button(menuFrame, text='New Folder', font=('Helvetica', 10), bg='grey')
    newFolderButton.place(anchor=W, relx=0.005, rely=0.5, relheight=0.9)

    renameButton = Button(menuFrame, text='Rename', font=('Helvetica', 10), bg='grey')
    renameButton.place(anchor=W, relx=0.12, rely=0.5, relheight=0.9)
    renameButton.config(command=rename)

    copyButton = Button(menuFrame, text='Copy', font=('Helvetica', 10), bg='grey')
    copyButton.place(anchor=W, relx=0.22, rely=0.5, relheight=0.9)
    copyButton.config(command=EZMGRV.copy_file)

    moveButton = Button(menuFrame, text='Move', font=('Helvetica', 10), bg='grey')
    moveButton.place(anchor=W, relx=0.29, rely=0.5, relheight=0.9)
    moveButton.config(command=move)

    deleteButton = Button(menuFrame, text='Delete', font=('Helvetica', 10), bg='grey')
    deleteButton.place(anchor=W, relx=0.36, rely=0.5, relheight=0.9)
    deleteButton.config(command=deleet)

    HideButton = Button(menuFrame, text='Hide', font=('Helvetica', 10), bg='grey')
    HideButton.place(anchor=W, relx=0.44, rely=0.5, relheight=0.9)
    HideButton.config(command=hide)

    reedButton = Button(menuFrame, text='Read Only', font=('Helvetica', 10), bg='grey')
    reedButton.place(anchor=W, relx=0.52, rely=0.5, relheight=0.9)
    reedButton.config(command=reed)

    filterButton = Button(menuFrame, text='Sort(ext)', font=('Helvetica', 10), bg='grey')
    filterButton.place(anchor=E, relx=0.995, rely=0.5, relheight=0.9)

    sortButton = Button(menuFrame, text='Sort:', font=('Helvetica', 10), bg='grey', fg='black')
    sortButton.place(anchor=E, relx=0.7, rely=0.5, relheight=0.9)
    sortVar = StringVar()
    sortVar.set('---SELECT--- ')
    sortOptions = OptionMenu(menuFrame,
                             sortVar,
                             'Name- A to Z',
                             'Name- Z to A',)
    sortOptions.place(anchor=W, relx=0.7, rely=0.5, relheight=0.9)
    sortOptions.config(bg='grey')
    sortOptions['menu'].config(bg='grey')

    # files frame in right panel
    fileFrameMain = LabelFrame(panelFrameR, bd=2, bg='#2b2b2b')
    fileFrameMain.place(anchor=N, relx=0.5, rely=0.1, relheight=0.9, relwidth=1.0)

    # defining variables
    canvas = None
    myScrollbar = None
    fileFrame = None
    '''
    canvas = Canvas(fileFrameMain, bg='#2b2b2b')
    canvas.pack(side=LEFT, expand=1, fill=BOTH)

    myScrollbar = ttk.Scrollbar(fileFrameMain, orient="vertical", command=canvas.yview)
    myScrollbar.pack(side=RIGHT, fill='y')
    canvas.configure(yscrollcommand=myScrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    fileFrame = Frame(canvas, bg='#2b2b2b')
    canvas.create_window((0, 0), window=fileFrame, anchor='nw')'''

    if goBack == '':
        main()
    root.mainloop()
