"""Problem 3: E-Commerce Coupon Fraud Detection 
Problem Statement 
A file named coupons.txt contains coupon usage records. 
SAVE50 
WELCOME20 
SAVE50 
FESTIVE10 
SAVE50 
WELCOME20 
NEWUSER 
FESTIVE10 
SAVE50 
NEWUSER 
Tasks 
1. Count the usage frequency of each coupon.  
2. Identify coupons used more than 3 times.  
3. Create a set of unique coupons.  
4. Display the most frequently used coupon.  
5. Save suspicious coupon records into fraud_report.txt.  
Sample Output 
Coupon Usage Frequency: 
SAVE50 : 4 
WELCOME20 : 2 
FESTIVE10 : 2 
NEWUSER : 2 
Suspicious Coupons: 
SAVE50 
Unique Coupons: 
{'SAVE50', 'WELCOME20', 'FESTIVE10', 'NEWUSER'} 
Most Frequently Used Coupon: 
SAVE50 
resources = { 
"Warehouse1": ["Food", "Medicine", "Blankets"], 
Fraud Report Generated Successfully"""
###########################cd classroom\python_test3
############################ python cyber_security_login_audit.py
def coupon_fraud_detection():
    try:
        file = open("coupons.txt", "r")

        coupon_count = {}
        unique_coupons = set()

        for line in file:
            coupon = line.strip()

            unique_coupons.add(coupon)

            if coupon in coupon_count:
                coupon_count[coupon] += 1
            else:
                coupon_count[coupon] = 1

        file.close()

        print("Coupon Usage Frequency:")
        for coupon in coupon_count:
            print(coupon, ":", coupon_count[coupon])

        print("\nSuspicious Coupons:")

        fraud_file = open("fraud_report.txt", "w")

        for coupon in coupon_count:
            if coupon_count[coupon] > 3:
                print(coupon)
                fraud_file.write(coupon + "\n")

        fraud_file.close()

        print("\nUnique Coupons:")
        print(unique_coupons)

        most_used = max(coupon_count, key=coupon_count.get)

        print("\nMost Frequently Used Coupon:")
        print(most_used)

        print("\nFraud Report Generated Successfully")

    except FileNotFoundError:
        print("coupons.txt file not found.")
    except Exception as e:
        print("Error:", e)


# Function Call
coupon_fraud_detection()