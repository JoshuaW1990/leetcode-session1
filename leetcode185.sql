-- Write your MySQL query statement below

SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM Employee AS e
JOIN Department AS d ON d.Id = e.DepartmentId
WHERE 3 > (
    SELECT COUNT(DISTINCT(e2.Salary))
    FROM Employee AS e2
    WHERE e2.Salary > e.Salary
    AND e.DepartmentId = e2.DepartmentId
);

