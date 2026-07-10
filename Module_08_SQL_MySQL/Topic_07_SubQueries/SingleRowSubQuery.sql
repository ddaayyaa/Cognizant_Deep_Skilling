SELECT name
FROM student
WHERE dept_id = (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'HR'
);