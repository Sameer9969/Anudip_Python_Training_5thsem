"""5. City Population & Development Dashboard 
Problem Statement 
The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density. 
 
Assignment Rule (Important) 
For all 5 Questions: 
• Use at least 30 records.  
• Do not use built-in sorting functions (sorted(), sort()).  
• Use loops and conditions to find maximum, minimum, rankings, and reports.  
• Display results in a structured format.  
• Add a menu-driven interface using while loop."""
# ============================================
# CITY POPULATION & DEVELOPMENT DASHBOARD
# ============================================

# 30 Cities ka Nested Dictionary
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 90},
    "Kolkata": {"population": 15000000, "area": 206, "literacy": 87},
    "Bangalore": {"population": 13000000, "area": 741, "literacy": 89},
    "Chennai": {"population": 11500000, "area": 426, "literacy": 90},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 83},
    "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 88},
    "Pune": {"population": 7000000, "area": 331, "literacy": 91},
    "Surat": {"population": 6500000, "area": 462, "literacy": 87},
    "Jaipur": {"population": 4000000, "area": 484, "literacy": 76},
    "Lucknow": {"population": 3800000, "area": 349, "literacy": 82},
    "Kanpur": {"population": 3200000, "area": 260, "literacy": 79},
    "Nagpur": {"population": 2900000, "area": 228, "literacy": 92},
    "Indore": {"population": 3300000, "area": 276, "literacy": 85},
    "Thane": {"population": 2500000, "area": 147, "literacy": 91},
    "Bhopal": {"population": 2600000, "area": 285, "literacy": 83},
    "Visakhapatnam": {"population": 2300000, "area": 540, "literacy": 81},
    "Patna": {"population": 2400000, "area": 135, "literacy": 71},
    "Vadodara": {"population": 2200000, "area": 220, "literacy": 90},
    "Ghaziabad": {"population": 2700000, "area": 210, "literacy": 84},
    "Ludhiana": {"population": 1700000, "area": 159, "literacy": 82},
    "Agra": {"population": 1600000, "area": 121, "literacy": 73},
    "Nashik": {"population": 1500000, "area": 259, "literacy": 84},
    "Ranchi": {"population": 1400000, "area": 175, "literacy": 76},
    "Faridabad": {"population": 1450000, "area": 204, "literacy": 83},
    "Meerut": {"population": 1350000, "area": 142, "literacy": 75},
    "Rajkot": {"population": 1400000, "area": 170, "literacy": 82},
    "Kalyan": {"population": 1200000, "area": 137, "literacy": 93},
    "Vasai": {"population": 1150000, "area": 105, "literacy": 88},
    "Srinagar": {"population": 1250000, "area": 294, "literacy": 70}
}

