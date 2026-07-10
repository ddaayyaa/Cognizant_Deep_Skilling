SELECT s.name
FROM student s
WHERE s.age > (
    SELECT AVG(age)
    FROM student
    WHERE dept_id = s.dept_id
);