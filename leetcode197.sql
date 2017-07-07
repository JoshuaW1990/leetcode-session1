-- Write your MySQL query statement below

-- Weather
-- +---------+------------+------------------+
-- | Id(INT) | Date(DATE) | Temperature(INT) |
-- +---------+------------+------------------+
-- |       1 | 2015-01-01 |               10 |
-- |       2 | 2015-01-02 |               25 |
-- |       3 | 2015-01-03 |               20 |
-- |       4 | 2015-01-04 |               30 |
-- +---------+------------+------------------+


SELECT w1.Id
FROM Weather AS w1
WHERE w1.Temperature > (
    SELECT w2.Temperature
    FROM Weather AS w2
    WHERE TIMESTAMPDIFF(day, w2.Date, w1.Date) = 1
);


-- https://discuss.leetcode.com/topic/21614/my-simple-solution-using-inner-join
SELECT w1.Id
FROM Weather AS w1
JOIN Weather AS w2 ON (TIMESTAMPDIFF(day, w2.Date, w1.Date) = 1) AND (w2.Temperature < w1.Temperature);


-- https://discuss.leetcode.com/topic/11066/simple-solution/2
SELECT wt1.Id
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND
      TO_DAYS(wt1.DATE)-TO_DAYS(wt2.DATE)=1;


SELECT w1.Id FROM Weather w1, Weather w2
WHERE subdate(w1.Date, 1)=w2.Date AND w1.Temperature>w2.Temperature;
