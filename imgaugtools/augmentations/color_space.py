import numpy as np

def change_color_channels(image, channel_images):
    print(channel_images)
    red_factor, green_factor, blue_factor = channel_images
    image[:, :, 0] *= red_factor
    image[:, :, 1] *= green_factor
    image[:, :, 2] *= blue_factor
    return np.clip(image, 0, 255)

def intensify_color(image, intensity_tuple):
    print(intensity_tuple)
    color,factor=intensity_tuple
    factor=np.uint8(factor*255)
    color_idx = {'red': 0, 'green': 1, 'blue': 2}
    channel = color_idx[color.lower()]
    image[:, :, channel] *= factor
    return np.clip(image, 0, 255)

def grayscale(image):
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)
    return np.dot(image[..., :3], [0.2989, 0.587, 0.114]).astype(np.uint8)
