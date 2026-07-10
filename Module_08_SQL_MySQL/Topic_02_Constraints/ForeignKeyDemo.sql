CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    dept_id INT,
    emp_name VARCHAR(100),
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);