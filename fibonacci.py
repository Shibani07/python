n=int(input("Enter number of terms "))
n1=0
n2=1
count=0
if n==1:
    print("The series is:",n1)
else:
    print("Fibonacci sequence: ")
    while count<n:
        print(n1)
        s=n1+n2
        n1=n2
        n2=s
        count+=1
