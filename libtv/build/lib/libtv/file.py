import os

def file_uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + "__" + str(counter) + "_" + extension
        counter += 1

    return path
