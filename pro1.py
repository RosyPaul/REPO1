#python functions for simple interest
def SI(principle,rate,time):
    return (principle*rate*time)/100

#int main()
p=float(input("Enter the principal amount"))
r=float(input("Enter rate of simple interset"))
t=int(input("Enter the time"))
res=SI(p,r,t)
print("The simple interest for given input is:",res)
