import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from parse import parse_airports
from parse import parse_routes
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

def load_routes(driver, rows):
    query = """
        UNWIND $routes AS row
        MATCH (s:Airport {iata: row.source_airport})
        MATCH (d:Airport {iata: row.destination_airport})
        MERGE (s)-[:FLYING_TO]->(d)
        """
    result = driver.execute_query(query, routes=rows, database_="neo4j")
    print(f"Created {result.summary.counters.relationships_created} route edges")

def main():
    airports = parse_airports("data/airports.dat")
    routes = parse_routes("data/routes.dat")
    airport_rows = [asdict(a) for a in airports]
    routes_rows = [asdict(a) for a in routes]
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connected to Neo4j")
        driver.execute_query(
            "CREATE CONSTRAINT airport_iata IF NOT EXISTS "
            "FOR (a:Airport) REQUIRE a.iata IS UNIQUE",
            database_="neo4j",
        )
        load_airports(driver, airport_rows)
        print(f"Loaded {len(airport_rows)} airports")
        load_routes(driver, routes_rows)
        print(f"Loaded {len(routes_rows)} routes")

if __name__ == "__main__":
    main()