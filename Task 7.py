a=float(input("Enter the first number"))
b=float(input("Enter the second number"))
c=float(input("Enter the third number"))
if(a>b):
   if(a<c):
       median=a
   elif(b>c):
       median=b
   else:
       median=c
else:
    if(b<c):
       median=b
    elif(a>c):
        median=a
    else:
        median=c
    
print("Median equals=",median)    
