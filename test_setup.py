import geopandas as gpd
import folium
from shapely.geometry import Point

mumbai = gpd.GeoDataFrame(
    {"name": ["Mumbai"]},
    geometry=[Point(72.8777, 19.0760)],
    crs="EPSG:4326",
)
print(mumbai)

pt = mumbai.geometry.iloc[0]
m = folium.Map(location=[pt.y, pt.x], zoom_start=11)
folium.Marker([pt.y, pt.x], popup="Mumbai").add_to(m)
m.save("mumbai_map.html")
print("Saved mumbai_map.html - setup works!")