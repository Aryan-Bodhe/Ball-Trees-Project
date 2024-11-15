import pandas as pd
import os
from BallStarTree import BallStarTree

# Double check the path to the dataset if you encounter a FileNotFoundError
# Define the relative path to the dataset
file_dir = os.path.dirname(__file__)  # Directory of the current Python file
csv_path = os.path.join(file_dir, '..', '..', 'Datasets', 'csv', '2D_Moons.csv')  # Go up and locate Datasets

# Load the dataset with headers (the Moons and Blobs and Swiss Roll datasets have headers)
df = pd.read_csv(csv_path)
data = df.to_numpy()

# Alternative Loading data when it's just plain data without headers
# df = pd.read_csv(csv_path, header = None)
# data = df.to_numpy()

# Initialize and fit the Ball* Tree (set has_classification to True if the dataset has target labels)
ball_star_tree = BallStarTree(data=data, has_classification = True, leaf_size=10, max_iterations=100, alpha=0.5, S=10)
ball_star_tree.fit()  # This will print the structure of the tree and plot it

query_point = [0.5, 0.75]

# K-Nearest Neighbors Query
k = 10
nearest_neighbors = ball_star_tree.knn_query(query_point, k)
print(f"\n\n\n\nThe {k} nearest neighbors to {query_point} are:")
print(nearest_neighbors)
# Convert nearest_neighbors to just a list of points
nearest_neighbors_points = [point[1] for point in nearest_neighbors]

# Range Query
radius = 0.1
range_query_points = ball_star_tree.range_query(query_point, radius)
print(f"\n\n\n\nThe points within a radius of {radius} from {query_point} are:")
print(range_query_points)

ball_star_tree.plot(query_point = query_point, knn_queried_points = nearest_neighbors_points, range_queried_points = range_query_points, radius = radius)