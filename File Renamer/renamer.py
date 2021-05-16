def renamer():
    import os
    path=input("Input the file path of the files you want to rename here: ")#This is the path you need to scan the files of
    rename=input("What would you like to rename the files to: ")
    j=int(input("What number do you want to start at: "))
    ext=input("Please input a file extension: ")
    os.chdir(path)#This is wherever you want Python to place the folder you've changed after the code is finished
    folder=os.scandir(path)#This scans the files in that path
    for i in folder:
        os.rename(i,rename+" "+str(j)+ext)
        j=j+1
    return "Completed"

renamer()
#Incomplete, I want it to:
##Start at a number and stop at a number
##Choose whether to use a number at all e.g. for changing file names without numbers in them
