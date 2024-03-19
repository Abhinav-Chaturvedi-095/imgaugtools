import os
from .apply_augmentation import apply_augmentation
from .utils import save_image, save_annotations

def process_images(input_folder_path, output_folder_path, augmentation_type, *args):
    """
    Apply augmentation to images in the input folder and save the augmented images and annotations in the output folder.

    Parameters:
        input_folder_path (str): Path to the input folder containing images and txt files.
        output_folder_path (str): Path to the output folder where augmented images and annotations will be saved.
        augmentation_type (str): Type of augmentation to apply.
        *args: Additional arguments for the specified augmentation.

    Returns:
        None
    """
    # Ensure output folder exists
    os.makedirs(output_folder_path, exist_ok=True)

    # Iterate over files in the input folder
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load image
            name=filename[:-4]
            image_path = os.path.join(input_folder_path, filename)
            txt_path = os.path.join(input_folder_path, filename[:-4] + ".txt")

            # Apply augmentation
            augmented_image, transformed_annotations = apply_augmentation(image_path, txt_path, augmentation_type, *args)

            # Save augmented image
            img_aug_filename=f'{name}_{augmentation_type}.jpg'
            output_image_path = os.path.join(output_folder_path, img_aug_filename)
            # print(img_aug_filename)
            save_image(augmented_image, output_image_path)

            # Save annotations
            # text_aug_filename=f'{filename}_{augmentation_type}.txt'
            output_txt_path = os.path.join(output_folder_path, img_aug_filename[:-4] + ".txt")
            save_annotations(transformed_annotations, output_txt_path)

