a=float(input("Enter the first side of triangle"))
b=float(input("Enter the second side of triangle"))
c=float(input("Enter the third side of triangle"))
if(a==b and a==c):
    print("Triangle is equilateral")
elif(a==b or a==c or b==c):
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")
