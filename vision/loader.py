import os
from utils import paths


def get_image_folder(subfolder=None):
    parent_directory = paths.PARENT_DIRECTORY
    images_folder = os.path.join(parent_directory, "images")

    if subfolder:
        images_folder = os.path.join(images_folder, subfolder)

    return images_folder


def get_image(subfolder, name_condition=""):
    images_folder = get_image_folder(subfolder)
    images = []

    for image in os.listdir(images_folder):
        if (
            name_condition in image
        ):  # This will always be true and if there is a condition, we can filter the file names.
            image_path = os.path.join(images_folder, image)
            images.append(image_path)

    return images