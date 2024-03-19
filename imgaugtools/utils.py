import cv2
import numpy as np

def save_image(image, filename):
    image_uint8 = image.astype(np.uint8)
    # OpenCV uses BGR color format, so convert the image back to BGR
    image_bgr = cv2.cvtColor(image_uint8, cv2.COLOR_RGB2BGR)
    # Save the image
    cv2.imwrite(filename, image_bgr)
    
def save_annotations(annotations, filename):
    with open(filename, 'w') as f:
        for annotation in annotations:
            # Convert annotation coordinates to string format
            annotation_str = ' '.join(map(str, annotation))
            # Write annotation to file
            f.write(annotation_str + '\n')