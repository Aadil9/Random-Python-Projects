

def File_Mover():
    import os
    import shutil

    source=input("Input the file path of the folder in which the files are: ")
    dest=input("Input the file path of the files you want to move to: ")
    ext=input("Input the type of file you want to move (e.g. .mp4 or .txt): ")

    delete=int(input("Do you want to delete the rest of the files in the folder after use? \nEnter 1 for 'Yes' or enter anything else for 'No': ")) #an option to delete empty files or what ever else is left in the folder
    delete_counter=0
    file_counter=0
    for x,y,z in os.walk(source): #os.walk generates 3 tuples, the current path (x), all of the directories/folders in the current path (y) and all of the files in each of the directories/folders in the current path (z)
        #print(z)    #this would print all of the filenames in each folder inside the current path
        for i in z:
            if i.endswith(ext):
                try:
                    shutil.move(os.path.join(x,i),dest)
                    file_counter+=1
                except:
                    pass
                

    for x,y,z in os.walk(source):
        if delete == 1:
            for i in y:
                shutil.rmtree(os.path.join(x,i))
                delete_counter+=1
                
    print("Number of items moved: "+str(file_counter))
    print("Number of items deleted: "+str(delete_counter))
    return

File_Mover()
