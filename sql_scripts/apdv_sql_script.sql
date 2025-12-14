# All databases
SHOW DATABASES;

# CREATE A Database for apqv sql lsusa
CREATE DATABASE apdv_sql_lsusa;

# consider required databasse
USE apdv_sql_lsusa;

# Show tables
SHOW TABLES;

CREATE TABLE liquor_sales(
	ls_id INT AUTO_INCREMENT PRIMARY KEY,
	years INT(4) NOT NULL,
    months INT(2) NOT NULL,
    supplier VARCHAR(1000),
    item_code VARCHAR(255) NOT NULL, # Change to VARCHAR 
    item_desc VARCHAR(2000),
    item_type VARCHAR(30),
    retail_sales FLOAT, # Change to float 
    retail_transfer FLOAT, # Change to float 
    warehouse_sales FLOAT # Change to float 
);

# SEE Liquor SALES
SELECT * from liquor_sales LIMIT 5;

# Altering month column dtype to tiny int to save space
ALTER TABLE liquor_sales
MODIFY COLUMN months TINYINT;

# Description of table 
DESC liquor_sales;

# Aggregate functions
SELECT SUM(retail_sales) FROM liquor_Sales;
SELECT avg(retail_sales) FROM liquor_sales;
SELECT * FROM liquor_Sales
WHERE retail_sales = (
	SELECT MAX(retail_Sales) FROM liquor_sales
);
SELECT * FROM liquor_sales
WHERE retail_sales = (
	SELECT MIN(retail_Sales) FROM liquor_sales
);
SELECT * FROM liquor_Sales
WHERE retail_sales < 3;
SELECT COUNT(*) FROM liquor_sales;

# Sum up Sales group by year 
SELECT
    years,
    SUM(retail_sales) AS total_retail_sales
FROM liquor_sales
GROUP BY years
ORDER BY years;


SELECT SUM(retail_sales) FROM liquor_sales
WHERE years = 2020
GROUP BY months;


# Delete all records
# SET SQL_SAFE_UPDATES = 0; 
# DELETE FROM liquor_Sales;
# SET SQL_SAFE_UPDATES = 1;
