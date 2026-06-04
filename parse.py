import pandas as pd

def main():
    airport_data = "data/airports.dat"
    route_data = "data/routes.dat"

    airport_data = pd.read_csv(airport_data)
    route_data = pd.read_csv(route_data)

if __name__ == "__main__":
    main()