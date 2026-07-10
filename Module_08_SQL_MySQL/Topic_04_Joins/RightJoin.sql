SELECT s.name, d.dept_name
FROM student s
RIGHT JOIN department d ON s.dept_id = d.dept_id;