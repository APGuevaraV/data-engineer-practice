select country.continent , floor(avg(city.population)) 
from country 
join city on 
country.code = city.countrycode 
group by country.continent;

select MAX(months * salary) as maximo,
 count(*) 
 from employee where 
 months*salary = (select max(months * salary)from employee);

  select ceil(avg(salary) - 
  AVG(cast(replace(cast(salary as char),'0','')as UNSIGNED))) 
  AS diferencia from employees;

SELECT
CASE
    WHEN a+b <=c or b+c<= a or a+c<=b THEN 'Not A Triangle'
    WHEN a=b and b=c  THEN 'Equilateral'
    WHEN a=b or b=c or c=a THEN 'Isosceles'
    ELSE 'Scalene'
    
END as TRIANGLE_TYPE
FROM 
TRIANGLES;