# main.py
import psycopg2
from band import Band
from concert import Concert
from venue import Venue

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="concert_db",
    user="nashon",
    password="23456",
    host="localhost"
)

# Example usage of Band class
band = Band(band_id=1, name="The Beatles", hometown="Liverpool", conn=conn)
band.play_in_venue("The Cavern Club", "1961-02-09")

# Example usage of Concert class
concert = Concert(concert_id=1, band_id=1, venue_id=1, date="1961-02-09", conn=conn)
print(concert.introduction())

# Example usage of Venue class
venue = Venue(venue_id=1, title="The Cavern Club", city="Liverpool", conn=conn)
print(venue.most_frequent_band())

# Close the connection after operations
conn.close()
