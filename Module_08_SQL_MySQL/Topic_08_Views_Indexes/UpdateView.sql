CREATE OR REPLACE VIEW student_summary AS
SELECT student_id, name, age
FROM student
WHERE age > 18;