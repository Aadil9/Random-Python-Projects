#Decided to go with inputting variables, coefficients and powers to make up the expression myself
#currently just trying for 1 term that is not a constant
#and perhaps only positive? maybe negative ints as well
#I got ahead of the curve a little and float'd insteading of int'ing
#There's a way to make a superscript map to help actually write out powers, but that's not important right now:https://stackoverflow.com/questions/8651361/how-do-you-print-superscript-in-python

#Below works for 1 term with positive and negative floats, with 1 variable and any digits - huge success
#can build on this for added features
#need to work on e's, natural logs and trig functions next

#The thing about trig functions is that the math module has the trig functions already.
#However, the math module probably also just has a derivative calculator. 
#The question is: am I allowed to use the math module or should I create the trig functions like just like the derivative calculator?

#taylor series?
#will need to be able to differentiate multiple expressions for that


def Diff():
    variable=input("input the variable letter/symbol: ")
    coefficient=float(input("input the coefficient to the variable: "))
    power=float(input("input the power of the variable: "))
    derivative=0
    if power==0:
        print(0)
        return
    else:
        derivative+=coefficient*power
    answer=str(derivative)+variable+"^"+str(power-1)
    print(answer)
    return

Diff()

