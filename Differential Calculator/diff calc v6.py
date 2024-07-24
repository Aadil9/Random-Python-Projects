#need to add a few try/except conditions for variables/integers/strings
#now ready to convert sin,cos,tan into taylor series
#added a condition for if the coefficient to the variable is 0
#it's already able to do fractions

def Diff():
    terms=int(input("How many terms does your expression have? "))
    answer=""
    expressions=[]
    exceptions=0
    for i in range(1,terms+1):
        print("Expression No." + str(i) + ": ")
        trig=upper(input("is the term a trigonometric function (i.e. sin(x), cos(x), tan(x), etc)?(Y/N): "))
        if trig=="Y":
            
            
            
        variable=input("input the variable letter/symbol: ")
        coefficient=float(input("input the coefficient to the variable: "))
        power=float(input("input the power of the variable: "))
        derivative=0
        if power==0:
            expressions+=[str(coefficient)]
        elif coefficient==0:
            exceptions+=1
            pass
        else:
            derivative+=coefficient*power
            expressions+=[str(derivative)+variable+"^"+str(power-1)]
    for i in expressions:
        if i[0]=="-":
            answer+=(i)
        else:
            answer+="+"+(i)
    print(answer)
    if exceptions>0:
        print("one or more coefficients were zero and thus could not be differentiated")
    return

Diff()
