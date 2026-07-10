CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    amount DECIMAL(10,2) CHECK (amount > 0)
);