import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from parse import parse_airports
from dataclasses import asdict

# read .env file
load_dotenv()

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

def load_airports(driver, rows):
    query = """
        UNWIND $airports AS row
        MERGE (a:Airport {iata: row.iata})
        SET a.name = row.name, 
            a.city = row.city, 
            a.airport_id = row.airport_id, 
            a.icao = row.icao, 
            a.latitude = row.latitude, 
            a.longitude = row.longitude
        """
    driver.execute_query(query, airports=rows, database_="neo4j")

def main():
    airports = parse_airports("data/airports.dat")
    rows = [asdict(a) for a in airports]
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connected to Neo4j")
        driver.execute_query(
            "CREATE CONSTRAINT airport_iata IF NOT EXISTS "
            "FOR (a:Airport) REQUIRE a.iata IS UNIQUE",
            database_="neo4j",
        )

if __name__ == "__main__":
    main()