
#below is me working on any number of digits before and after the variable x
#this one works for any digits beore the variable but not for the more than 1 digit powers
#I don't know why it doesn't work for more than 1digit powers. Even if i can fix it, the best case scenario is 2 digits. 
#That's not good enough

def Diff():
    x=input("input a number e.g.: 2x^2: ")
    a=""
    b=""
    c=""
    counter=0
    for i in x:
        counter+=1
        try:
            int(i)
            #has to be done so that i can iterate through x and see if there's a type(i) == string before the current indexed i so that i can add it to c
            #don't need to iterate
            try:
                (int(x[counter-2]))
                a+=i
            except:
                c+=i
        except:
            b+=i
    print([a,b,c])
    abc=str(int(a)*int(c))+str(b)+str(int(c)-1)
    print(abc)
    return

Diff()