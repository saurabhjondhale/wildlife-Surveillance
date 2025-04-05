import pandas as pd
import folium

data = pd.read_csv("sightings_log.csv")
m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=14)

for _, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Detection']} ({row['Confidence']*100:.1f}%)",
        icon=folium.Icon(color="green" if row["Confidence"] > 0.8 else "red")
    ).add_to(m)

m.save("wildlife_map.html")
