#currently, the big problem is doing a factorial - I don't want to have to use the math module, but there's no product function. make a special exception?
#if I import Math, there's no significance to me making a function for cos with the taylor series cause I can just use the cos fucntion in math 
#multiplication of 2 numbers n and m, is just adding n by m of amount of times
#multiplication of 3 numbers n, m and p is just adding n by by m amount of times then the product of that by p times
#this wouldn't be a big deal if there weren't 2 sets of variables. {N} -> the number of numbers to multiply, and {n} -> the numbers themselves
#and {N} = count({n}) or |{n}| or the cardinality of {n}, so really, there's only 1 variable to consider

#all of the above didn't help with this task, as I didn't realise you can write *= and its basically a sumproduct() function - but its interesting thinking

terms2=5
def factorial():
    facto=1
    for i in range(1,terms2+1):
        facto*=i
    return(facto)


print(factorial())
