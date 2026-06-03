# write a program to calculate simple intrest
#--------------------------------
#input of principle amount ,time, rate of intrest
print("-----SIMPLE INTREST -----")
principle = float(input("Enter the principle amount: "))
time = int(input("enter the time: "))
rate = float(input("enter the rate of intrest:"))
#--------------------------------
print("----------------------------------------")
print("principle amount: ", principle)
print("taken: ", time)
print("rate of interest: ", rate)
print("----------------------------------------")
#--------------------------------
#calculating the simple intrest
if(principle<0 ):
    exit("principle amount cannot be negative.....EXITED")
if(time<0 ):
    exit("time cannot be negative.....EXITED")
if(rate<0 ):
    exit("rate of interest cannot be negative.....EXITED")
#--------------------------------

simple_intrest = (principle * time * rate) / 100
print("Simple Interest: ", simple_intrest)

#--------------------------------