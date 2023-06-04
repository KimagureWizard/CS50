-- Keep a log of any SQL queries you execute as you solve the mystery.

--get the crime scene report
SELECT * FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

--get clues
SELECT * FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28;

--| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

--get plate number to confirm the entry time
SELECT * FROM people
WHERE name = "Eugene";

--check timeframe
SELECT * FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute <= 30 AND minute >= 15 AND activity = 'exit';

SELECT * FROM atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street";


SELECT * FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"
AND name IN
(
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND month = 7 AND day = 28 AND duration <= 60
)
AND name IN
(
SELECT name FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute <= 30 AND minute >= 15 AND activity = 'exit'
)
AND name IN
(
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON flights.origin_airport_id = airports.id
WHERE year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND city = "Fiftyville"
)

SELECT * FROM phone_calls
WHERE caller = "(367) 555-5533" AND year = 2021 AND month = 7 AND day = 28 AND duration <= 60;

SELECT * FROM phone_calls
WHERE caller = "(770) 555-1861" AND year = 2021 AND month = 7 AND day = 28;

SELECT * FROM airports
JOIN flights ON flights.origin_airport_id = airports.id
JOIN passengers ON passengers.flight_id = flights.id
WHERE (passengers.passport_number = 5773159633 OR passengers.passport_number = 3592750733) AND city = "Fiftyville" AND year = 2021 AND month = 7 AND day = 28;

SELECT city FROM airports
WHERE id = 4;


SELECT * FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE (phone_number = "(725) 555-3243" OR phone_number = "(375) 555-8161");

SELECT * FROM flights
WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29;


SELECT * FROM flights
JOIN passengers ON passengers.flight_id = flights.id
WHERE passport_number = "3391710505";


|   id   | name  |  phone_number  | passport_number | license_plate | account_number | person_id | creation_year | id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       | 49610011       | 686048    | 2010          | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       | 26013199       | 514354    | 2012          | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |


|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 847116 | Philip | (725) 555-3243 | 3391710505      | GW362R6       |
| 864400 | Robin  | (375) 555-8161 | NULL            | 4V16VO0



| id | abbreviation |          full_name          |    city    | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+--------------+-----------------------------+------------+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 18        | 3592750733      | 4C   |
| 7  | DXB          | Dubai International Airport | Dubai      | 24 | 7                 | 8                      | 2021 | 7     | 30  | 16   | 27     | 24        | 3592750733      | 2C   |
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 36        | 5773159633      | 4A   |
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville | 54 | 8                 | 5                      | 2021 | 7     | 30  | 10   | 19     | 54        | 3592750733      | 6C   |