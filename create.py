import os


def create_dir(folder_path):
    """
    Creates a folder in the destination path if does not exist already.
    :param folder_path: The path to create the folder
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)