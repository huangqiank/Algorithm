select a.Salary as SecondHighestSalary from
(select id, Salary, row_number() over (order by Salary) as rnk
from Employee) a where rnk = 2

select ifnull  ((select distinct salary from Employee
order by salary desc
limit 1 offset  1),null) as SecondHighestSalary
'''ifnull''''