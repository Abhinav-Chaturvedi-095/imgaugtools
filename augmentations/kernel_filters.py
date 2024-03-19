import numpy as np
from scipy.ndimage import convolve

def sharpen(image):
    kernel = np.array([[0, -1, 0],
                       [-1,  5, -1],
                       [0, -1, 0]])
    
    sharpened_image = np.zeros_like(image)
    for i in range(image.shape[-1]):  # Loop over channels
        sharpened_image[..., i] = convolve(image[..., i], kernel)
        
    return sharpened_image

def blur(image):
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]],dtype=np.float32) / 9.0
    
    blur_image = np.zeros_like(image)
    for i in range(image.shape[-1]):
        blur_image[...,i] = convolve(image[..., i],kernel)
    
    return blur_image

def add_noise(image, noise_level):
    print(noise_level)
    image_uint8 = np.clip(image, 0, 255).astype(np.uint8)
    
    # Generate noise with the same shape as the input image
    noise = np.random.normal(scale=noise_level, size=image.shape)
    
    # Add noise to the input image and clip the result to the valid range [0, 255]
    noisy_image = np.clip(image_uint8 + noise, 0, 255)
    
    return noisy_image

def scale_image(image, annotations, scale_factor):
    new_width,new_height = int(image.shape[0] * scale_factor), int(image.shape[1] * scale_factor)
    transformed_image=np.resize(image, (new_width, new_height, image.shape[2]))
    adjusted_annotations=[]
    for annotation in annotations:
        label, x_center, y_center, width, height = annotation
        
        x_center_norm = x_center / image.shape[0]
        y_center_norm = y_center / image.shape[1]
        width_norm = width / image.shape[0]
        height_norm = height / image.shape[1]
        
        x_center_scaled = x_center_norm * scale_factor
        y_center_scaled = y_center_norm * scale_factor
        width_scaled = width_norm * scale_factor
        height_scaled = height_norm * scale_factor

        x_center_adj = x_center_scaled * transformed_image.shape[0]
        y_center_adj = y_center_scaled * transformed_image.shape[1]
        width_adj = width_scaled * transformed_image.shape[0]
        height_adj = height_scaled * transformed_image.shape[1]
        
        adjusted_annotations.append([label, x_center_adj, y_center_adj, width_adj, height_adj])
        
    return transformed_image,adjusted_annotations
