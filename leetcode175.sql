-- Write your MySQL query statement below

SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person AS p
LEFT JOIN Address AS a ON a.PersonId = p.PersonId;
