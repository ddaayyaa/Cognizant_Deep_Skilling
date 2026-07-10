SELECT name
FROM student
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE dept_name IN ('HR', 'Sales')
);