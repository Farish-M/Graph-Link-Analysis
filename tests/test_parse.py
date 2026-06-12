from parse import clean, parse_airports, parse_routes, Airport, Route

class TestClean:
    def test_strips_whitespace(self):
        assert clean("  HGU  ") == "HGU"

    def test_empty_string_becomes_none(self):
        assert clean("") is None

    def test_backslash_n_becomes_none(self):
        assert clean(r"\N") is None
    
    def test_normal_value_passthrough(self):
        assert clean("LAX") == "LAX"

class TestParseAirports:
    def test_valid_row_produces_airports(self, airports_file):
        result = parse_airports(str(airports_file))
        expected = Airport(
            airport_id=1,
            name="Goroka Airport",
            city="Goroka",
            iata="GKA",
            icao="AYGA",
            latitude=-6.081689834590001,
            longitude=145.391998291
            )
        assert len(result) == 2
        assert result[0] == expected

    def test_wrong_field_count_is_skipped(self, airports_file):
        result = parse_airports(str(airports_file))
        assert all(airport.airport_id != 2 for airport in result)

    def test_bad_numeric_field_is_skipped(self, airports_file):
        result = parse_airports(str(airports_file))
        assert all(airport.airport_id != 3 for airport in result)
    
    def test_missing_iata_is_skipped(self, airports_file):
        result = parse_airports(str(airports_file))
        assert all(airport.airport_id!= 4 for airport in result)
    
    def test_null_icao_still_valid(self,airports_file):
        result = parse_airports(str(airports_file))
        expected = Airport(
            airport_id=5,
            name="Port Moresby Jacksons International Airport",
            city="Port Moresby",
            iata="POM",
            icao=None,
            latitude=-9.443380355834961,
            longitude=147.22000122070312,
            )
        assert expected in result

class TestParseRoutes:
    def test_valid_row_produces_routes(self, routes_file):
        result = parse_routes(str(routes_file))
        expected = Route(
            airline="2B",
            airline_id=410,
            source_airport="AER",
            source_airport_id=2965,
            destination_airport="KZN",
            destination_airport_id=2990
        )
        assert len(result) == 2
        assert result[0] == expected
        assert result[1].source_airport_id is None

    #def test_wrong_field_count_is_skipped(self, routes_file):

    #def test_bad_id_is_skipped(self, routes_file):

    #def test_null_id_still_valid(self, routes_file):

    #def test_missing_airport_code_skipped(self, routes_file):