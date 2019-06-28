n=int(input("Enter the number of elements in the list"))
l=[]
print("Enter the numbers")
for i in range(n):
    i=int(input())
    l.append(i)
ans=1
for j in range(n):
      ans=ans*l[j]
print("Product= ",ans)     
         
