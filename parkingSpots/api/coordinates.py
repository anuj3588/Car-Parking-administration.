import math

def calculate_coordinates_within_radius(lat, lon, radius):
    # Earth's radius in meters
    earth_radius = 6371000

    # Convert latitude and longitude to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Calculate the distance in radians corresponding to the radius
    angular_radius = radius / earth_radius

    # Create a grid of coordinates within the specified radius
    coordinates = []
    steps = 20  # Number of steps in each dimension of the grid
    for i in range(steps):
        for j in range(steps):
            # Calculate the relative position within the grid
            rel_x = (i / steps) - 0.5
            rel_y = (j / steps) - 0.5

            # Calculate the angular distance for the current grid point
            ang_dist_x = angular_radius * rel_x
            ang_dist_y = angular_radius * rel_y

            # Calculate the new latitude and longitude coordinates
            new_lat = math.degrees(lat_rad + ang_dist_y)
            new_lon = math.degrees(lon_rad + ang_dist_x / math.cos(lat_rad))

            coordinates.append((new_lat, new_lon))

    return coordinates

# # Example usage
# latitude = 18.55625
# longitude = 73.779044
# radius = 10000  # in meters
#
# result = calculate_coordinates_within_radius(latitude, longitude, radius)
# for lat, lon in result:
#     print(f"Latitude: {lat}, Longitude: {lon}")
