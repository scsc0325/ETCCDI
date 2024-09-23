import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Coordinates for the AOSO observatories
observatories = {
    'Seoul': (37.5665, 126.9780),
    'Jeju': (33.4996, 126.5312),
    'Gwangju': (35.1595, 126.8526)
}

# Create a GeoDataFrame with the observatories
geometry = [Point(lon, lat) for lat, lon in observatories.values()]
gdf = gpd.GeoDataFrame(observatories.keys(), geometry=geometry, columns=['Location'])

# Load a base map of South Korea (using a GeoPandas dataset or external shapefile)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
korea = world[(world.name == 'South Korea')]

# Plotting the map
fig, ax = plt.subplots(figsize=(8, 10))
korea.plot(ax=ax, color='lightgrey')

# Plot the observatories
gdf.plot(ax=ax, color='red', markersize=100)

# Annotate the observatoriesfor x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['Location']):
    ax.text(x, y, label, fontsize=12, ha='right')

# Set title and show the plot
ax.set_title('AOSO Observatories in Korea')
plt.show()