import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

from flight.models import SensorDataAnalysis

geolocator = Nominatim(user_agent="geolocator")


# execute a celery task, every 30 mins, return data for the latest entry in database
def analyze_senor_data():
    df = pd.read_csv("sensor-data.csv")

    # Clean up data
    rows_initial = len(df)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    rows_after_cleanup = len(df)
    # TODO: cleaning wrong data or improve format

    # Get address for start, end and every LOCATION_STEP-th location for relevant insights
    df["LatLong"] = df.apply(lambda row: str(row["LATITUDE"]) + "," + str(row["LONGITUDE"]), axis=1)
    LOCATION_STEP = 2000
    df_intermediate = df.iloc[::LOCATION_STEP, :]
    df = pd.concat([df_intermediate, df.tail(1)])

    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    df["Location"] = df["LatLong"].apply(geocode)
    locations = df["Location"].to_list()
    locations = [f"({loc.latitude}, {loc.longitude}) -> {loc.address}" for loc in locations if loc]

    SensorDataAnalysis.objects.create(
        initial_entries=rows_initial,
        entries_after_cleanup=rows_after_cleanup,
        test_locations=len(locations),
        start_location=locations[0],
        end_location=locations[-1],
        intermediate_locations=locations[1:-1],
    )
