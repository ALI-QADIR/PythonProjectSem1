from tkinter import *
import EZMGRP
import EZMGRV
import easygui
from tkinter import filedialog


def open_window_rename(name):
    read = easygui.fileopenbox()
    return EZMGRP.Renem(read, name)


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


def srt(method):
    read = filedialog.askdirectory()
    lst = EZMGRP.sort_alpha(read, method)
    top = Toplevel(height=400, width=400, bg='#2b2b2b')
    listbox = Listbox(top, bg='#2b2b2b')
    listbox.grid(row=0, column=0)
    scrollbar = Scrollbar(top)
    scrollbar.grid(row=0, column=1)

    for i in range(len(lst)):
        listbox.insert(i, lst[i])

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)


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


def extsort():
    read = filedialog.askdirectory()
    return EZMGRP.sort_ext_(read)


def sortalpha():
    top = Toplevel(height=200, width=300, bg='#2b2b2b')
    lbl = Label(top, text='Select Order:')
    lbl.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.8, relheight=0.15)
    btn1 = Button(top, text='Ascending', command=lambda: srt(2), bg='grey')
    btn1.place(anchor=N, relx=0.25, rely=0.6, relwidth=0.4)
    btn2 = Button(top, text='Descending', command=lambda: srt(1), bg='grey')
    btn2.place(anchor=N, relx=0.75, rely=0.6, relwidth=0.4)


def newfolder():
    top = Toplevel(height=200, width=300, bg='#2b2b2b')
    lbl = Label(top, text='Enter name for New Folder', bg='#2b2b2b')
    lbl.place(anchor=N, relx=0.5, rely=0.2, relwidth=0.8, relheight=0.15)
    e = Entry(top)
    e.place(anchor=N, relx=0.5, rely=0.4, relwidth=0.8)
    lbl2 = Label(top, text='Click OK to proceed to Folder Selection', bg='#2b2b2b')
    lbl2.place(anchor=N, relx=0.5, rely=0.6, relwidth=0.8, relheight=0.15)
    btn = Button(top, text='OK', command=lambda: EZMGRV.make_folder(e.get()), bg='grey')
    btn.place(anchor=N, relx=0.75, rely=0.8, relwidth=0.4)


if __name__ == '__main__':
    root = Tk()
    root.title('EZ Manager by OverwatchdedgameXD')
    root.geometry('450x450')

    mainFrame = LabelFrame(root, bg='#2b2b2b')
    mainFrame.pack(fill=BOTH, expand=1)
    topFrame = LabelFrame(mainFrame, bg='grey')
    topFrame.place(relheight=0.1, relwidth=1.0, anchor=N, relx=0.5, rely=0.0)
    text = Label(topFrame, text='EZ Manager by OverwatchdedgameXD', font=('Times New Roman', 18), bg='grey')
    text.pack(padx=4, pady=4)
    subFrame = LabelFrame(mainFrame, bg='#2b2b2b')
    subFrame.place(relheight=0.9, relwidth=1.0, anchor=N, relx=0.5, rely=0.1)

    sortAlphaB = Button(subFrame, text='Sort by Alphabets', command=sortalpha, bg='grey')
    sortAlphaB.place(anchor=N, relx=0.5, rely=0.05, relheight=0.1, relwidth=0.3)
    sortExtB = Button(subFrame, text='Sort by Extension', command=extsort, bg='grey')
    sortExtB.place(anchor=N, relx=0.5, rely=0.15, relheight=0.1, relwidth=0.3)
    moveB = Button(subFrame, text='Move Files/Folders', command=move, bg='grey')
    moveB.place(anchor=N, relx=0.5, rely=0.25, relheight=0.1, relwidth=0.3)
    deleteB = Button(subFrame, text='Delete Files/Folders', command=deleet, bg='grey')
    deleteB.place(anchor=N, relx=0.5, rely=0.35, relheight=0.1, relwidth=0.3)
    renameB = Button(subFrame, text='Rename Files', command=rename, bg='grey')
    renameB.place(anchor=N, relx=0.5, rely=0.45, relheight=0.1, relwidth=0.3)
    newFolderB = Button(subFrame, text='New Folder', command=newfolder, bg='grey')
    newFolderB.place(anchor=N, relx=0.5, rely=0.55, relheight=0.1, relwidth=0.3)
    copyB = Button(subFrame, text='Copy', command=EZMGRV.copy_file, bg='grey')
    copyB.place(anchor=N, relx=0.5, rely=0.65, relheight=0.1, relwidth=0.3)
    quitB = Button(subFrame, text='Quit', command=root.quit, bg='grey')
    quitB.place(anchor=N, relx=0.5, rely=0.75, relheight=0.1, relwidth=0.3)

    root.mainloop()
# canvas.place(anchor=W, relx=0.0, rely=0.5, relheight=1.0) for gui.py
