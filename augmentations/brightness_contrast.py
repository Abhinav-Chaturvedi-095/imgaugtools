import numpy as np

def adjust_brightness(image, factor):
    return np.clip(image * factor, 0, 255)

def adjust_contrast(image, factor):
    mean_value = np.mean(image)
    return np.clip((image - mean_value) * factor + mean_value, 0, 255)
