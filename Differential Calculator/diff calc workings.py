x="3"
y="4"
z=x+y
print(int(z))

y=list("3x^2")
print(y)
#can you do for i+1?

"""for i in range(1,len(y)):
    if type(y[i]) == int:
        
    print(c)
    
    # don't need to do this cause it's gonna be a string anyway
    """
    
y="3x^2"
print(y[1])

""""a=341515130
print(a[6])

This wont work because an integer isn't considered a list the same way a string is"""

#Does python consider negatives to be integers?

print(type(-1))

#it do

#does python consider negatives to be floats?

print(type(-1.0))

#it also do


print(float(13/787))

print(sum(range(1,4)))

print((-1)**2)

print(str(((-1)**2)/sum(range(0,2*2+1))))

n=5
for i in range(3):
    n+=1
    
print(n)

print((2*0)-1)



num=[i for i in range(0,5)]

num.pop(max(num))

max(num)