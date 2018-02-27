import glob
import os


def find_files(folder_path):
    """
    Finds all the files in the specified folder
    :param folder_path: The path of the folder
    :return: The list of the files
    """
    files_list = [f for f in os.listdir(folder_path)]
    return files_list


def find_folders(folder_path):
    """
    Lists all the folders in the specified folder, ignoring the files
    :param folder_path: The path of the folder
    :return: The list of the folders
    """
    folders = [directory for directory in os.listdir(folder_path)
               if os.path.isdir(os.path.join(folder_path, directory))]
    return folders

