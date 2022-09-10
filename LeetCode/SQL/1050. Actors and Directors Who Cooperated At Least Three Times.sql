# Write your MySQL query statement below
select actor_id ,director_id from actordirector
group by 1,2
having count(director_id)>2