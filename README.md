# Graph-Link-Analysis
Graph-link analysis tool that loads airport and route data into Neo4j to answer connection questions.

## Overview
The graph-link analysis tool uses the openflights.org data of airports and routes, in order to determine the shortest path between airports, the busiest airports and reachable neighbours from a source airport.

## Assumptions
- Airports have 14 columns, and Routes have 9 columns.
- Missing airport codes in route data are unsuable and should be skipped rather than used.
- Airports without a IATA code should be excluded from the graph


## Data Model
The airports are the nodes of the graph and routes are the relationships, with IATA as the join key used to link the directed `FLYING_TO` relationships between airports. I used IATA as the key as it's the unique identifier the routes use to link the source to destination airports.

Each airport nodes carry name, city, IATA, ICAO, and coordinates properties.

I apply the uniqueness constraint on IATA in the database, as it allows for loading to be idempotent and fast.

## Architecture
`parse.py`
Validates raw data on dat files into clean objects usable data for Neo4j database
- Flight and Route data are parsed in separate functions
- Checks are performed to validate the data following the data model and assumptions
- Once validated the data class objects are appeneded into a Python list, valid.

`load.py`
- Connects the tool to a Neo4j database using the .env file
- Uses `parse_airports` and `parse_routes` functions from `parse.py`
- Create the constraint for the airport IATA and require the it to be unique for each of the airports
- Iterates through parsed airports and routes list, turning it into Python dictionaries.
- Run `load_airports` and `load_routes` to unwind data into the Neo4j database

`quaries.py`
- Run the specific Cypher queries in order to achieve the goal of the tool, to find: the shortest path, high traffic hubs, and reachable neighbours from a source airport.

## Prerequisites
- Python 3.14.5
- Neo4j instance
- Data files: **airports**.dat and routes.dat

## Setup
- Clone the repo
- Run `pip install -r requirements.txt`
- Download `airports.dat` and `routes.dat` into a data folder
  - `airports.dat` = `https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat`
  - `routes.dat` = `https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat`
- Create a Neo4j instance
- Copy instance information into a .env file. See .env.example for required credentials.

## Usage

## Data Source and Licensing

## Future Work and Limitations