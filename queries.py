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

def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print(shortest_path(driver, "HGU", "PNP"))

if __name__ == "__main__":
    main()