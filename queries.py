import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()
URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

def shortest_path(driver, source, destination):
    query = """
    MATCH p = SHORTEST 1 (s:Airport {iata: $source})-[:FLYING_TO]->+(d:Airport {iata: $destination})
    RETURN length(p) AS result
    """
    records, _, _ = driver.execute_query(
        query, source=source, destination=destination, database_="neo4j"
    )
    return records[0]["result"] if records else None

def top_hub(driver):
    query = """
    MATCH (s:Airport)
    RETURN s.name AS Airport, COUNT { (s)-[:FLYING_TO]-() } as Connections
    ORDER BY Connections DESC
    LIMIT 10
    """
    records, _, _ = driver.execute_query(query)
    for record in records:
        print(record["Airport"], record["Connections"])

def two_hop_neighbour(driver, source):
    query = """
    MATCH (s:Airport {iata: $source})-[r:FLYING_TO*1..2]-(d:Airport)
    WHERE d <> s
    RETURN DISTINCT d.name as Reachable
    """
    records, _, _ = driver.execute_query(query, source=source, database_="neo4j")
    return [record["Reachable"] for record in records]

def main():
    source = input("Source airport (IATA code): ").strip().upper()
    destination = input("Destination airport (IATA code): ").strip().upper()
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print(shortest_path(driver, source, destination))
        top_hub(driver)
        print(two_hop_neighbour(driver, source))

if __name__ == "__main__":
    main()