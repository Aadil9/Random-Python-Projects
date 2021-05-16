def cringe_writer():
    Options=int(input("Welcome to my Twitter Cringe Writer. \nThis program allows for multiple types of cringe writing. \nFor classic uppercase/lowercase cringe writing, type 1. \nFor writing between spaces, type 2.\n"))
    text=list(input("Input text to be manipulated: "))
    mid=[]
    counter=0
    if Options == 1:
        for i in text:
            counter+=1
            if counter%2==0:
                mid.append(i.upper())
            else:
                mid.append(i.lower())
        newtext1="".join(mid)
        print(newtext1)
        return
    if Options == 2:
        for i in text:
            mid.append(i+" ")
        newtext2="".join(mid)
        print(newtext2)
        return

cringe_writer()
