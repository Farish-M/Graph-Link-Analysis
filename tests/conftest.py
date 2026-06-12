import pytest

@pytest.fixture
def airports_file(tmp_path):
    rows = [
        '1,"Goroka Airport","Goroka","Papua New Guinea","GKA","AYGA",-6.081689834590001,145.391998291,5282,10,"U","Pacific/Port_Moresby","airport","OurAirports"',
        '2,"Madang Airport","Madang","Papua New Guinea","MAG","AYMD",-5.20707988739,145.789001465,20,10,"Pacific/Port_Moresby","airport","OurAirports"',
        '3,"Mount Hagen Kagamuga Airport","Mount Hagen","Papua New Guinea","HGU","AYMH","Non-Numeric Latitude",144.29600524902344,5388,10,"U","Pacific/Port_Moresby","airport","OurAirports"',
        r'4,"Nadzab Airport","Nadzab","Papua New Guinea","\N","AYNZ",-6.569803,146.725977,239,10,"U","Pacific/Port_Moresby","airport","OurAirports"',
        r'5,"Port Moresby Jacksons International Airport","Port Moresby","Papua New Guinea","POM","\N",-9.443380355834961,147.22000122070312,146,10,"U","Pacific/Port_Moresby","airport","OurAirports"'
    ]
    path = tmp_path / "airports.dat"
    path.write_text("\n".join(rows), encoding="utf-8")
    return path

@pytest.fixture
def routes_file(tmp_path):
    rows = [
        "2B,410,AER,2965,KZN,2990,,0,CR2",
        "2B,410,ASF,2966,KZN,2990,0,CR2",
        r"2B,410,ASF,\N,MRV,2962,,0,CR2",
        "2B,410,CEK,2968.0,KZN,2990,,0,CR2"
    ]
    path = tmp_path / "routes.dat"
    path.write_text("\n".join(rows), encoding="utf-8")
    return path