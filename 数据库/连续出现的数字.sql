/*
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
*/

Create table If Not Exists Logs (Id int, Num int);
Truncate table Logs;
insert into Logs (Id, Num) values ('1', '1');
insert into Logs (Id, Num) values ('2', '1');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '2');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');

/*# Write your MySQL query statement below*/

select distinct num as ConsecutiveNums 
from (select num,case @row when num then @count:=@count+1 else @count:=1 end as amount,case @row when num then @row else @row:=num end as sign from logs,(select @row:=null,@count:=1) a) temp 
where amount>=3;

select distinct l1.Num ConsecutiveNums from logs l1
join logs l2 on l1.Id = l2.Id - 1
join logs l3 on l1.Id = l3.Id - 2
where l1.num = l2.num and l2.num = l3.num;