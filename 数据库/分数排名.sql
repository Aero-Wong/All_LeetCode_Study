/*
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/

Create table If Not Exists Scores (Id int, Score DECIMAL(3,2))
Truncate table Scores
insert into Scores (Id, Score) values ('1', '3.5')
insert into Scores (Id, Score) values ('2', '3.65')
insert into Scores (Id, Score) values ('3', '4.0')
insert into Scores (Id, Score) values ('4', '3.85')
insert into Scores (Id, Score) values ('5', '4.0')
insert into Scores (Id, Score) values ('6', '3.65')

/*# Write your MySQL query statement below*/

SELECT
    obj.score as Score,
    cast(
    CASE
WHEN @rowtotal = obj.score THEN
    @rownum
WHEN @rowtotal := obj.score THEN
    @rownum :=@rownum + 1
WHEN @rowtotal = 0 THEN
    @rownum :=@rownum + 1
END as SIGNED) AS Rank
FROM
    (
        SELECT
            score
        FROM
            Scores 
        ORDER BY
            score DESC
    ) AS obj,
    (SELECT @rownum := 0 ,@rowtotal := NULL) r;


select s1.Score, count(distinct s2.Score) Rank
from Scores as s1 join Scores as s2 on s1.Score <= s2.Score
group by s1.Id 
order by s1.Score DESC;