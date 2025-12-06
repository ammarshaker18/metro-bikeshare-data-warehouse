import pandas as pd

# Load raw file
df = pd.read_csv("metro-trips-2024-q1.csv")

# Rename columns for clarity
df = df.rename(columns={
    "trip_id": "Trip Id",
    "duration": "Duration",
    "start_time": "Start Time",
    "end_time": "End Time",
    "start_station": "Start Station",
    "end_station": "End Station",
    "bike_id": "Bike Id",
    "passholder_type": "Passholder Type",
    "bike_type": "Bike Type"
})

# Convert datetime columns
df["Start Time"] = pd.to_datetime(df["Start Time"])
df["End Time"] = pd.to_datetime(df["End Time"])

# Add useful date fields for analysis
df["Year"] = df["Start Time"].dt.year
df["Month"] = df["Start Time"].dt.month
df["Day"] = df["Start Time"].dt.day
df["Hour"] = df["Start Time"].dt.hour

# Save cleaned file
df.to_csv("transformed_trips.csv", index=False)

print("ETL pipeline completed successfully.")
