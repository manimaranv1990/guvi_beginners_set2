lower=int(input("Enter the Lower Limit for the Range:"))
upper=int(input("Enter the Upper Limit for the Range:"))

for i in range(lower+1,upper):
    if(i%2==0):
        print(i)
