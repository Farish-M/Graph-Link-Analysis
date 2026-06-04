import pandas as pd

def clean_empty(data):
    data.dropna(inplace = True)
    return data

def main():
    airport_data = "data/airports.dat"
    route_data = "data/routes.dat"

    airport_data = pd.read_csv(airport_data)
    route_data = pd.read_csv(route_data)

    print(clean_empty(airport_data))
    print(clean_empty(route_data))

if __name__ == "__main__":
    main()