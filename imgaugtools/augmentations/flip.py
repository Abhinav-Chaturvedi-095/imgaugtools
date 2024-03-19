import numpy as np

def flip_horizontal(image, annotations, image_shape):
    # Ensure image is at least 2D
    if len(image.shape) < 2:
        raise ValueError("Input image must be at least 2D.")

    flipped_image = np.fliplr(image)

    transformed_annotations = []
    for annotation in annotations:
        if len(annotation) != 5:
            raise ValueError("Each annotation should have four elements: [x1, y1, x2, y2]")
        
        label,x1, y1, x2, y2 = annotation
        transformed_x1 = image_shape[0] - x2
        transformed_x2 = image_shape[0] - x1
        
        x_center = (transformed_x1 + transformed_x2) / 2
        x_center_norm=x_center/image_shape[0]
        y_center = (y1 + y2) / 2
        y_center_norm=y_center/image_shape[1]
        
        width = transformed_x2 - transformed_x1
        width_norm=width/image_shape[0]
        height = y2 - y1
        height_norm=height/image_shape[1]
        
        transformed_annotations.append([label,x_center_norm, y_center_norm, width_norm, height_norm])

    return flipped_image, transformed_annotations

def flip_vertical(image, annotations, image_shape):
    # Ensure image is at least 2D
    if len(image.shape) < 2:
        raise ValueError("Input image must be at least 2D.")

    flipped_image = np.flipud(image)

    transformed_annotations = []
    for annotation in annotations:
        if len(annotation) != 5:
            raise ValueError("Each annotation should have four elements: [x1, y1, x2, y2]")
        
        label,x1, y1, x2, y2 = annotation
        transformed_y1 = image_shape[1] - y2
        transformed_y2 = image_shape[1] - y1
        
        x_center = (x1 + x2) / 2
        x_center_norm=x_center/image_shape[0]
        y_center = (transformed_y1 + transformed_y2) / 2
        y_center_norm=y_center/image_shape[1]
        
        
        height = transformed_y2 - transformed_y1
        height_norm=height/image_shape[1]
        width = x2 - x1
        width_norm=width/image_shape[0]
        
        transformed_annotations.append([label,x_center_norm, y_center_norm, width_norm, height_norm])

    return flipped_image, transformed_annotations