# Infinite Menu Loop
while True:

    # Menu Display
    print("\n" + "=" * 60)
    print("CITY POPULATION & DEVELOPMENT DASHBOARD")
    print("=" * 60)

    print("1. Display All City Details")
    print("2. Find Most Populated City")
    print("3. Find Least Populated City")
    print("4. Calculate Average Population")
    print("5. Cities With Literacy Above 90%")
    print("6. Cities With Literacy Below Average")
    print("7. Calculate Population Density")
    print("8. Find Highest Density City")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. High Literacy / Low Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities By Density")
    print("14. Exit")

    # User Choice
    choice = input("\nEnter Choice : ")

    # ============================================
    # OPTION 1
    # ============================================

    if choice == "1":

        print("\nALL CITY DETAILS")

        for city in cities:

            population = cities[city]["population"]
            area = cities[city]["area"]
            literacy = cities[city]["literacy"]

            print(city, population, area, literacy)

    # ============================================
    # OPTION 2
    # ============================================

    elif choice == "2":

        max_city = list(cities.keys())[0]

        for city in cities:

            if cities[city]["population"] > cities[max_city]["population"]:

                max_city = city

        print("\nMost Populated City :", max_city)
        print("Population :", cities[max_city]["population"])

    # ============================================
    # OPTION 3
    # ============================================

    elif choice == "3":

        min_city = list(cities.keys())[0]

        for city in cities:

            if cities[city]["population"] < cities[min_city]["population"]:

                min_city = city

        print("\nLeast Populated City :", min_city)
        print("Population :", cities[min_city]["population"])

    # ============================================
    # OPTION 4
    # ============================================

    elif choice == "4":

        total_population = 0

        for city in cities:

            total_population += cities[city]["population"]

        average_population = total_population / len(cities)

        print("\nAverage Population :", average_population)

    # ============================================
    # OPTION 5
    # ============================================

    elif choice == "5":

        print("\nCities With Literacy Above 90%")

        for city in cities:

            if cities[city]["literacy"] > 90:

                print(city, "-", cities[city]["literacy"])

    # ============================================
    # OPTION 6
    # ============================================

    elif choice == "6":

        total_literacy = 0

        for city in cities:

            total_literacy += cities[city]["literacy"]

        average_literacy = total_literacy / len(cities)

        print("\nCities With Literacy Below Average")

        for city in cities:

            if cities[city]["literacy"] < average_literacy:

                print(city, "-", cities[city]["literacy"])

    # ============================================
    # OPTION 7
    # ============================================

    elif choice == "7":

        print("\nPopulation Density Report")

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            print(city, "-", round(density, 2))

    # ============================================
    # OPTION 8
    # ============================================

    elif choice == "8":

        highest_density_city = list(cities.keys())[0]

        highest_density = (
            cities[highest_density_city]["population"]
            / cities[highest_density_city]["area"]
        )

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            if density > highest_density:

                highest_density = density
                highest_density_city = city

        print("\nHighest Density City :", highest_density_city)
        print("Density :", round(highest_density, 2))

    # ============================================
    # OPTION 9
    # ============================================

    elif choice == "9":

        print("\nCity Categories")

        for city in cities:

            population = cities[city]["population"]

            if population < 2000000:

                category = "Small"

            elif population <= 10000000:

                category = "Medium"

            else:

                category = "Large"

            print(city, "-", category)

    # ============================================
    # OPTION 10
    # ============================================

    elif choice == "10":

        print("\nDevelopment Priority List")

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            if cities[city]["literacy"] < 80 and density > 5000:

                print(city)
                print("Literacy :", cities[city]["literacy"])
                print("Density :", round(density, 2))
                print()

    # ============================================
    # OPTION 11
    # ============================================

    elif choice == "11":

        high_literacy = {}
        low_literacy = {}

        for city in cities:

            if cities[city]["literacy"] >= 85:

                high_literacy[city] = cities[city]

            else:

                low_literacy[city] = cities[city]

        print("\nHigh Literacy Cities :", len(high_literacy))
        print("Low Literacy Cities :", len(low_literacy))

    # ============================================
    # OPTION 12
    # ============================================

    elif choice == "12":

        total_population = 0
        total_area = 0
        total_literacy = 0

        for city in cities:

            total_population += cities[city]["population"]
            total_area += cities[city]["area"]
            total_literacy += cities[city]["literacy"]

        average_literacy = total_literacy / len(cities)

        print("\nNational Summary Report")
        print("Total Cities :", len(cities))
        print("Total Population :", total_population)
        print("Total Area :", total_area)
        print("Average Literacy :", round(average_literacy, 2))

    # ============================================
    # OPTION 13
    # ============================================

    elif choice == "13":

        density_list = []

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            density_list.append([city, density])

        n = len(density_list)

        for i in range(n):

            for j in range(0, n - i - 1):

                if density_list[j][1] < density_list[j + 1][1]:

                    temp = density_list[j]
                    density_list[j] = density_list[j + 1]
                    density_list[j + 1] = temp

        print("\nCity Density Ranking")

        rank = 1

        for item in density_list:

            print(rank, item[0], round(item[1], 2))

            rank += 1

    # ============================================
    # OPTION 14
    # ============================================

    elif choice == "14":

        print("\nThank You")
        break

    # ============================================
    # INVALID CHOICE
    # ============================================

    else:

        print("\nInvalid Choice")