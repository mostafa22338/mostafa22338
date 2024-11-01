  #ex1
'''def getfact(x):
    i=1
    product=1
    while (i<=x):
        product=product*x
        x=x-1
    return product

a=int(input("enter an integer: "))
if(a<0):
    a=int(input("invalid input /n enter a positive integer: "))
    print(getfact(a))
else: print(getfact(a))'''

#ex2
'''def getdiv(x):
     a=[]
     i=1
     while (i<=x):
          if(x%i==0):
             a.append(i)  
             i=i+1
          else : 
             i=i+1
     return a
a=int(input("enter an integer: "))
print(getdiv(a))'''

#ex3
'''def reverse(x):
    return x[ : :-1]
a=input("enter a string: ")
print(reverse(a))'''

#ex4
'''def idk(a):
    b=[]
    for i in a:
        if(i%2==0):
            b.append(i)
        else: continue
    return b

a=(int(input(" enter a nb to the list: ")))  # i dont know how to let the user insert a list so i did this
c=[]
if(a<0):
    a=int(input("invalid input, add a positive integer: "))
    c.append(a)

while (a>0):
    c.append(a)
    a=int(input(" enter another nb to the list, enter 0 or a negative nb to stop: "))
print ("input ", c ,"output ",idk(c))'''

#ex5
'''def passw(a):
    upp=False
    low=False
    dig=False
    charac=False
    if(len(a)<8):
        return "weak password "
    for i in a:
        if(i.isupper()):
            upp=True
        elif(i.islower()):
            low=True
        elif(i.isdigit()):
            dig=True
        elif(i=="!" or i=="#" or i=="$" or i=="?"):
            charac=True
    if(upp and low and dig and charac):
        print("Strong passwird: ")
    else: print("weak password: ")

b=input("enter a password: ")
passw(b)'''

#ex6
'''def isvalid(a):
    ip=a.split('.')
    if(len(ip)!=4):
        return "invalid ip"
    for i in ip:
        if(not i.isdigit() ):
            return "invalid ip"
        if(int(i)<0 or int(i)>255):
            return "invalid ip"
        if (i!="0" and i[0]=='0'):
            return "invalid ip"
    return "valid ip"
x=input("enter an ip: ")
print(isvalid(x))'''
    




             
    
 



