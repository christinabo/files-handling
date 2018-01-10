from shutil import copyfile


def copy_singlefile(src, dest):
    """
    Example of copying a file from the src file path to the dest file path using the shutil module
    :param src: The source file path
    :param dest: The destination file path
    """
    copyfile(src, dest)


if __name__ == '__main__':

    copy_singlefile('/root/folder/test.csv', 'other/folder/othername.csv')