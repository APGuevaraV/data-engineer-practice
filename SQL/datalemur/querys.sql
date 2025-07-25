/*
Write a query that calculates the total viewership for laptops
 and mobile devices where mobile is defined as the sum of tablet
 and phone viewership. Output the total viewership for laptops as
 laptop_reviews and the total viewership for mobile devices as 
 mobile_views.
*/

select 
count(if(device_type = 'laptop',1,null)) as laptop_views,
count(if(device_type in ('phone','tablet'),1,null)) as mobile_views
from viewership;


with cte as(
select user_id,count(tweet_id) as cnt 
from tweets 
where year(tweet_date)=2022 
group by user_id;
)

select cnt as tweet_bucket,count(user_id) as user from cte
group by cnt;

/*
Write a query to retrieve the top three cities that have the highest 
number of completed trade orders listed in descending order. Output 
the city name and the corresponding number of completed trade orders.
*/
SELECT users.city, 
sum(
    CASE 
        WHEN 
        trades.status = 'Completed' 
            THEN 1 
        ELSE 
            null 
    END
    )
as total_orders 
FROM trades
inner JOIN
users
on 
 users.user_id = trades.user_id
GROUP by users.city
ORDER BY total_orders DESC
LIMIT 3
;