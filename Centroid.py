# Calculate centroid

import Centrepoint
import numpy as np

axis_x = [33.763541543,42.573478754647,35.2412342141234]
axis_y = [6,7,8,9,0,563767254.435849367432]

def calcCentroid():
    centroid_x = np.mean(axis_x)
    centroid_y = np.mean(axis_y)

    return centroid_x, centroid_y
