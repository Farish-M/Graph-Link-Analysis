import pandas as pd
import csv
from dataclasses import dataclass

@dataclass
class Airport:
    airport_id: int
    name: str
    city: str
    IATA: str
    ICAO: str
    Latitude: float
    Longitude: float

@dataclass
class Route:
    airline: str
    airline_id: int
    source_airport: str
    source_airport_id: int
    destination_airport: str
    destination_airport_id: int

def clean(value):
    """Normalise OpenFlights nulls: '\\N' and '' both mean None."""
    value = value.strip()
    return None if value in ("", r"\N") else value

def parse_airports(file):
    valid, skipped = [], 0
    with open(file, encoding="utf-8", newline="") as f:
        for line in csv.reader(f):
            # TODO 1: Guard the field count, then skip and log why
            for values in line:
                clean(values)
            # TODO 2: Run types through try/except
            # TODO 3: Check graph usability
            # TODO 4: Append an Aiport(...) on success, else skipped += 1 and log reason
            pass
    print(f"airports: {len(valid)} valid, {skipped} skipped")
    return valid

def main():
    airport_data = "data/airports.dat"
    route_data = "data/routes.dat"

    parse_airports(airport_data)

    airport_data = pd.read_csv(airport_data)
    route_data = pd.read_csv(route_data)

if __name__ == "__main__":
    main()