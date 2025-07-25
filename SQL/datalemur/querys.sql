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

/*
Write a query to identify the top 2 Power Users who sent the highest number
 of messages on Microsoft Teams in August 2022. Display the IDs of these 2 
 users along with the total number of messages they sent. Output the results
  in descending order based on the count of the messages.
*/

SELECT sender_id, count(sender_id) from messages 
where 
DATE_PART('year', sent_date) = 2022 and 
EXTRACT(MONTH FROM sent_date) = 8
GROUP by sender_id
ORDER by count(*) desc
limit 2;