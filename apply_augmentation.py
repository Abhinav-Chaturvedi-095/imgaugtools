import numpy as np
import os
from .augmentations import *
import cv2

def apply_augmentation(image_path, txt_path, augmentation_type, *args):
    # Load image
    image = load_image(image_path)
    
    # Get image shape
    image_shape = image.shape[:2]
    # Apply augmentation
    if augmentation_type == 'flip_horizontal':
        # Load annotations
        annotations = load_annotations(txt_path,image.shape)
        augmented_image, transformed_annotations = flip_horizontal(image, annotations, image_shape)
        
    elif augmentation_type == 'flip_vertical':
        annotations = load_annotations(txt_path,image.shape)
        augmented_image, transformed_annotations = flip_vertical(image, annotations, image_shape)
    
    elif augmentation_type == 'change_color_channels':
        augmented_image = change_color_channels(image, *args)
        transformed_annotations = load_direct_annotation(txt_path)
    
    elif augmentation_type == 'intensify_color':
        augmented_image = intensify_color(image, *args)
        transformed_annotations = load_direct_annotation(txt_path)

    
    elif augmentation_type == 'grayscale':
        augmented_image = grayscale(image)
        transformed_annotations = load_direct_annotation(txt_path)

    
    elif augmentation_type == 'sharpen':
        augmented_image = sharpen(image)
        transformed_annotations = load_direct_annotation(txt_path)

    
    elif augmentation_type == 'blur':
        augmented_image = blur(image)
        transformed_annotations = load_direct_annotation(txt_path)

    
    elif augmentation_type == 'add_noise':
        augmented_image = add_noise(image, *args)
        transformed_annotations = load_direct_annotation(txt_path)

    
    elif augmentation_type == 'scale_image':
        annotations = load_annotations(txt_path,image.shape)
        augmented_image, transformed_annotations = scale_image(image, annotations, *args)
    
    elif augmentation_type == 'resize':
        annotations = load_annotations(txt_path,image.shape)
        augmented_image, transformed_annotations = resize(image, annotations, *args)
    
    else:
        raise ValueError("Unknown augmentation type")
    
    return augmented_image, transformed_annotations

def load_image(image_path):
    # Load image using OpenCV
    import cv2
    image = cv2.imread(image_path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def load_annotations(txt_path,image_shape):
    # Load annotations from text file
    annotations = []
    with open(txt_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Parse annotation format: label, x_center, y_center, width, height
            label, x_center, y_center, width, height = line.strip().split(' ')
            # Convert string values to floats
            x_center, y_center, width, height = map(float, (x_center, y_center, width, height))
            # Convert to x1, y1 (top-left) and x2, y2 (bottom-right) coordinates
            x1 = x_center - width / 2
            y1 = y_center - height / 2
            x2 = x_center + width / 2
            y2 = y_center + height / 2
            
            x1=x1*image_shape[0]
            x2=x2*image_shape[0]
            y1=y1*image_shape[1]
            y2=y2*image_shape[1]
            # Append annotation in [x1, y1, x2, y2] format
            annotations.append([label,x1, y1, x2, y2])
    return annotations

def load_direct_annotation(txt_path):
    annotations=[]
    with open(txt_path,'r') as file:
        lines = file.readlines()
        for line in lines:
            label, x_center, y_center, width, height = line.strip().split(' ')
            annotations.append([label, x_center, y_center, width, height])
    return annotations