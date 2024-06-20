import mariadb


def query1():
    # Execute the SQL query
    cursor.execute("""
        SELECT VIN, c.customerName
        FROM `customer's car`
        NATURAL JOIN vehicles as v
        NATURAL JOIN customers as c
        WHERE modelName IN (
            SELECT s.modelName
            FROM suppliers as s
            WHERE manufacturingDate BETWEEN '2014-01-01' AND '2017-12-31'
            AND manufacturingPart = 'transmission'
            AND supplierName = 'Getrag'
        )
    """)

    # Fetch all the results
    results = cursor.fetchall()

    print("The customers who own a car with a Getrag transmission are:")
    # Print the results
    for result in results:
        print(f"VIN: {result[0]}, Customer Name: {result[1]}")


def query2():
    # Execute the SQL query
    cursor.execute("""
            SELECT dealerName
            FROM (
                SELECT dealerID, dealerName, SUM(saleFigure) AS sumSale
                FROM salerecord AS s
                NATURAL JOIN dealers
                WHERE DATEDIFF(CURRENT_DATE, saleDate) < 365
                GROUP BY dealerID, dealerName
            ) AS dIdNs
            ORDER BY sumSale DESC
            LIMIT 1;
        """)

    # Fetch all the results
    results = cursor.fetchall()

    print("The dealer with the highest sales in the past year is:")
    # Print the results
    for result in results:
        print(f"Dealer Name: {result[0]}")


def query3():
    # Execute the SQL query
    cursor.execute("""
        SELECT brandName
        FROM salerecord
        NATURAL JOIN vehicles
        NATURAL JOIN models
        NATURAL JOIN brands
        WHERE DATEDIFF(CURRENT_DATE, saleDate) < 365
        GROUP BY brandName
        ORDER BY COUNT(*) DESC
        LIMIT 2;
    """)

    # Fetch all the results
    results = cursor.fetchall()

    print("In the past year the top 2 brands with the most sales are:")
    # Print the results
    for result in results:
        print(f"Brand Name: {result[0]}")


def query4():
    # Execute the SQL query
    cursor.execute("""
        SELECT MONTH(saleDate) as saleMonth
        FROM salerecord
        NATURAL JOIN vehicles
        WHERE bodyStyle LIKE '%SUV%'
        GROUP BY saleMonth
        ORDER BY COUNT(*) DESC
        LIMIT 1;
    """)

    # Fetch all the results
    results = cursor.fetchall()

    print("The month with the most SUV sales is:")
    # Print the results
    for result in results:
        print(f"Sale Month: {result[0]}")


def query5():
    # Execute the SQL query
    cursor.execute("""
        SELECT dealerName
        FROM inventory
        NATURAL JOIN dealers
        GROUP BY dealerName
        ORDER BY AVG(DATEDIFF(CURRENT_DATE, inventoryTime)) DESC
        LIMIT 1;
    """)

    # Fetch all the results
    results = cursor.fetchall()

    print("The dealer with the oldest inventory is:")
    # Print the results
    for result in results:
        print(f"Dealer Name: {result[0]}")


if __name__ == "__main__":
    user_setting = {
        "user": "411177034",
        "password": "411177034",
        "host": "0.tcp.jp.ngrok.io",
        "port": 12592,
        "database": "411177034"
    }

    connection = mariadb.connect(**user_setting)
    cursor = connection.cursor()

    # Disable Auto-Commit
    connection.autocommit = False

    print("--------------------")
    query1()
    print("--------------------")
    query2()
    print("--------------------")
    query3()
    print("--------------------")
    query4()
    print("--------------------")
    query5()
    print("--------------------")

    cursor.close()
    connection.close()
