import pathlib


PARENT_DIRECTORY = None


def set_parent_directory(file):
    global PARENT_DIRECTORY

    PARENT_DIRECTORY = pathlib.Path(file).parent.resolve()
    print("=" * 30)
    print(PARENT_DIRECTORY)
    print("=" * 30)


print(PARENT_DIRECTORY)
