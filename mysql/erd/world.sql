USE world;

SELECT name, language, percentage 
FROM countries
JOIN languages ON countries.id = languages.country_id 
WHERE language = 'Slovene' 
ORDER BY percentage DESC;

SELECT countries.name, COUNT(cities.country_id) AS city_count
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY city_count DESC;

SELECT cities.population, cities.name
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name = 'Mexico'
ORDER BY cities.population DESC;

SELECT language, percentage, countries.name
FROM languages
JOIN countries ON languages.country_id = countries.id
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT name
FROM countries
WHERE government_form = 'Constitutional Monarchy' 
AND life_expectancy > 75 
AND capital > 200;

SELECT  countries.name AS country, cities.name AS city, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND district = 'Buenos Aires' AND cities.population > 500000;

SELECT region, COUNT(name) AS num_countries
FROM countries
GROUP BY region
ORDER BY num_countries DESC;

