n=int(input("Enter the number of elements"))
l=[]
print("Enter the numbers")
for j in range(n):
 l.append(input())
for i in range(n):
    if(l[i]%2==0):
        print("Even")
    else:
        print("Odd")
        

