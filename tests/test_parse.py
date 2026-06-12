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
        expected = Airport(airport_id=1,name="Goroka Airport",city="Goroka",iata="GKA",icao="AYGA",latitude=-6.081689834590001,longitude=145.391998291)
        assert len(result) == 2
        assert result[0] == expected