-- =====================================
-- CREATE DATABASE
-- =====================================

CREATE DATABASE IF NOT EXISTS superstore_db;

USE superstore_db;

-- =====================================
-- CUSTOMERS TABLE
-- =====================================

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    segment VARCHAR(50)
);

-- =====================================
-- PRODUCTS TABLE
-- =====================================

CREATE TABLE products (
    product_id VARCHAR(30) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    sub_category VARCHAR(100)
);

-- =====================================
-- LOCATIONS TABLE
-- =====================================

CREATE TABLE locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code INT,
    region VARCHAR(50)
);

-- =====================================
-- ORDERS TABLE
-- =====================================

CREATE TABLE orders (
    order_id VARCHAR(30) PRIMARY KEY,
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),

    customer_id VARCHAR(20),
    location_id INT,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);

-- =====================================
-- SALES TABLE
-- =====================================

CREATE TABLE sales (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,

    order_id VARCHAR(30),
    product_id VARCHAR(30),

    sales DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(10,2),

    shipping_days INT,
    sales_per_unit DECIMAL(10,2),
    profit_margin DECIMAL(10,2),

    CONSTRAINT fk_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);