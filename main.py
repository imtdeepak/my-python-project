'''
MY first Project
'''
name = "Deepak"
print(f"I am {name}")
a = int(input("Enter a Number A: "))
b = int(input("Enter a Number B: "))
print("The Greater Number is : ")
if a>b: 
    print(a)
if (b>a) :
    print(b)
else :
    print ("Both are same numbers.")
x=1
print("Test while loop exit at 0")
while x >0 :
    print(x)
    x = int(input("Enter a number"))

def get_sum (a,b):
    return a + b

print("sum of both the numbers :")
print("The sum of A and B is = ", get_sum(a,b))
