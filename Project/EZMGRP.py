import os
import shutil
import stat
# Tejasvee's contributtion is imported in line 169

from send2trash import send2trash
from tkinter import messagebox as mb


def sort_alpha(path, method):
    #Sort Alphabetically
    files = os.listdir(path)
    print(path, method)
    if method == 'Name- Z to A':
        for i in range(len(sorted(files))):
            return sorted(files, reverse=True)
    elif method == 'Name- A to Z':
        for i in range(len(sorted(files))):
            return sorted(files, reverse=False)
    else:
        mb.showerror('Error', 'Please select a sort method!!')

def sort_ext_(path):
    #Finding extensions through ext and listing files using files
    ext, files = [], os.listdir(path)
    for i in files:
        if os.path.splitext(i)[1] in ext:
            #making sure no over-write
            pass
        else:
            ext.append(os.path.splitext(i)[1])
    if "" in ext:
        #removing the folder extension " "
        ext.remove("")
    for i in ext:
        #printing extensions
        print(i)
    #listing source
    Source = path
    for i in ext:
        #making the dir's
        try:
            #Videos
            if i == ".mp4" or i == ".mkv":
                i = r"Videos"
                path = os.path.join(Source, i)
                os.mkdir(path)

            #Images
            elif i == ".png" or i == ".webm" or i == ".jpg" or i == ".jpeg" or i == ".gif" or i == ".jfif":
                i = r"Images"
                path = os.path.join(Source, i)
                os.mkdir(path)

            #Skipping INI
            elif i == ".ini":
                pass

            #Music
            elif i == ".mp3" or i == ".wav" or i == ".mpeg":
                i = r"Music"
                path = os.path.join(Source, i)
                os.mkdir(path)

            #Zipped Files
            elif i == ".zip" or i == ".7z" or i == ".rar":
                i = r"Zipped"
                path = os.path.join(Source, i)
                os.mkdir(path)

            #Readable
            elif i == ".mobi" or i == ".pdf" or i == ".txt":
                i = r"Readable"
                path = os.path.join(Source, i)
                os.mkdir(path)

            #Executable
            elif i == ".exe":
                i = r"Executable"
                path = os.path.join(Source, i)
                os.mkdir(path)

            #Other Stuff
            else:
                path = os.path.join(Source, i)
                os.mkdir(path)

        #Error Handling
        except FileExistsError:
            print("{} Folder Already Exists".format(i))
    #SORTING
    for i in files:
        e = os.path.splitext(i)[1]
        if e == "":
            pass
        else:
            for j in ext:
                if j in i:
                    #Images
                    if j == ".png" or j == ".webm" or j == ".jpg" or j == ".jpeg" or j == ".gif" or j == ".jfif":
                        j = r"Images"
                        Dest = os.path.join(Source, j)
                        #print("Dest",Dest, "SRC", Source, "\nJ", j)
                        shutil.move(Source + "\\" + i, Dest)

                    #Videos
                    elif j == ".mp4" or j == ".mkv":
                        j = r"Videos"
                        Dest = os.path.join(Source, j)
                        #print("Dest", Dest, "SRC", Source, "\nJ", j)
                        shutil.move(Source + "\\" + i, Dest)

                    #Music
                    elif j == ".mp3" or j == ".wav" or j == ".mpeg":
                        j = r"Music"
                        Dest = os.path.join(Source, j)
                        #print("Dest", Dest, "SRC", Source, "\nJ", j)
                        shutil.move(Source + "\\" + i, Dest)

                    #Zipped
                    elif j == ".zip" or j == ".7z" or j == ".rar":
                        j = r"Zipped"
                        Dest = os.path.join(Source, j)
                        #print("Dest", Dest, "SRC", Source, "\nJ", j)
                        shutil.move(Source + "\\" + i, Dest)

                    #Skipping INI
                    elif j == ".ini":
                        pass

                    #Readables
                    elif j == ".pdf" or j == ".mobi" or j == ".txt":
                        j = r"Readable"
                        Dest = os.path.join(Source, j)
                        #print("Dest", Dest, "SRC", Source, "\nJ", j)
                        shutil.move(Source + "\\" + i, Dest)

                    #Executable
                    elif j == ".exe":
                        j = r"Executable"
                        Dest = os.path.join(Source, j)
                        #print("Dest", Dest, "SRC", Source, "\nJ", j, i)
                        shutil.move(Source + "\\" + i, Dest)

                    #Others
                    else:
                        Dest = os.path.join(Source, j)
                        #print("Dest",Dest, "SRC", Source, "\nJ", j)
                        shutil.move(Source+"\\"+i, Dest)
    return

