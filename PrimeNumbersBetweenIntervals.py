lower = int(input("Enter Lower Range: "))
upper = int(input("Enter Upper Range: "))

print("Prime Numbers Between",lower,"&",upper,"are:")

for num in range(lower+1,upper):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
