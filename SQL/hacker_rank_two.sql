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

--distancia euclidiana 
select round(sqrt(power(min(lat_n) - max(lat_n),2) +  power(min(long_w) - max(long_w),2)),4) 
from station;

select round(
            abs(min(lat_n) - max(lat_n) ) +  
            abs( min(long_w) - max(long_w))
        ,4) 
from station;

select concat(name,'(',upper(left(occupation,1)),')') from occupations order by name;

select concat('There are a total of',' ',count(*),' ',lower(occupation),'s.' )
from occupations 
group by occupation 
order by count(*) asc,occupation asc;

--subconsultas
--Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

(select city, CHAR_LENGTH(city) as lenght
from station 
where CHAR_LENGTH(city) 
in ( select min(CHAR_LENGTH(city)) from station )
order by city limit 1)

union

(select city, CHAR_LENGTH(city) as lenght
from station 
where CHAR_LENGTH(city) 
in ( select max(CHAR_LENGTH(city)) from station )
order by city limit 1)