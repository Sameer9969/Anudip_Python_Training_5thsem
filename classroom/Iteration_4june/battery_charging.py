#write a program to for dispaling that battery is charging level
charging_level = int(input("enter the battery charging level:"))
electricity_status = True
while(charging_level<=100):
    if(electricity_status):
        print("Battery level :",charging_level,"%")
        charging_level +=10
    else:
        print("Battery is not charging")
        break
#--------------------------------
print("Battery is fully charged")
print("----------------------------------------")
#--------------------------------


