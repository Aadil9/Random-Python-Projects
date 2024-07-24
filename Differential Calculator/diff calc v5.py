#taylor series?
#will need to be able to differentiate multiple expressions for that
#can't split across operators, will probably just ask to input however many expressions
#need to somehow need to make it so that my formula ask for expressions the same amount of times as the integer entered by user
#i.e. if terms = 3, the formula needs to ask for 3 different expressions
#successfully made it so that it can differentiate multiple terms
#Need to remember to make sure to set up error catches: variable not being a string, coefficient and power having letters, terms not being a string, etc
#Need to make it so that in generating the final answer the for loop can detect whether or not to put a +, or if there is a -, turn the term into a - 
#done that, now ready to convert sin,cos,tan into taylor series




def Diff():
    terms=int(input("How many terms does your expression have? "))
    answer=""
    expressions=[]
    for i in range(1,terms+1):
        print("Expression No." + str(i) + ": ")
        variable=input("input the variable letter/symbol: ")
        coefficient=float(input("input the coefficient to the variable: "))
        power=float(input("input the power of the variable: "))
        derivative=0
        if power==0:
            expressions+=[coefficient]
        else:
            derivative+=coefficient*power
            expressions+=[str(derivative)+variable+"^"+str(power-1)]
    for i in expressions:
        if i[0]=="-":
            answer+=i
        else:
            answer+="+"+i
    print(answer)
    print(expressions)
    return

Diff()
2