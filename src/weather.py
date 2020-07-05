# API Documentation: https://www.weatherbit.io/api/weather-forecast-16-day
# API Endpoint: "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
# Scoring Model: http://www.meteovista.com/weather-rating/2971/0
# Limit: 500 calls/day



# Get Data from API
import pandas as pd

# Convert wind speed in m/s into beaufort
def beaufort(x):
        x = pd.DataFrame(x)
        for index, row in x.iterrows():
            if row["wind_spd"] <= 0.2:
                x.iloc[index][0] = 0
            elif row["wind_spd"] <= 1.5:
                x.iloc[index][0] = 1
            elif row["wind_spd"] <= 3.3:
                x.iloc[index][0] = 2
            elif row["wind_spd"] <= 5.4:
                x.iloc[index][0] = 3
            elif row["wind_spd"] <= 7.9:
                x.iloc[index][0] = 4
            elif row["wind_spd"] <= 10.7:
                x.iloc[index][0] = 5
            elif row["wind_spd"] <= 13.8:
                x.iloc[index][0] = 6
            elif row["wind_spd"] <= 17.1:
                x.iloc[index][0] = 7
            elif row["wind_spd"] <= 20.7:
                x.iloc[index][0] = 8
            elif row["wind_spd"] <= 24.4:
                x.iloc[index][0] = 9
            elif row["wind_spd"] <= 28.4:
                x.iloc[index][0] = 10
            else:
                x.iloc[index][0] = 11
        return x

