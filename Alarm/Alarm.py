def alarm():
    import os
    import datetime
    path=' '# Let path be the path to any file you want as an alarm sound (e.g. the path to a bell ringing sound on your pc)
    Hour=int(input("Hour of the alarm (24 hour clock): "))
    Minute=int(input("Minute of the alarm: "))
    Succ=False
    while True:
        now=datetime.datetime.now().time()
        if now.hour == Hour and now.minute == Minute:
            Succ=True
            os.startfile(path)
            break

alarm()
