import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

# Load a sample geospatial dataset (Natural Earth data or custom shapefile)
shapefile_path = "C:/Users/cheta/Downloads/geodata/geodata"
world = gpd.read_file(shapefile_path)

# Select a subset of countries to make the network smaller
subset = world[world['ADMIN'].isin(['United States of America', 'Canada', 'Mexico', 'Brazil', 'United Kingdom'])]

# Create a GeoDataFrame of centroids for the selected countries
centroids = subset.copy()
centroids['geometry'] = centroids.centroid

# Extract country names and centroids for labeling
country_names = centroids['ADMIN'].tolist()
coordinates = centroids['geometry'].apply(lambda point: (point.x, point.y)).tolist()

# Create a graph
G = nx.Graph()

# Add nodes (countries) with their coordinates
for name, coord in zip(country_names, coordinates):
    G.add_node(name, pos=coord)

# Add random edges (connections between countries)
edges = [
    ('United States of America', 'Canada'),
    ('United States of America', 'Mexico'),
    ('United Kingdom', 'Brazil'),
    ('Canada', 'Brazil'),
    ('Mexico', 'United Kingdom'),
]
G.add_edges_from(edges)

# Plot the network
fig, ax = plt.subplots(figsize=(12, 10))

# Plot country boundaries
world.boundary.plot(ax=ax, linewidth=1, color="lightgray")  # setting boundary color

# Draw the network with customized parameters
nx.draw(
    G,
    pos=nx.get_node_attributes(G, 'pos'),
    ax=ax,
    with_labels=True,
    node_size=800,  # Larger nodes
    node_color='darkorange',  #node color
    font_size=12,  # Increased font size for better visibility
    font_weight='bold',  # Bold labels
    edge_color='green',  # edge color green
    width=2,  # Increased edge width
    alpha=0.7  # Slight transparency for edges
)

# Add a title and show the plot
plt.title("Geospatial Network and Interconnection", fontsize=16)
plt.show()
