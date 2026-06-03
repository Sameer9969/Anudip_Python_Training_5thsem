#program to convert tine into coorresponding minute , hour and second
#INPUT OF TIME IN SECOND
second = int(input("Enter the time in second: "))
# CHECK THE SECOND IS NEGATIVE
if(second<0):
    exit("time cannot be negative......EXITED")
# -----------------------------------------
print("----------------------------------------")
hour = 0
minutes = 0
#convert the second into hour
if(second>=3600):
    hour = second // 3600
    second = second % 3600
#convert the second into minute
#------------------------------------------
if(second>=60):
    minutes = second // 60
    second = second % 60
#------------------------------------------
#OUTPUT OF THE TIME IN HOUR, MINUTE AND SECOND
print("Time in hour: ", hour,"hr")
print("Time in minute: ", minutes,"min")
print("Time in second: ", second,"sec")
#------------------------------------------
#------------------------------------------
