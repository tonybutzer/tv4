# manages xml files
import os

FAV_DIR='/home/tony/tv/favorites'
DOWN_DIR = '/home/tony/Downloads'


def xm_get_download_files(pattern):

    # Get the path to the Downloads directory
    downloads_directory = os.path.expanduser(DOWN_DIR)

    # List all files that contain "prog"
    prog_files = [f for f in os.listdir(downloads_directory) if pattern in f]

    mydir = f'{DOWN_DIR}/'

    prepended_list = [mydir + item for item in prog_files]
    # Print the matching files
    for file in prog_files:
            print(file)

    return(prepended_list)

def xm_get_favorite_files(pattern):

    # Get the path to the Downloads directory
    downloads_directory = os.path.expanduser(FAV_DIR)

    # List all files that contain "prog"
    prog_files = [f for f in os.listdir(downloads_directory) if pattern in f]

    mydir = f'{FAV_DIR}/'

    prepended_list = [mydir + item for item in prog_files]


    # Print the matching files
    # for file in prog_files:
            # print(file)

    return(prepended_list)
