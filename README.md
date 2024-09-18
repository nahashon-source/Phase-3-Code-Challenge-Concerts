# Phase-3-Code-Challenge-Concerts


## Overview 
This project involves managing a database of bands, venues, and concerts. It uses PostgreSQL for the database and psycopg2 as the Python library to interact with it.

## Tables
Bands: This table holds information about different bands. It includes columns for the band's name and their hometown.
Venues: This table stores data about venues where concerts are held. It includes the venue's title and city.
Concerts: This table records concert events, linking bands to venues and noting the date of the concert. It establishes relationships between bands and venues through foreign keys.

## Class Descriptions
<!-- Band Class -->
The Band class allows interaction with the bands table. It includes methods to:

1.  Retrieve all concerts by the band.
2. Find all venues where the band has performed.
3. Add a new concert for the band at a specified venue on a given date.
4. Generate introduction statements for all concerts the band has played.
5. Determine which band has performed the most concerts.

<!-- Venue Class -->
The Venue class interacts with the venues table. Its methods include:

1. List all concerts held at the venue.
2. Find all bands that have performed at the venue.
3. Check for concerts on a specific date at the venue.
4. Identify the band that has performed the most at the venue.


<!-- Concert Class -->
The Concert class manages data from the concerts table. It features methods to:

1. Retrieve the band and venue for a specific concert.
2. Check if a concert is held in the band’s hometown.
3. Create an introduction message for the concert.


## Summary
It uses PostgreSQL and psycopg2 for database operations. The project includes tables for bands, venues, and concerts, with classes to handle various queries and data manipulations. The goal is to understand and implement relational database operations and interactions using Python.