#!/usr/bin/env python3

from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine("sqlite:///Chinook.sqlite")

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on "
                       "PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000 ",engine)

# Print head of DataFrame
print(df.head())