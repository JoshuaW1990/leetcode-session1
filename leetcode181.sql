-- Write your MySQL query statement below

-- Use WHERE
SELECT e.Name AS Employee
FROM Employee e
WHERE e.Salary > (
    SELECT m.Salary
    FROM Employee m
    WHERE e.ManagerId = m.Id
);


-- Use JOIN
SELECT e.Name AS Employee
FROM Employee e
JOIN Employee m ON e.ManagerId = m.Id AND e.Salary > m.Salary;
