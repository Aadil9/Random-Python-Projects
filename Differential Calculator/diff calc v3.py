#Could probably try to get it to work universally with numbers using if/if else/else statements instead of trys
#works with if statements
#Differential Calc now works for 1 expression
#can't do negatives lol
#I think the next step might be to remove the input function. Altough its useful, stringing integers first may not be the best way to do this.
#Although, I'm not sure how I would include the variable x. If x was included in the function (e.g. diff(12x)) python would automatically consider this a string
#Without raw integers, negatives and positives can't be distinguished without a lot more work.

#For now I'm thinking leave it as inputs, split by [-,+] (will need more thought for * and /) and then do an if + while loop on c being at 2 elements max. 
#This wont work for multiple expressions yet as C will probably need to be a list and negative integers will get split out too
#better yet, will have to create for loops for new "c" string holder variables depending on the number of items in the split list, then add those new "c"s depending
#on where we're at in the

#Could ask users to input their variable, input their coefficients, input their powers and input whether there's more than 1 expression or not.
#This would heavily simplify the process, and this way I could int() the numbers without the trouble

#Currently still unsure about what to do for quotient rule, chain rule, product rule, logs, natural logs, trigonometric functions

def Diff():
    x=input("input a number in the form [X]x^[Y], where X and Y can be any digit, positive integers: ")
    a=""
    b=""
    c=""
    for i in x:
        try:
            int(i)
            if b != "":
                c+=i
            else:
                a+=i
        except:
            b+=i
    print([a,b,c])
    abc=str(int(a)*int(c))+str(b)+str(int(c)-1)
    print(abc)
    return

Diff()

