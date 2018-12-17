#Input N<=1000

n=int(input("Enter Number:"))
temp=n
rev=0

if(n<=1000):
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    
    if(temp==rev):
        print("The Number is a Palindrome!")
    
    else:
        print("The Number isn't a Palindrome!")
else:
    print("Enter a Number less than or equal to 1000")
