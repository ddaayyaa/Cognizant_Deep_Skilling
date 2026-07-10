SELECT name
FROM student
WHERE age > (
    SELECT AVG(age)
    FROM student
);