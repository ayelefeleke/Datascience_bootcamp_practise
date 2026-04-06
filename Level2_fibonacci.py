#ask the user to enter input
print("Enter the number of fibonacci numbers you want to generate")
n=int(input())#convert input to integer
#chech if number is positive
if n <=0:
    print("Please enter positive number")
else:
    #first two fibonacci numbers
    a=0
    b=1
    print("fibonacci sequence.")
    for i in range(n):
        print(a,end=" ")#this prints on the same line wit space
        temp=a+b #calculate the next no.
        a=b  #move b into a
        b=temp   #move temp to b