SELECT dept_id, COUNT(*) AS count
FROM employee
GROUP BY dept_id
HAVING COUNT(*) > 1;