def move(src, dest):
    # src, dest = r"C:\Users\Xx_Poy517us_xX\Desktop\Lol", r"C:\Users\Xx_Poy517us_xX\Desktop\kekw"
    try:
    #Checking if dest is folder or not
        files_dest = os.listdir(dest)
    except NotADirectoryError:
        mb.showwarning('Warning', 'Enter a directory NOT a file !!!')

    try:
    #To transfer if input is folder
        files_src = os.listdir(src)
        for i in files_src:
            shutil.move(src+"\\"+i, dest)
    except NotADirectoryError:
    #To transfer if input is a file
        shutil.move(src, dest)
    finally:
        # importing Tejasvee's contribution
        import CS_PROJECT
        CS_PROJECT.main()
        mb.showinfo('Confirmation', 'Process Completed !')
    return

def deleet(src):
    flag = 0
    try:
        abc = os.listdir(src)
    except NotADirectoryError:
        flag = 1
    if flag == 1:
        send2trash(src)
    elif flag == 0:
        send2trash(src)
    import CS_PROJECT
    CS_PROJECT.main()
    mb.showinfo('Deleted', "Yeeted Your File!!!")
    return

def Renem(src, name, ext = "1"):
    if os.path.isdir(src):
        old_dir = os.path.dirname(src)
        new_dir = old_dir + "\\" + name
        # print(old_dir, new_dir, src)
        os.rename(src, new_dir)
    else:
        old_dir = os.path.dirname(src)
        if ext == "1":
            new_dir = old_dir + "\\" + name + os.path.splitext(src)[1]
            # print(src, old_dir, new_dir)
            os.rename(src, new_dir)
        else:
            new_dir = old_dir + "\\" + name + ext
            os.rename(src, new_dir)
    mb.showinfo('confirmation', "Process Completed !")
    return

def Sus(src, selection):
    abc = bool(os.stat(src).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
    print("File is currently hidden:", abc)
    y = selection
    if abc == True and y == 1:
        print("Already Hidden")
    elif abc == False and y == 2:
        print("Already Public")
    elif abc == False and y == 1:
        p = os.popen('ATTRIB +H ' + src)
        t = p.read()
        p.close()
    elif abc == True and y == 2:
        p = os.popen('ATTRIB -H ' + src)
        t = p.read()
        p.close()

def Reed(src, selection):
    abc = bool(os.stat(src).st_file_attributes & stat.FILE_ATTRIBUTE_READONLY)
    print("File is currently Read-Only:", abc)
    y = selection
    if abc == True and y == 1:
        print("Already Read-Only")
    elif abc == False and y == 2:
        print("Already Open")
    elif abc == False and y == 1:
        p = os.popen('ATTRIB +R ' + src)
        t = p.read()
        p.close()
    elif abc == True and y == 2:
        p = os.popen('ATTRIB -R ' + src)
        t = p.read()
        p.close()

#__main__
if __name__=='__main__':
    x = int(input("""What do you want to do: 
    1 = Sort by extension at location 
    2 = Sort by alphabets at location 
    3 = move file from x to y
    4 = delete file or folder
    5 = Rename a File or Folder
    6 = Hide/Unhide File/Folder
    7 = ReadOnly/ReadAndWrite File/Folder
    :"""))
    if x == 1:
        path = str(input(r"Enter Location"))
        sort_ext_(path)
    elif x == 2:
        path = str(input("Enter Location"))
        method = int(input("1 = UP \n2 = DOWN \n:"))
        sort_alpha(path, method)
    elif x == 3:
        src = str(input(r"Enter Source File/Folder:"))
        dest = str(input(r"Enter Destination Folder:"))
        move(src, dest)
    elif x == 4:
        src = str(input(r"Enter File/Folder to be deleted:"))
        deleet(src)
    elif x == 5:
        src = str(input(r"Enter source file/folder:"))
        name = str(input(r"Enter New name:"))
        if os.path.isdir(src):
            Renem(src, name)
        else:
            ext = str(input(r"Enter 1 if you want same ext or else enter new extension:"))
            Renem(src, name, ext)
    elif x == 6:
        src = str(input(r"Enter file/folder"))
        Sus(src, 1)
    elif x == 7:
        src = str(input(r"Enter file/folder"))
        Reed(src, 1)
    print("Done")
