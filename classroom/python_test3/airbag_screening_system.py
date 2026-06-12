"""Problem 2: Airport Baggage Screening System 
Problem Statement 
Passenger baggage weights (in kg) are stored as tuples: 
baggage = ( 
("P101", 18), 
("P102", 32), 
("P103", 24), 
("P104", 36), 
("P105", 28), 
("P106", 20), 
("P107", 41), 
("P108", 26), 
("P109", 19), 
("P110", 34) 
) 
Tasks 
1. Display passengers carrying baggage above 30 kg.  
2. Count passengers within and exceeding limits.  
3. Calculate excess baggage charges (₹500 per kg above 30 kg).  
4. Create a list of passengers requiring manual inspection.  
5. Find the passenger carrying the heaviest baggage.  
Sample Output 
Passengers Exceeding 30 kg Limit: 
P102 
P104 
P107 
P110 
Passengers Within Limit: 6 
Passengers Exceeding Limit: 4 
Excess Baggage Charges: 
P102 : ₹1000 
P104 : ₹3000 
P107 : ₹5500 
P110 : ₹2000 
Passengers Requiring Manual Inspection: 
['P102', 'P104', 'P107', 'P110'] """


#============================================
def baggage_screening():
    try:
        baggage = (
            ("P101", 18),
            ("P102", 32),
            ("P103", 24),
            ("P104", 36),
            ("P105", 28),
            ("P106", 20),
            ("P107", 41),
            ("P108", 26),
            ("P109", 19),
            ("P110", 34)
        )

        within_limit = 0
        exceeding_limit = 0
        inspection_list = []

        print("Passengers Exceeding 30 kg Limit:")

        for passenger, weight in baggage:
            if weight > 30:
                print(passenger)
                exceeding_limit += 1
                inspection_list.append(passenger)
            else:
                within_limit += 1

        print("\nPassengers Within Limit:", within_limit)
        print("Passengers Exceeding Limit:", exceeding_limit)

        print("\nExcess Baggage Charges:")
        for passenger, weight in baggage:
            if weight > 30:
                charge = (weight - 30) * 500
                print(passenger, ": ₹", charge)

        print("\nPassengers Requiring Manual Inspection:")
        print(inspection_list)

        heaviest_passenger = baggage[0][0]
        heaviest_weight = baggage[0][1]

        for passenger, weight in baggage:
            if weight > heaviest_weight:
                heaviest_weight = weight
                heaviest_passenger = passenger

        print("\nHeaviest Baggage:")
        print(heaviest_passenger, "-", heaviest_weight, "kg")

    except Exception as e:
        print("Error:", e)


# Function Call
baggage_screening()