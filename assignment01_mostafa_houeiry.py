#ex1
'''a=int(input("enter a nb:"))
b=int(input("enter a nb: "))
c=int(input("enter a nb: "))
if(a>b and a>c):
    print ("the max is ",a)
elif(b>a and b>c):
    print ("the max is " ,b)
else : print ("the max is ",c)'''

#ex2
'''n=int(input("enter a nb: "))

product=1
i=1
if(n<=2 and n>=0): print(1)
else : 
    while(i<=n and product <=100):
        if(i%2!=0):  # check if the number is odd 
            product=product * i
        i+=1
    if (product>=100):
        print ("multiplication exceed ")
    else: print(product)'''

#ex3
'''sum=0
i=0
n=float(input("enter a number: "))
if (n==-1 ): print ("no score were entered ")
else: 
    while (n!=-1):
        sum= sum +n # to sum the numbers
        i+=1  # to count the numbers
        n=float(input("enter a nb: ")) #to let the user re enter another number 
    print("the score average is: " ,sum/i)'''
 
 
 #ex4 
'''n=int(input("enter a four digit number: "))
a=n%10 #to bring the last digit
b=int(n/10)%10  # to bring the 3rd digit
c=int(n/100)%10 # to bring the second digit
d=int(n/1000)%10 # to bring the first digit
print(a,b,c,d) # its extra to show each digit seperately

if(a+b == c+d ):
    print("F")
else: print("u")'''








