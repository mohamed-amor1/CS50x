-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema

.tables

.schema crime_scene_reports

-- Find crime scene description
SELECT description FROM crime_scene_reports 
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

.schema interviews
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";


.schema bakery_security_logs  
SELECT name, people.license_plate FROM people 
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;

.schema atm_transactions
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND 
transaction_type = "withdraw";

/*
We know that As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
*/

SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

/*
We now have caller and receiver phone numbers for possible suspects
*/

.schema
SELECT name, caller, receiver 
FROM people 
JOIN phone_calls ON people.phone_number = phone_calls.caller 
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;


SELECT name, caller, receiver 
FROM people 
JOIN phone_calls ON people.phone_number = phone_calls.receiver 
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- Let's change the phone_calls table to include the names of callers and receivers

ALTER TABLE phone_calls ADD caller_name;
ALTER TABLE phone_calls ADD receiver_name;

-- adding the caller_name
UPDATE phone_calls
SET caller_name = (SELECT name FROM people WHERE people.phone_number = phone_calls.caller AND year = 2021 AND month = 7 AND day = 28 AND duration < 60)
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- adding the receiver name

UPDATE phone_calls
SET receiver_name = (SELECT name FROM people WHERE people.phone_number = phone_calls.receiver AND year = 2021 AND month = 7 AND day = 28 AND duration < 60)
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- List of suspects (caller_name + receiver_name)
SELECT caller_name, receiver_name FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;


-- the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow

.schema flights
SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29
ORDER BY hour,minute LIMIT 1;

/*
-- earliest flight tomorrow (day 29)
id	= 36
origin_airport_id= 8
destination_airport_id=	4
year=2021	
month	=7
day	=29
hour	=8
minute = 20
*/

.tables
.schema

-- getting the origin airport
SELECT * FROM airports JOIN flights ON airports.id = flights.origin_airport_id WHERE flights.origin_airport_id = 8 AND flights.id = 36;

-- getting the destination airport
SELECT * FROM airports JOIN flights ON airports.id = flights.destination_airport_id WHERE flights.destination_airport_id = 4 AND flights.id = 36 ;

-- getting the passenger list for flight 36
.schema
SELECT name FROM people JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id WHERE flights.id = 36;




/*
by executing the below query we find that Bruce is the thief
*/
SELECT name FROM people JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id WHERE flights.id = 36
AND name IN 
(SELECT caller_name FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
AND name IN
(SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND 
transaction_type = "withdraw")
AND name IN
(SELECT name FROM people 
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25);
