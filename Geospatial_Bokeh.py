import geopandas as gpd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, HoverTool
from bokeh.palettes import Spectral11
from bokeh.transform import linear_cmap
import numpy as np

# Path to your downloaded shapefile
shapefile_path = "C:/Users/cheta/Downloads/geodata/geodata"

# Load the shapefile
world = gpd.read_file(shapefile_path)

# Print columns to identify potential country name column
print("Columns in dataset:", world.columns)

# Check for column containing country names and map it to 'name'
if 'ADMIN' in world.columns:  # Example: Use 'ADMIN' as country names
    world.rename(columns={'ADMIN': 'name'}, inplace=True)
elif 'SOVEREIGNT' in world.columns:  # Fallback example
    world.rename(columns={'SOVEREIGNT': 'name'}, inplace=True)
else:
    print("No suitable column for country names found. Adding placeholders.")
    world['name'] = 'Unknown'

# Add synthetic population data if 'pop_est' is missing
if 'pop_est' not in world.columns:
    print("'pop_est' column is missing. Adding synthetic data...")
    world['pop_est'] = np.random.randint(1000000, 200000000, size=len(world))

# Prepare the GeoJSON data
geo_source = GeoJSONDataSource(geojson=world.to_json())

# Create a Bokeh figure
p = figure(
    title="Interactive World Map",
    width=900,  # Increased width for better view
    height=600,  # Increased height for better view
    tools="pan,wheel_zoom,reset",
    tooltips=[("Country", "@name"), ("Population", "@pop_est")],
)

# Add patches for countries with a color mapper
mapper = linear_cmap(
    field_name='pop_est', 
    palette=Spectral11, 
    low=world["pop_est"].min(), 
    high=world["pop_est"].max(),
)

p.patches(
    'xs', 'ys', 
    source=geo_source, 
    fill_color=mapper, 
    fill_alpha=0.8,  # Increased transparency for clearer view
    line_color="black",  # border color to black for better contrast
    line_width=1,  # Increased line width for borders
)

# Add HoverTool for interactivity
p.add_tools(HoverTool(tooltips=[("Country", "@name"), ("Population", "@pop_est")]))

# Hide axis for cleaner map
p.axis.visible = False

# Save the output to an HTML file and open it in a browser
output_file("interactive_world_map_custom.html")
show(p)
