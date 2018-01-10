import os
import glob


def delete_files_recursively(root_folder, filepattern):
    """
    Example of finding all the files with this name/pattern that live on the root folder
    and deleting them.
    :param root_folder: The path of the folder to search in
    """
    for filename in glob.iglob(root_folder + '**/'+filepattern, recursive=True):
        os.remove(filename)
