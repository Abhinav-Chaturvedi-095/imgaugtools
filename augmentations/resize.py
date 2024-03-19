import numpy as np

def resize(image, annotations, new_size):
    """
    Apply resizing augmentation to the image and adjust bounding box annotations.

    Parameters:
        image (numpy.ndarray): Input image.
        annotations (list): List of bounding box annotations in original form.
        new_size (tuple): Desired dimensions (height, width) for the resized image.

    Returns:
        tuple: Tuple containing resized image and adjusted bounding box annotations in normalized form.
    """
    # Resize the image using NumPy
    print(new_size)
    image_copy = np.copy(image)
    resized_image = np.array(image_copy.resize((new_size[0], new_size[1])))
    
    # Calculate scaling factors for converting coordinates
    scale_y = new_size[1] / image.shape[1]
    scale_x = new_size[0] / image.shape[0]
    print(image.shape)
    print(resized_image.shape)
    
    # Adjust bounding box annotations
    adjusted_annotations = []
    for annotation in annotations:
        label, x_center, y_center, width, height = annotation

        # Scale the bounding box coordinates
        x_center_scaled = x_center * scale_x
        y_center_scaled = y_center * scale_y
        width_scaled = width * scale_x
        height_scaled = height * scale_y

        # Convert scaled coordinates to normalized form
        x_center_norm = x_center_scaled / new_size[0]
        y_center_norm = y_center_scaled / new_size[1]
        width_norm = width_scaled / new_size[0]
        height_norm = height_scaled / new_size[1]

        adjusted_annotations.append([label, x_center_norm, y_center_norm, width_norm, height_norm])

    return resized_image, adjusted_annotations
