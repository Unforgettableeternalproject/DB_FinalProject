### This project provides multilanguage README.md file
[![Static Badge](https://img.shields.io/badge/lang-en-red)](https://github.com/Unforgettableeternalproject/DB_FinalProject/blob/main/README.md) [![Static Badge](https://img.shields.io/badge/lang-zh--tw-yellow)](https://github.com/Unforgettableeternalproject/DB_FinalProject/blob/main/README.zh-tw.md)

---
# Automobile Company Database Project

### Project Members: 411177013 顏榕嶙、 411177034 吳傢澂

## Overview

This project involves designing and implementing a relational database for an automobile company. The database covers various aspects of the company's operations, including vehicles, brands, models, options, dealers, customers, suppliers, and manufacturing plants. The project includes the following components:
1. E-R Diagram
2. Relational Schema
3. Database Creation and Population
4. Sample Queries and Results
5. User Interface (Wyrm)

## Project Structure

The project repository is organized as follows:

```graphql
├── ER_Diagram/
│   └── er_diagram.png
├── Relational_Schema/
│   └── relational_schema.png
├── Results/
│   └── Example Query 1.png
│   └── Example Query 2.png
│   └── Example Query 3.png
│   └── Example Query 4.png
│   └── Example Query 5.png
│   └── User_Interface_Snapshot.png
├── src/
│   └── Generator/
│       └── RandomDataGenerator.py
│   └── ConnectionTest.py
│   └── ExampleQuery.py
├── README.md
├── README.zh-tw.md
└── requirements.txt
```

### Folder Descriptions

- **ER_Diagram**: Contains the E-R diagram of the database.
- **Relational_Schema**: Contains the relational schema diagram.
- **Results**: Contains the results of sample queries.
- **src**: Contains the data generator, database connection test, and example query scripts.
- **README.md**: This README file.
- **README.zh-tw.md**: This README file in Traditional Chinese.
- **requirements.txt**: Lists the dependencies required for running the project.

## E-R Diagram

The E-R diagram represents the conceptual design of the database, including all entity and relationship sets, primary keys, and cardinalities. It can be found in the `ER_Diagram` folder:

![ER Diagram](ER_Diagram/er_diagram.png)

## Relational Schema

The relational schema diagram represents the logical design of the database. It includes the tables, columns, primary keys, and foreign keys. The diagram can be found in the `Relational_Schema` folder:

![Relational Schema](Relational_Schema/relational_schema.png)

## Sample Queries

The `sample_queries.sql` script contains SQL queries that answer specific questions as required by the project. You can run this script to get the results, which are also provided in the `Results` folder.

### Sample Queries List

1. **Defective Transmissions Query**: Identifies cars with defective transmissions and their customers.
2. **Top Dealer by Sales**: Finds the dealer with the highest sales by dollar amount in the past year.
3. **Top 2 Brands by Unit Sales**: Identifies the top 2 brands by unit sales in the past year.
4. **Best Month for SUV Sales**: Determines the month(s) with the highest SUV sales.
5. **Dealers with Longest Inventory Time**: Finds dealers who keep vehicles in inventory for the longest average time.

## User Interface (GUI)
We have developed a GUI for querying to facilitate usage. This GUI can be obtained from the following repository:
[Wyrm-DB_GUI](https://github.com/Unforgettableeternalproject/Wyrm-DB_GUI-)

Snapshot:
![截圖](Results/User_Interface_Snapshot.png)

This GUI provides an interface to connect to a MariaDB database and retrieve information. Users can input queries through the GUI and view results directly within the application.

## Running the Project

### Requirements

- Python 3.10 or above
- MariaDB (or any other relational database)
- Required Python packages listed in `requirements.txt`

### Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Unforgettableeternalproject/DB_FinalProject
   cd <repository_name>
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the sample queries:
   ```bash
   python src/ExampleQuery.py
   ```
4. (Optional) Run the provided interface:
   ```bash
   git clone https://github.com/Unforgettableeternalproject/Wyrm-DB_GUI-
   cd Wyrm-DB_GUI-
   # Follow the instructions in Wyrm-DB_GUI-'s README to configure and run
   ```

## Conclusion

This project demonstrates the full cycle of database development from conceptual design to implementation and querying. The provided E-R diagram and relational schema ensure a robust and scalable database design. The sample data and queries showcase the database's functionality and provide insights into the company's operations.

For any questions or issues, please contact Bernie, Charlie here: [![Static Badge](https://img.shields.io/badge/mail-Bernie-blue)
](mailto:ptyc4076@gmail.com), [![Static Badge](https://img.shields.io/badge/mail-Charlie-green)](mailto:charlie930320@gmail.com).

---
