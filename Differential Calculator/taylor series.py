#need to make the taylor series sum iterable
#start with cosx
#maybe make it its own function?
#can't do a sum, it must be an expression so that each term can be differentiated
#currently, the big problem is doing a factorial - sum(range()) doesnt work 
#I don't want to have to use the math module, but there's no product function. make a special exception?

#Got factorials to work, need to sort out the factorial integration
#Currently, the problem is that the facotorial() function starts from the beginning for every i
#therefore always giving the biggest number factorial divising each element of the list
#probably need to remove the factorial function and instead create facto in the for loop

#factorial needs to only be factorial even numbers - in the same loop as the coefficient assigning loop?
#couple ways i can do this - append 2*terms2 to a list and pick only the even entries, etc
#however, I'd rather avoid list based work here if possible - I'd rather it be cleaner
#don't think it's possible yet, or I'm unsure how to do it, so I'm going with the list option with 2 for loops :(

#Signage and cos taylor series is correct except for 0 somehow, need to look into that next
#doesnt work for 0 because 2*1-1 = -1 and =/= 0 lol - fixed
#need to make sure the output can add a + or - depending on sign, might need to change where the cos variable is
#could probably make this way more efficient and neat

#Done with cosx from the taylor series
#sinx should be simple from here, just need to change the conditions for the 2nd loop
#need to think about how i'm going to integrate this into the derivative calc
#don't need necessarily have the cos variable because each coefficient needs to be differentiated 
#first things first, Sin, then tan then the cos variable


def trig():
    choice=int(input("Choose 1 for Cos(), 2 for Sin() and 3 for Tan(): "))
    if choice==1:
        terms2=int(input("how many terms of the taylor series for Cos() do you want?: "))
    elif choice==2:
        terms2=int(input("how many terms of the taylor series for Sin() do you want?: "))
    else:
        terms2=int(input("how many terms of the taylor series for Tan() do you want?: "))
    variable=(input("input the variable letter/symbol: "))
    trig=""
    coefficient=[]
    facto=1
    factorial_list=[]
    for n in range(0,2*(terms2+1)):
        if n>0:
            facto*=n
            factorial_list.append(facto)
    if choice==1:
        for i in range(0,terms2+1):
            if i==0:
                coefficient+=[str(1)]
            elif i%2==0:
                coefficient+=["+"+str((-1)**i/factorial_list[(2*i)-1])]
            else:
                coefficient+=[str((-1)**i/factorial_list[(2*i)-1])]
            trig+=coefficient[i]+str(variable)+"^"+str(2*i)
    elif choice==2:
        trig+="x-"
        for i in range(0,terms2+1):
            if i%2==1:
                coefficient+=["+"+str((-1)**i/factorial_list[(2*i)])]
            else:
                coefficient+=[str((-1)**i/factorial_list[(2*i)])]
            trig+=coefficient[i]+str(variable)+"^"+str(2*i+1)
    print(trig)
    print(coefficient)
    print((factorial_list))
    return

trig()
