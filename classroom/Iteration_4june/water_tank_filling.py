#A water tank is being filled with water at a constant rate of 10 liters per minute. Initially, the tank contains 0 liters of water. 
#Write a program that displays the amount of water in the tank after each minute and continues until the tank reaches 100 liters.
#--------------------------------
water = 0
while(water <=100):
    print("Water in the tank:", water, "liters")
    water += 10
print("tank is full")
print("----------------------------------------")