--Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates
SELECT DISTINCT(city) from station where right(city,1) in ('a','e','i','o','u')

select DISTINCT(CITY) from station 
where lower(left(CITY,1)) not in ('a','e','i','o','u') 
and right(CITY,1) not in ('a','e','i','o','u');

select distinct(city) from station where left(city,1) not in ('a','e','i','o','u');
select DISTINCT(city) from station 
where lower(left(city,1)) not in ('a','e','i','o','u') 
and right(city,1) not in ('a','e','i','o','u');

select name from customers ORDER BY right(name,3),customer_id ;

select format(min(lat_n),4) from station where lat_n > 38.7780;