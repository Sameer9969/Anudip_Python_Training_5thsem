"""2. E-Commerce Inventory & Sales Dashboard 
Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).  """

# ==================================================
# E-COMMERCE INVENTORY & SALES DASHBOARD
# ==================================================

# Nested Dictionary
# Har Product ki ID key hai
# Aur value me name, price, stock aur sold store hai

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Smartphone", "price": 25000, "stock": 4, "sold": 60},
    "P103": {"name": "Headphones", "price": 2500, "stock": 45, "sold": 110},
    "P104": {"name": "Smart Watch", "price": 5000, "stock": 0, "sold": 40},
    "P105": {"name": "Keyboard", "price": 1200, "stock": 15, "sold": 8}
}

# Menu baar-baar chalane ke liye infinite loop
while True:

    # Menu Display
    print("\n====================================")
    print("E-COMMERCE INVENTORY DASHBOARD")
    print("====================================")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock After Sale")
    print("4. Out Of Stock Products")
    print("5. Products With Stock Less Than 5")
    print("6. Total Inventory Value")
    print("7. Best Selling Product")
    print("8. Least Selling Product")
    print("9. Total Revenue")
    print("10. Low Stock Report")
    print("11. Above Average Sales Products")
    print("12. Promotion Products")
    print("13. Exit")

    # User se choice lena
    choice = input("Enter Choice : ")

    # ======================================
    # 1. DISPLAY ALL PRODUCTS
    # ======================================
    if choice == "1":

        print("\nALL PRODUCTS")

        # Dictionary Traversal
        for pid in products:

            print(
                pid,
                products[pid]["name"],
                products[pid]["price"],
                products[pid]["stock"],
                products[pid]["sold"]
            )

    # ======================================
    # 2. ADD NEW PRODUCT
    # ======================================
    elif choice == "2":

        pid = input("Enter Product ID : ").upper()

        # Duplicate ID Check
        if pid in products:

            print("Product ID Already Exists")

        else:

            name = input("Enter Product Name : ")

            price = int(input("Enter Price : "))
            stock = int(input("Enter Stock : "))
            sold = int(input("Enter Sold Quantity : "))

            # Validation
            if price >= 0 and stock >= 0 and sold >= 0:

                products[pid] = {
                    "name": name,
                    "price": price,
                    "stock": stock,
                    "sold": sold
                }

                print("Product Added Successfully")

            else:

                print("Values Cannot Be Negative")

    # ======================================
    # 3. UPDATE STOCK AFTER SALE
    # ======================================
    elif choice == "3":

        pid = input("Enter Product ID : ").upper()

        if pid in products:

            qty = int(input("How Many Products Sold : "))

            if qty <= products[pid]["stock"]:

                products[pid]["stock"] = products[pid]["stock"] - qty

                products[pid]["sold"] = products[pid]["sold"] + qty

                print("Stock Updated Successfully")

            else:

                print("Not Enough Stock Available")

        else:

            print("Product Not Found")

    # ======================================
    # 4. OUT OF STOCK PRODUCTS
    # ======================================
    elif choice == "4":

        print("\nOUT OF STOCK PRODUCTS")

        for pid in products:

            if products[pid]["stock"] == 0:

                print(
                    pid,
                    products[pid]["name"]
                )

    # ======================================
    # 5. STOCK LESS THAN 5
    # ======================================
    elif choice == "5":

        print("\nLOW STOCK PRODUCTS")

        for pid in products:

            if products[pid]["stock"] < 5:

                print(
                    pid,
                    products[pid]["name"],
                    products[pid]["stock"]
                )

    # ======================================
    # 6. TOTAL INVENTORY VALUE
    # ======================================
    elif choice == "6":

        total_value = 0

        for pid in products:

            value = (
                products[pid]["price"]
                * products[pid]["stock"]
            )

            total_value = total_value + value

        print("Total Inventory Value =", total_value)

    # ======================================
    # 7. BEST SELLING PRODUCT
    # ======================================
    elif choice == "7":

        best_pid = ""

        highest_sold = -1

        for pid in products:

            if products[pid]["sold"] > highest_sold:

                highest_sold = products[pid]["sold"]

                best_pid = pid

        print(
            best_pid,
            products[best_pid]["name"],
            products[best_pid]["sold"]
        )

    # ======================================
    # 8. LEAST SELLING PRODUCT
    # ======================================
    elif choice == "8":

        least_pid = ""

        lowest_sold = 999999

        for pid in products:

            if products[pid]["sold"] < lowest_sold:

                lowest_sold = products[pid]["sold"]

                least_pid = pid

        print(
            least_pid,
            products[least_pid]["name"],
            products[least_pid]["sold"]
        )

    # ======================================
    # 9. TOTAL REVENUE
    # ======================================
    elif choice == "9":

        revenue = 0

        for pid in products:

            revenue = revenue + (
                products[pid]["price"]
                * products[pid]["sold"]
            )

        print("Total Revenue =", revenue)

    # ======================================
    # 10. LOW STOCK REPORT
    # ======================================
    elif choice == "10":

        print("\nLOW STOCK REPORT")

        for pid in products:

            if products[pid]["stock"] < 5:

                print(
                    pid,
                    products[pid]["name"],
                    products[pid]["stock"]
                )

    # ======================================
    # 11. ABOVE AVERAGE SALES
    # ======================================
    elif choice == "11":

        total_sold = 0

        for pid in products:

            total_sold = (
                total_sold
                + products[pid]["sold"]
            )

        average = total_sold / len(products)

        print("Average Sales =", average)

        for pid in products:

            if products[pid]["sold"] > average:

                print(
                    pid,
                    products[pid]["name"],
                    products[pid]["sold"]
                )

    # ======================================
    # 12. PROMOTION PRODUCTS
    # ======================================
    elif choice == "12":

        promo_products = {}

        for pid in products:

            if products[pid]["sold"] < 10:

                promo_products[pid] = products[pid]

        print("\nPROMOTION PRODUCTS")

        for pid in promo_products:

            print(
                pid,
                promo_products[pid]["name"],
                promo_products[pid]["sold"]
            )

    # ======================================
    # 13. EXIT
    # ======================================
    elif choice == "13":

        print("Program Ended Successfully")

        break

    # Invalid Menu Choice
    else:

        print("Invalid Choice")