import csv
from dataclasses import dataclass

EXPECTED_AIRPORT_FIELDS = 14
EXPECTED_ROUTE_FIELDS = 9

@dataclass
class Airport:
    airport_id: int
    name: str
    city: str
    iata: str
    icao: str | None
    latitude: float
    longitude: float

@dataclass
class Route:
    airline: str
    airline_id: int | None
    source_airport: str
    source_airport_id: int | None
    destination_airport: str
    destination_airport_id: int | None

def clean(value):
    """Normalise OpenFlights nulls: '\\N' and '' both mean None."""
    value = value.strip()
    return None if value in ("", r"\N") else value

def parse_airports(file):
    valid, skipped = [], 0
    with open(file, encoding="utf-8", newline="") as f:
        for line in csv.reader(f):
            # TODO 1: Guard the field count, then skip and log why
            if len(line) != EXPECTED_AIRPORT_FIELDS:
                skipped += 1
                print(f"skip - expected {EXPECTED_AIRPORT_FIELDS} fields, got {len(line)}")
                continue
            fields = [clean(values) for values in line]
            # TODO 2: Run types through try/except
            try:
                airport_id = int(fields[0])
                latitude = float(fields[6])
                longitude = float(fields[7])
            except (ValueError, TypeError) as e:
                skipped += 1
                print(f"skip - bad number: {e}")
                continue
            # TODO 3: Check graph usability
            if fields[4] is None:
                skipped += 1
                print(f"skip - no IATA: {fields[1]}")
                continue
            # TODO 4: Append an Aiport(...) on success, else skipped += 1 and log reason
            valid.append(Airport(
                airport_id=airport_id,
                name=fields[1],
                city=fields[2],
                iata=fields[4],
                icao=fields[5],
                latitude=latitude,
                longitude=longitude
            ))
    print(f"airports: {len(valid)} valid, {skipped} skipped")
    return valid

# TODO 5: Repeat parse_airports() but for routes
def parse_routes(file):
    valid, skipped = [], 0
    with open(file, encoding="utf-8", newline="") as f:
        for line in csv.reader(f):
            if len(line) != EXPECTED_ROUTE_FIELDS:
                skipped += 1
                print(f"skip - expected {EXPECTED_ROUTE_FIELDS} fields, got {len(line)}")
                continue
            fields = [clean(values) for values in line]
            if fields[2] is None or fields[4] is None:
                skipped += 1
                print(f"skip - missing airport code")
                continue
    print(f"routes: {len(valid)} valid, {skipped} skipped")
    return valid  

def main():
    airport_data = "data/airports.dat"
    route_data = "data/routes.dat"

    airports = parse_airports(airport_data)
    routes = parse_routes(route_data)

if __name__ == "__main__":
    main()