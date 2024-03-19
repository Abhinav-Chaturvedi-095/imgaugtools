import numpy as np

def rotate(image, angle):
    radians = np.radians(angle)
    rotation_matrix = np.array([[np.cos(radians), -np.sin(radians)],
                                [np.sin(radians), np.cos(radians)]])
    return np.dot(image, rotation_matrix)

def rotate_clockwise(image, angle):
    return np.rot90(image, k=int(angle / 90), axes=(1, 0))

def rotate_anticlockwise(image, angle):
    return np.rot90(image, k=int(-angle / 90), axes=(1, 0))