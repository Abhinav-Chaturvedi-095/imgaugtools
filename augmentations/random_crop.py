import random

def random_crop(image, annotations, crop_size):
    """
    Apply random crop augmentation to the image and adjust bounding box annotations.

    Parameters:
        image (numpy.ndarray): Input image.
        annotations (list): List of bounding box annotations.
        crop_size (tuple): Size of the cropped region in the format (height, width).

    Returns:
        tuple: Tuple containing cropped image and adjusted bounding box annotations.
    """
    # Determine the maximum x and y offsets for cropping
    max_x_offset = image.shape[0] - crop_size[0]
    max_y_offset = image.shape[1] - crop_size[1]

    # Randomly select x and y offsets for cropping
    x_offset = random.randint(0, max_x_offset)
    y_offset = random.randint(0, max_y_offset)

    # Crop the image
    cropped_image = image[x_offset:x_offset + crop_size[0],y_offset:y_offset + crop_size[1]]

    # Adjust bounding box annotations
    adjusted_annotations = []
    for annotation in annotations:
        label, x_center, y_center, width, height = annotation

        # Check if bounding box intersects with cropped region
        x1 = max(0, min(image.shape[0], x_center - width / 2 - x_offset))
        y1 = max(0, min(image.shape[1], y_center - height / 2 - y_offset))
        x2 = max(0, min(image.shape[0], x_center + width / 2 - x_offset))
        y2 = max(0, min(image.shape[1], y_center + height / 2 - y_offset))

        # Convert pixel coordinates back to normalized coordinates relative to the cropped region
        if x1 < x2 and y1 < y2: 
            x_center_norm_crop = (x1 + x2) / crop_size[0]
            y_center_norm_crop = (y1 + y2) / crop_size[1]
            width_norm_crop = (x2 - x1) / crop_size[0]
            height_norm_crop = (y2 - y1) / crop_size[1]

            adjusted_annotations.append([label, x_center_norm_crop, y_center_norm_crop, width_norm_crop, height_norm_crop])

    return cropped_image, adjusted_annotations
