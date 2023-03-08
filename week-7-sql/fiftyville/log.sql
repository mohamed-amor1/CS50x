-- The following SQL code is used to solve a mystery and involves querying a database.

-- Use .schema to display the schema of the database.
.schema

-- Use .tables to display the tables in the database.
.tables

-- Use .schema to display the schema of the crime_scene_reports table.
.schema crime_scene_reports

-- Find the crime scene description for a particular date and street.
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Use .schema to display the schema of the interviews table.
.schema interviews

-- Find interviews that took place on a particular date and contain the word "bakery" in the transcript.
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

-- Use .schema to display the schema of the bakery_security_logs table.
.schema bakery_security_logs

-- Find the names and license plates of people who were at a bakery on a particular date and time.
SELECT name, people.license_plate FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;

-- Use .schema to display the schema of the atm_transactions table.
.schema atm_transactions

-- Find the names of people who made a withdrawal from an ATM located on a particular street on a particular date.
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND
transaction_type = "withdraw";



-- We are looking for phone calls made on a particular date with a duration of less than 60 seconds.
SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- We have obtained caller and receiver phone numbers from the previous query and want to find the names associated with those phone numbers.
-- Use .schema to display the schema of the database.
.schema

-- Find the names associated with the phone numbers of callers who made a call on a particular date with a duration of less than 60 seconds.
SELECT name, caller, receiver
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- Find the names associated with the phone numbers of receivers who received a call on a particular date with a duration of less than 60 seconds.
SELECT name, caller, receiver
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;




-- We want to modify the phone_calls table to include the names of callers and receivers.
-- Add a column called "caller_name" to the phone_calls table.
ALTER TABLE phone_calls ADD caller_name;

-- Add a column called "receiver_name" to the phone_calls table.
ALTER TABLE phone_calls ADD receiver_name;

-- We want to populate the "caller_name" column with the names of the callers for calls made on a specific date with a duration of less than 60 seconds.
-- Update the "caller_name" column for calls made on a specific date with a duration of less than 60 seconds.
UPDATE phone_calls
SET caller_name = (SELECT name FROM people WHERE people.phone_number = phone_calls.caller AND year = 2021 AND month = 7 AND day = 28 AND duration < 60)
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- We want to populate the "receiver_name" column with the names of the receivers for calls received on a specific date with a duration of less than 60 seconds.
-- Update the "receiver_name" column for calls received on a specific date with a duration of less than 60 seconds.
UPDATE phone_calls
SET receiver_name = (SELECT name FROM people WHERE people.phone_number = phone_calls.receiver AND year = 2021 AND month = 7 AND day = 28 AND duration < 60)
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- We want to create a list of possible suspects by selecting the caller and receiver names from the phone_calls table for calls made on a specific date with a duration of less than 60 seconds.
-- Select the caller and receiver names from the phone_calls table for calls made on a specific date with a duration of less than 60 seconds.
SELECT caller_name, receiver_name FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;



-- the thief says that they were planning to take the earliest flight out of Fiftyville tomorrow

-- Select the earliest flight departing from Fiftyville on July 29, 2021
-- Display the flight's ID, origin and destination airport IDs, date, and departure time
SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29
ORDER BY hour, minute LIMIT 1;

/*
earliest flight tomorrow (day 29)
id = 36
origin_airport_id = 8
destination_airport_id = 4
year = 2021
month = 7
day = 29
hour = 8
minute = 20
*/

-- Select the origin airport for flight 36
SELECT * FROM airports JOIN flights ON airports.id = flights.origin_airport_id WHERE flights.origin_airport_id = 8 AND flights.id = 36;

-- Select the destination airport for flight 36
SELECT * FROM airports JOIN flights ON airports.id = flights.destination_airport_id WHERE flights.destination_airport_id = 4 AND flights.id = 36;

-- Select the passenger list for flight 36
-- Join the people and passengers tables on passport number
-- Join the flights table on flight ID
SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE flights.id = 36;





-- Select the name of the person who was on flight 36, made a phone call on July 28, 2021 that lasted less than 60 seconds, withdrew money from an ATM on Leggett Street on the same day, and had their license plate detected by bakery security cameras between 10:15 and 10:25 AM on the same day
-- This person is identified as the thief

SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id
WHERE flights.id = 36
AND name IN (
SELECT caller_name FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
)
AND name IN (
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
)
AND name IN (
SELECT name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
);

/*
by executing the query we find that Bruce is the thief
*/

-- Select the caller and receiver names for phone calls made on July 28, 2021 that lasted less than 60 seconds and were initiated by Bruce
-- This helps identify Bruce's accomplice, who is named Robin
SELECT caller_name, receiver_name FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller_name = 'Bruce';

/*
caller_name     receiver_name
Bruce           Robin
*/



