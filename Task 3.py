list=[]
n=int(input("Enter the number of words u are going to enter: "))
print("Enter the words: ")
 for i in range(n):
   list.append(input())

 length=len(words[0])

 for i in range(1,n):
   if length<len(words[i]):
      length=len(words[i])
 print("Length of longest word: ",length)     

   
