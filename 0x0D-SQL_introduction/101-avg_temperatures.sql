-- displays the average temp by city
-- ordered by temperature desc

SELECT city, AVG(value)as avg_temp
FROM temperature
GROUP BY city
Order BY avg_temp DESC;
